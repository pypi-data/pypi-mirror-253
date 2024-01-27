import yaml
from routerfy.utils.yaml.sub import Sub, sub_representer
from routerfy.utils.yaml.ref import Ref, ref_representer
from routerfy.utils.yaml.find_in_map import FindInMap, find_in_map_representer

def get_dumper():
    """Add representers to a YAML seriailizer."""
    safe_dumper = yaml.SafeDumper
    safe_dumper.add_representer(Sub, sub_representer)
    safe_dumper.add_representer(Ref, ref_representer)
    safe_dumper.add_representer(FindInMap, find_in_map_representer)
    return safe_dumper