import xprompt
from xprompt.client_prompt_parser import ClientPromptParser
from xprompt.data_client import OutputConvertorClient
from xprompt.schemas import XPromptOutput
from xprompt.utils import send_request_with_json


class OpenAIGenerate:
    output_convertor: OutputConvertorClient = OutputConvertorClient()

    @staticmethod
    def client_prompt_parsing(messages):
        for message in messages:
            if message["role"] != "assistant":
                prompt = message["content"]
                prompt_parser = ClientPromptParser(prompt=prompt)

                # upload file to s3
                prompt_parser.handle_src_in_tag()

                # run local parsing
                message["content"], parsing_info = prompt_parser.run_services()

    @classmethod
    def create(cls, **kwargs):
        timeout = kwargs.pop("timeout", None)
        kwargs["client_type"] = "chat_completion"
        kwargs["openai_api_key"] = xprompt.openai_api_key
        output_type = kwargs.pop("output_format", None)

        # client side parsing
        cls.client_prompt_parsing(kwargs["messages"])

        # send xprompt api request
        response = send_request_with_json(
            json_payload=kwargs, endpoint="generate/", timeout=timeout
        )

        generation_response = response.json()
        if output_type and generation_response["choices"]:
            for message in generation_response["choices"]:
                content = message["message"].get("content")
                if not content:
                    continue

                byte_content = cls.output_convertor.convert(
                    text=message["message"]["content"], output_type=output_type
                )
                message["message"]["byte_content"] = byte_content

        return XPromptOutput(generation_response)


class ChatCompletion(OpenAIGenerate):
    """
    Replace of openai.ChatCompletion
    """

    @classmethod
    def create(cls, **kwargs):
        kwargs["client_type"] = "chat_completion"
        return super().create(**kwargs)


class Completion(OpenAIGenerate):
    """
    Replace of openai.Completion
    """

    @classmethod
    def create(cls, **kwargs):
        kwargs["client_type"] = "completion"
        return super().create(**kwargs)


class Embedding(OpenAIGenerate):
    """
    Replace of openai.Embedding
    """

    @classmethod
    def create(cls, **kwargs):
        kwargs["client_type"] = "embedding"
        return super().create(**kwargs)
