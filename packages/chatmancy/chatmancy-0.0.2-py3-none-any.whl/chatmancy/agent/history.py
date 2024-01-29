from abc import ABC
from typing import Dict, List
import logging


from ..message import Message, MessageQueue, UserMessage
from ..logging import trace


class HistoryGenerator(ABC):
    """Abstract Base Class for generating a history."""

    @trace(name="HistoryGenerator.create_history")
    def create_history(
        self,
        input_message: Message,
        context: Dict[str, str] = None,
    ) -> MessageQueue:
        """Method to create a history.

        Args:
            input_message: The input message.
            context: Additional context information.

        Returns:
            A MessageQueue object representing the history.
        """
        self.logger = logging.getLogger("chatmancy.HistoryGenerator")


class StaticHistoryGenerator(HistoryGenerator):
    """A class to generate a static history from a given list of statements."""

    def __init__(
        self,
        statements: List[str],
        **kwargs,
    ) -> None:
        """Initializes a StaticHistoryGenerator object."""
        super().__init__(**kwargs)

        self._message_q = MessageQueue(
            self._parse_statement(statement) for statement in statements
        )

    @staticmethod
    def _parse_statement(statement: (str | Message)) -> Message:
        if isinstance(statement, str):
            return UserMessage(statement)
        elif isinstance(statement, Message):
            return statement
        else:
            raise TypeError(
                (
                    "Invalid statement type. "
                    f"Expected a str or Message, got {type(statement)}."
                )
            )

    @trace(name="StaticHistoryGenerator.create_history")
    def create_history(
        self, input_message: Message, context: Dict[str, str] = None
    ) -> MessageQueue:
        """Creates a history for a given input message and context.

        Args:
            input_message: The input message.
            context: Additional context information.

        Returns:
            A MessageQueue object representing the history.
        """
        return self._message_q.copy()


class HistoryManager:
    """
    Manages the history of messages in a conversation.

    Args:
        generator (List[str] | HistoryGenerator): The generator used to
            create the history.
        max_prefix_tokens (int, optional): The maximum number of tokens to include in
            the prefix. Defaults to None.

    Raises:
        TypeError: If the generator is not a list of statements or a HistoryGenerator.

    Attributes:
        max_prefix_tokens (int): The maximum number of tokens to include in the prefix.
        generator (HistoryGenerator): The generator used to create the history.

    Methods:
        create_history: Creates the history based on the
            input message, context, and maximum number of tokens.
    """

    def __init__(
        self,
        generator: (List[str] | HistoryGenerator),
        max_prefix_tokens: int = None,
    ) -> None:
        self.logger = logging.getLogger("chatmancy.HistoryManager")

        # Tokens
        self.max_prefix_tokens = max_prefix_tokens

        # Create prefix
        if generator is None:
            generator = []
        if isinstance(generator, list):
            statements = [
                item["content"] if isinstance(item, dict) else item
                for item in generator
            ]
            self.generator = StaticHistoryGenerator(
                statements=statements,
            )

        elif isinstance(generator, HistoryGenerator):
            self.generator = generator
        else:
            raise TypeError(
                "generator must either be a list of statements or a HistoryGenerator, "
                f"not a {type(generator)}"
            )

    def _create_prefix(
        self, input_message: Message, context: Dict[str, str]
    ) -> MessageQueue:
        """
        Creates the prefix for the history based on the input message and context.

        Args:
            input_message (Message): The input message.
            context (Dict[str, str]): The context of the conversation.

        Returns:
            MessageQueue: The prefix for the history.
        """
        prefix = self.generator.create_history(input_message, context)
        if self.max_prefix_tokens is not None:
            prefix = MessageQueue(prefix.get_last_n_tokens(self.max_prefix_tokens))
        return prefix

    @trace(name="Agent.create_history")
    def create_history(
        self,
        input_message: Message,
        history: MessageQueue,
        context: Dict[str, str],
        max_tokens: int,
    ) -> MessageQueue:
        """
        Creates the history based on the input message, history, context,
            and maximum number of tokens.

        Args:
            input_message (Message): The input message.
            history (MessageQueue): The history of messages in the conversation.
            context (Dict[str, str]): The context of the conversation.
            max_tokens (int): The maximum number of tokens in the history.

        Returns:
            MessageQueue: The created history.

        Raises:
            ValueError: If the maximum number of tokens is less than the number
                 of tokens in the context and input message.
        """
        # Validate args
        if not isinstance(history, MessageQueue):
            try:
                history = MessageQueue(history)
            except Exception:
                raise TypeError(
                    f"history must be a MessageQueue, not a {type(history)}."
                )

        # Handle none message
        history = history.copy()
        if input_message is None:
            input_message = history.pop()

        # Prepare prefix
        self.logger.info("Creating prefix")
        self.logger.debug(f"Max prefix tokens is {self.max_prefix_tokens}")
        prefix = self._create_prefix(input_message, context)
        self.logger.debug(f"Prefix token count is {prefix.token_count}")
        if context:
            context_message = UserMessage(f"The current context is {context}")
            context_token_count = context_message.token_count
        else:
            context_message = None
            context_token_count = 0
        # Validate
        if max_tokens < context_token_count + input_message.token_count:
            raise ValueError(
                "The maximum number of tokens is less than the number of tokens in "
                "the context and input message"
            )

        # Trim
        self.logger.debug(f"Trimming history to {max_tokens} tokens")
        available_tokens = (
            max_tokens
            - prefix.token_count
            - context_token_count
            - input_message.token_count
        )

        history = history.get_last_n_tokens(available_tokens)

        # Combine
        result = prefix + history
        if context_message:
            result += [context_message]
        result += [input_message]
        return result
