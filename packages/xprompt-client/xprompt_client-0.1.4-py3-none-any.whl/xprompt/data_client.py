import xprompt
from xprompt.utils import send_request_with_json


class OutputConvertorClient:
    @classmethod
    def convert(cls, text, output_type, **kwargs):
        timeout = kwargs.pop("timeout", None)
        payload = {"text": text, "output_format": output_type, **kwargs}

        response = send_request_with_json(
            json_payload=payload, endpoint="convert_output", timeout=timeout
        )
        return response.content


if __name__ == "__main__":
    res = OutputConvertorClient()
    xprompt.api_key = ""
    content = res.convert("sure, this is something", "audio")
    with open("./test.mp3", "wb") as f:
        f.write(content)

    print("done")
