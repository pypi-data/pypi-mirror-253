from typing import Dict, Optional

from bamt_light.builders.builders_base import VerticesDefiner, EdgesDefiner
from bamt_light.log import logger_builder
from bamt_light.nodes.composite_continuous_node import CompositeContinuousNode
from bamt_light.nodes.composite_discrete_node import CompositeDiscreteNode


class CompositeDefiner(VerticesDefiner, EdgesDefiner):
    """
    Object that might take additional methods to decompose structure builder class
    """

    def __init__(
            self,
            descriptor: Dict[str, Dict[str, str]],
            regressor: Optional[object] = None,
    ):
        super().__init__(descriptor, regressor)

        # Notice that vertices are used only by Builders
        self.vertices = []

        # LEVEL 1: Define a general type of node: Discrete or Сontinuous
        for vertex, type in self.descriptor["types"].items():
            if type in ["disc_num", "disc"]:
                node = CompositeDiscreteNode(name=vertex)
            elif type == "cont":
                node = CompositeContinuousNode(name=vertex, regressor=regressor)
            else:
                msg = f"""First stage of automatic vertex detection failed on {vertex} due TypeError ({type}).
                Set vertex manually (by calling set_nodes()) or investigate the error."""
                logger_builder.error(msg)
                continue

            self.vertices.append(node)
