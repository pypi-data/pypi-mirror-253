import yaml

from typing import List

class FindInMap():
    def __init__(self, values: List[str]):
        self.values = values
    
def find_in_map_representer(dumper: yaml.SafeDumper, find_in_map: FindInMap) -> yaml.nodes.SequenceNode:
    return dumper.represent_sequence("!FindInMap", find_in_map.values, True)

def find_in_map_constructor(loader: yaml.SafeLoader, node: yaml.nodes.SequenceNode) -> FindInMap:
  return FindInMap(loader.construct_sequence(node))