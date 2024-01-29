# from xprompt.client_services.dummy_parser import DummyParser
from xprompt.utils import send_request_with_file
from xprompt_common.data_utils import FilePathType, identify_path_type
from xprompt_common.base_service import BaseService
from xprompt_common.prompt_parser import PromptParser

TAG_TO_SERVICE = {
    # "dummy": DummyParser,
}

try:
    pass

    from xprompt.client_services.llamahub_connectors.google_docs import GoogleDoc

    TAG_TO_SERVICE.update(
        {
            "gdoc": GoogleDoc,
        }
    )
except ImportError:
    pass


class ClientPromptParser(PromptParser):
    tag_to_service: dict[str, BaseService.__class__] = TAG_TO_SERVICE

    def handle_src_in_tag(self):
        """
        Upload file to server and create mapping between s3 path and original path
        Args:
            src:

        Returns:
            new s3 path
        """
        local_file_paths = []
        for tag in self.tags:
            if (
                "src" in tag.attrs
                and identify_path_type(tag["src"]) == FilePathType.LOCAL
            ):
                local_file_paths.append(tag["src"])

        if len(local_file_paths) > 0:
            response = send_request_with_file(
                file_paths=local_file_paths, endpoint="upload_files/"
            )
            s3_paths = response["s3_paths"]
            local_file_to_s3_path = {
                local_file_path: s3_path
                for local_file_path, s3_path in zip(local_file_paths, s3_paths)
            }

            for tag in self.tags:
                if (
                    "src" in tag.attrs
                    and identify_path_type(tag["src"]) == FilePathType.LOCAL
                ):
                    if tag["src"] in local_file_to_s3_path:
                        tag["src"] = local_file_to_s3_path[tag["src"]]
                    else:
                        raise RuntimeError(f"Failed to handle {tag['src']}")
