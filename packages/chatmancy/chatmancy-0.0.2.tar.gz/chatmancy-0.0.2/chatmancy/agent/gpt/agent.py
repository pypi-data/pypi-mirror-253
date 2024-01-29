from typing import List

from ...agent.base import Agent, TokenSettings
from ...agent.history import HistoryGenerator
from ...message import Message


from .model import GPTModelHandler
from .history import GPTHistoryManager


class GPTAgent(Agent):
    """
    Agent class for generating chat responses using GPT

    Args:
        name: The name of the agent.
        desc: A description of the agent.
        model: The name of the OpenAI model to use.
        system_prompt: The prompt to use when generating system responses.
        history: A generator to add a history prefix to all calls to the agent.
        token_settings: Settings for the token generation.
        model_max_tokens: The maximum number of tokens to generate for the model.
            Required if the passed model is not recorded in GPTModelHandler.

    """

    def __init__(
        self,
        name: str,
        desc: str,
        model: str,
        system_prompt: str = "You are a helpful chat agent.",
        history: (List[str] | HistoryGenerator) = None,
        token_settings: (TokenSettings | dict) = None,
        model_max_tokens: int = None,
    ) -> None:
        """Create a new Agent instance.

        Args:
            name: The name of the agent.
            desc: A description of the agent.
        """
        super().__init__(
            name=name,
            desc=desc,
            model=model,
            system_prompt=system_prompt,
            history=history,
            token_settings=token_settings,
            model_max_tokens=model_max_tokens,
        )

    def _initialize_model_handler(
        self, model: str, model_max_tokens: int = None, **kwargs
    ):
        return GPTModelHandler(model=model, max_tokens=model_max_tokens)

    def _initialize_history_manager(
        self, history: (List[str] | HistoryGenerator), system_prompt: str, **kwargs
    ):
        return GPTHistoryManager(
            system_message=Message(sender="system", content=system_prompt),
            generator=history,
            max_prefix_tokens=self.token_settings.max_prefix_tokens,
        )
