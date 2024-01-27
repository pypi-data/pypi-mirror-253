from garak.generators.base import Generator

from ..engine.config import _get_default_agent_config

class Agent(Generator):
    """
    Generic Agent class, takes after the Generator class in garak
    """
        
    def __init__(self, name, generations: float = 10):
    # def __init__(self, name, config: AgentConfig=None):
        """
        Initializes the Agent class, given a `name`.
        """
        super().__init__(name, generations)
        # if config is None:
        config = _get_default_agent_config(family="", name=self.name)
        for field in [
                "endpoint","max_tokens", "presence_penalty", "temperature", "top_k", "seed","presence_penalty","supports_multiple_generations"
            ]:
            if hasattr(config, field):
                setattr(self, field, getattr(config, field))