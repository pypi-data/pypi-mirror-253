from typing import Optional, Union

from llama_index.core.llms.llm import LLM
from llama_index.core.llms.mock import MockLLM
from llama_index.core.llms.openai import OpenAI
from llama_index.core.llms.openai_utils import validate_openai_api_key

LLMType = Union[str, LLM]


def resolve_llm(llm: Optional[LLMType] = None) -> LLM:
    """Resolve LLM from string or LLM instance."""
    if llm == "default":
        # return default OpenAI model. If it fails, return Mock
        try:
            llm = OpenAI()
            validate_openai_api_key(llm.api_key)
        except ValueError as e:
            raise ValueError(
                "\n******\n"
                "Could not load OpenAI model. "
                "If you intended to use OpenAI, please check your OPENAI_API_KEY.\n"
                "Original error:\n"
                f"{e!s}"
                "\nTo disable the LLM entirely, set llm=None."
                "\n******"
            )
    elif llm is None:
        print("LLM is explicitly disabled. Using MockLLM.")
        llm = MockLLM()

    return llm
