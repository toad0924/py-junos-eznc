"""
Pythonifier for PhyPort Table/View
"""
from ..factory import loadyaml
_YAML_ = __file__.replace('.py','.yml')
globals().update(loadyaml(_YAML_))