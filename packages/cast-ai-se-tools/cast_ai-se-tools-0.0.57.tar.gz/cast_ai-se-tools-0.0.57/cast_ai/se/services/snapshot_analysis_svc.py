import logging
import re
from typing import Dict, Any

from cast_ai.se.constants import (NON_RELEVANT_NAMESPACES, POD_SPEC_KEYWORDS, CLOUD_TAINTS, K8S_WORKLOADS,
                                  WORKLOAD_MAP, RS_ASH_PATTERN)
from cast_ai.se.models.redfined_snapshot import RefinedSnapshot
from cast_ai.se.models.redfined_snapshot_analysis import RefinedSnapshotAnalysis


class SnapshotAnalyzer:
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._refined_snapshot = None
        self._rs_metadata = RefinedSnapshotAnalysis()

    def refine_snapshot(self, snapshot_data: Dict[str, Any]):
        self._refined_snapshot = RefinedSnapshot()
        self._refine_snapshot_workloads(snapshot_data)
        self._refine_snapshot_pdbs(snapshot_data)
        self._summarize_rs_object_types()
        # self._refine_snapshot_nodes(rf, snapshot_data)

    def _summarize_rs_object_types(self) -> None:

        for workload_type, workload_list in self._refined_snapshot.workloads.__dict__.items():
            for workload in workload_list:
                for reason in workload["refined_reason"]:
                    if workload["namespace"] not in self._rs_metadata[reason][workload_type]:
                        self._rs_metadata[reason][workload_type][workload["namespace"]] = set()
                    self._rs_metadata[reason][workload_type][workload["namespace"]].add(workload["name"])
                    self._rs_metadata[reason][workload_type]["total"] += 1
                    self._rs_metadata[reason]["total"] += 1
                    self._rs_metadata.counters["total"] += 1

    def _get_taints_or_tolerations(self, item: Dict[str, Any], keyword: str):
        taints_or_tolerations_list = []
        for taint_or_toleration in item["spec"][keyword]:
            if "key" not in taint_or_toleration.keys() or taint_or_toleration["key"] not in CLOUD_TAINTS:
                print()
                taints_or_tolerations_list.append(taint_or_toleration)
            else:
                if "key" not in item.keys():
                    self._logger.info(f'Ignored {keyword} as no key found')
                else:
                    self._logger.info(f'Ignored {keyword} as no key part of known cloud taints')
        return taints_or_tolerations_list

    def _refine_snapshot_pdbs(self, snapshot_data: Dict[str, Any]) -> None:
        if snapshot_data["podDisruptionBudgetList"]["items"]:
            for pdb in snapshot_data["podDisruptionBudgetList"]["items"]:
                if pdb["metadata"]["namespace"] in NON_RELEVANT_NAMESPACES:
                    self._logger.info(f'Ignored pdb {pdb["metadata"]["name"]} (it`s in {pdb["metadata"]["namespace"]})')
                    continue
                new_refined_pdb = {"name": pdb["metadata"]["name"],
                                   "namespace": pdb["metadata"]["namespace"],
                                   "spec": pdb["spec"]}
                self._logger.info(f'Found pdb {pdb["metadata"]["name"]} in {pdb["metadata"]["namespace"]}')
                self._refined_snapshot.pdbs.append(new_refined_pdb)

    # def _refine_snapshot_nodes(self, rf: RefinedSnapshot,  snapshot_data: Dict[str, Any]) -> None:
    #     self._logger.info(f"Starting to refine nodes...")
    #     for node in snapshot_data["nodeList"]["items"]:
    #         new_refined_node= {"name": node["metadata"]["name"]}
    #         if "labels" in node["metadata"].keys():
    #             new_refined_node["labels"] = node["metadata"]["labels"]
    #         if "taints" in node["spec"].keys():
    #             taint_list = self._get_taints_or_tolerations(node, "taints")
    #             if taint_list:
    #                 new_refined_node["taints"] = taint_list
    #                 self._logger.info(f"Found taints on {node['metadata']['name']}")
    #         if len(new_refined_node) > 1:
    #             rf.nodes.append(new_refined_node)

    def _refine_snapshot_workloads(self, snapshot_data: Dict[str, Any]) -> None:
        for workload_key in K8S_WORKLOADS:
            if snapshot_data[workload_key]["items"]:
                self._logger.info(f"Starting to refine workloads({workload_key})...")

                for workload in snapshot_data[workload_key]["items"]:
                    if workload["metadata"]["namespace"] in NON_RELEVANT_NAMESPACES:
                        continue
                    if workload_key == "replicaSetList" and re.search(RS_ASH_PATTERN, workload["metadata"]["name"]):
                        continue
                    new_refined_workload = {"name": workload["metadata"]["name"],
                                            "namespace": workload["metadata"]["namespace"],
                                            "refined_reason": []}
                    self._refine_podspec(new_refined_workload, workload)
                    self._refine_tolerations(new_refined_workload, workload)
                    if "requests" not in workload["spec"]["template"]["spec"].keys():
                        new_refined_workload["refined_reason"].append("no_requests")
                    if len(new_refined_workload) > 2:
                        self._refined_snapshot.workloads.add_item(WORKLOAD_MAP[workload_key], new_refined_workload)

    def _refine_tolerations(self, new_refined_workload: Dict[str, Any], workload: Dict[str, Any]) -> None:
        if "tolerations" in workload["spec"]["template"]["spec"].keys():
            toleration_list = self._get_taints_or_tolerations(workload["spec"]["template"], "tolerations")
            if toleration_list:
                new_refined_workload["tolerations"] = toleration_list
                self._logger.debug(f"Added toleration's data ({toleration_list}) to {new_refined_workload['name']}")
                new_refined_workload["refined_reason"].append("tolerations")

    def _refine_podspec(self, new_refined_workload: Dict[str, Any], workload: Dict[str, Any]) -> None:
        for spec_keyword in POD_SPEC_KEYWORDS:
            if spec_keyword in workload["spec"]["template"]["spec"].keys():
                new_refined_workload[spec_keyword] = workload["spec"]["template"]["spec"][spec_keyword]
                self._logger.debug(f"Added {spec_keyword} to {new_refined_workload['name']}")
                new_refined_workload["refined_reason"].append(spec_keyword)

    def generate_report(self, detailed: bool = False) -> str:
        report = (f"{self._rs_metadata.counters['total']} "
                  f"Workloads with scheduling-challenging settings:\n")
        for reason in [key for key in self._rs_metadata.counters.keys() if key != "total"]:
            if self._rs_metadata.counters[reason]['total']:
                report += f"\t- {self._rs_metadata.counters[reason]['total']} workloads with {reason} field\n"
                report = self._add_workloads_to_report(detailed, reason, report)
        return report

    def _add_workloads_to_report(self, detailed: bool, reason: str, report: str):
        for workload_type in [key for key in self._rs_metadata.counters[reason].keys() if key != "total"]:
            if self._rs_metadata.counters[reason][workload_type]['total']:
                report += (f"\t\t- {self._rs_metadata.counters[reason][workload_type]['total']} {workload_type}"
                           f"\n")
                if detailed:
                    report = self._add_detailed_workloads_to_report(reason, report, workload_type)
        return report

    def _add_detailed_workloads_to_report(self, reason: str, report: str, workload_type: str) -> str:
        for namespace in self._rs_metadata.counters[reason][workload_type].keys():
            if namespace != "total":
                report += f"\t\t\t- {namespace}\n"
                for workload_name in (
                        list(self._rs_metadata.counters[reason][workload_type][namespace])):
                    report += f"\t\t\t\t- {workload_name}\n"
        return report
