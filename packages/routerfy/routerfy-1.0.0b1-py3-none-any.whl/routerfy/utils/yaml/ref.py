import yaml

class Ref():
    def __init__(self, value: str):
        self.value = value
    
def ref_representer(dumper: yaml.SafeDumper, ref: Ref) -> yaml.nodes.ScalarNode:
    return dumper.represent_scalar("!Ref", ref.value)

def ref_constructor(loader: yaml.SafeLoader, node: yaml.nodes.ScalarNode) -> Ref:
  return Ref(str(loader.construct_scalar(node)))