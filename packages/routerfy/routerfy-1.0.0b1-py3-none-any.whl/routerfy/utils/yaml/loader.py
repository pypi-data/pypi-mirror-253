import yaml

from routerfy.utils.yaml.sub import sub_constructor
from routerfy.utils.yaml.ref import ref_constructor
from routerfy.utils.yaml.find_in_map import find_in_map_constructor

def get_loader():
  loader = yaml.SafeLoader
  loader.add_constructor("!Sub", sub_constructor)
  loader.add_constructor("!Ref", ref_constructor)
  loader.add_constructor("!FindInMap", find_in_map_constructor)
  return loader