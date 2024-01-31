import re
from typing import Dict

from bamt_light.builders.composite_builder import CompositeDefiner
from bamt_light.networks.base import BaseNetwork


class CompositeBN(BaseNetwork):
    """
    Composite Bayesian Network with Machine Learning Models support
    """

    def __init__(self):
        super(CompositeBN, self).__init__()
        self._allowed_dtypes = ["cont", "disc", "disc_num"]
        self.type = "Composite"
        self.parent_models = {}

    def add_nodes(self, descriptor: Dict[str, Dict[str, str]]):
        """
        Function for initializing nodes in Bayesian Network
        descriptor: dict with types and signs of nodes
        """
        self.descriptor = descriptor

        worker_1 = CompositeDefiner(descriptor=descriptor, regressor=None)
        self.nodes = worker_1.vertices

    def set_classifiers(self, classifiers: Dict[str, object]):
        """
        Set classifiers for logit nodes.
        classifiers: dict with node_name and Classifier
        """
        for node in self.nodes:
            if node.name in classifiers.keys():
                node.classifier = classifiers[node.name]
                node.type = re.sub(
                    r"\([\s\S]*\)", f"({type(node.classifier).__name__})", node.type
                )
            else:
                continue

    def set_regressor(self, regressors: Dict[str, object]):
        """
        Set regressor for gaussian nodes.
        classifiers: dict with node_name and regressors
        """
        for node in self.nodes:
            if node.name in regressors.keys():
                node.regressor = regressors[node.name]
                node.type = re.sub(
                    r"\([\s\S]*\)", f"({type(node.regressor).__name__})", node.type
                )
            else:
                continue
