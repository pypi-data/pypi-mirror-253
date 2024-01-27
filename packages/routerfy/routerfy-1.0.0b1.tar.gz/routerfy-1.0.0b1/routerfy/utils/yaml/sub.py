import yaml

class Sub():
    def __init__(self, value: str):
        self.value = value
    
def sub_representer(dumper: yaml.SafeDumper, sub: Sub) -> yaml.nodes.ScalarNode:
    return dumper.represent_scalar("!Sub", sub.value)

def sub_constructor(loader: yaml.SafeLoader, node:yaml.nodes.ScalarNode) -> Sub:
  return Sub(str(loader.construct_scalar(node)))