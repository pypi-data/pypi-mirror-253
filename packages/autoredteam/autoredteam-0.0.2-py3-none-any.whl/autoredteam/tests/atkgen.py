from garak.probes.atkgen import Tox
from .base import Test

## TODO: make this work
probe_instance = Tox()


class ToxicityAttack(Test):
    
    probe = probe_instance
    __doc__ = probe_instance.__doc__
    name = 'atkgen.ToxicityAttack'
    description = probe_instance.description
    goal = probe_instance.goal
    uri = probe_instance.uri
    detectors = probe_instance.recommended_detector
    tags = ['vijil:Toxicity', 'source:garak'] + probe_instance.tags
    
    def generate(self, agent, logged=False):
        """
        Generate attempts by calling an agent.
        """
        self.attempt_results = self.probe.probe(agent)


# import probe and instantiate
# module_name = "atkgen"
# probe_module = importlib.import_module(f"garak.probes.{module_name}")

# # get all probes under probe module
# all_probes = [p for p in dir(probe_module) if not p.startswith("_") and p != "Path" and p != "Probe"]

# # create Test classes for all probes
# this = sys.modules[__name__]

# for probe_name in all_probes:
#     # import probe and instantiate
#     probe_instance = getattr(probe_module, probe_name)()
#     # import detectors and instantiate
#     probe_detectors = []
#     for detector in probe_instance.recommended_detector:
#         module_name, detector_name = detector.split(".")
#         detector_module = importlib.import_module(f"garak.detectors.{module_name}")
#         probe_detectors.append(getattr(detector_module, detector_name)())

#     # define test class based on probe
#     classname = probe_name
#     setattr(
#         this,
#         classname,
#         type(
#             classname,
#             (Test,),
#             {
#                 "__init__": local_constructor,
#                 "__doc__": probe_instance.__doc__,
#                 "probe": probe_instance,
#                 "detectors": probe_detectors,
#                 "uri": probe_instance.uri,
#                 "description": probe_instance.description,
#                 "tags": ['vijil:Toxicity', 'source:garak'] + probe_instance.tags,
#                 "goal": probe_instance.goal,
#             },
#         ),
#     )
