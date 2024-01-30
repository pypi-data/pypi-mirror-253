"""
Wrapper for the Grooper API. It encapsulates the API's functionality in an
object-oriented manner, and provides a more Pythonic interface for interacting
with Grooper.
"""

import json
import re
from abc import ABC
from dataclasses import dataclass
from typing import Optional
from urllib.parse import urljoin

import requests

from grooper.exceptions import GrooperError
from grooper.utils.tools import JSONType
from grooper.utils.tools import PrimitiveJSONType
from grooper.utils.tools import to_snake_case


class API(ABC):
    """
    Class for managing API requests. It holds all the logic for making requests
    to the Grooper API, and provides a simple interface for interacting with
    Grooper.
    """

    base_path: str = "/api/v1/BatchProcessing"
    url: Optional[str] = None
    key: Optional[str] = None
    timeout: int = 30
    debug_mode = False

    @staticmethod
    def _request(method: str, endpoint: str, **kwargs) -> JSONType:
        if not API.url:
            raise ValueError("API URL not set")
        if not API.key:
            raise ValueError("API key not set")

        response: requests.Response = requests.request(
            method=method,
            url=urljoin(base=API.url, url=endpoint.replace(" ", "%20")),
            headers={"APIKey": API.key},
            timeout=API.timeout,
            **kwargs,
        )

        if (
            response.url is None
            or response.status_code is None
            or response.text is None
            or response.content is None
        ):
            raise GrooperError("Error connecting to Grooper.")

        request_url: str = response.url
        status: int = response.status_code
        text: str = response.text
        last_content: bytes = bytes(response.content)

        if API.debug_mode:
            print(f"Request: /{method} {request_url}")
            if kwargs:
                print(f"\tBody: {kwargs}")
            print("Response:")
            print(f"\tStatus: {status}")
            print(f"\tContent-Type: {response.headers.get('content-type')}")
            print(f"\tEncoded content: {'True' if last_content else 'False'}")

        if status != 200:
            raise GrooperError(f"Request failed with status {status}: {text}")
        if "json" in response.headers.get("content-type", ""):
            data: JSONType = response.json()
            if isinstance(data, dict) and "Message" in data:
                raise GrooperError(data["Message"])
            return data
        if "html" in response.headers.get("content-type", ""):
            return text
        return last_content

    @staticmethod
    def get(endpoint: str, **kwargs) -> JSONType:
        """
        Performs a GET request to the Grooper API.
        """
        return API._request(method="GET", endpoint=endpoint, **kwargs)

    @staticmethod
    def post(endpoint: str, **kwargs) -> JSONType:
        """
        Performs a POST request to the Grooper API.
        """
        return API._request(method="POST", endpoint=endpoint, **kwargs)

    @staticmethod
    def delete(endpoint: str) -> bool:
        """
        Performs a DELETE request to the Grooper API.
        """
        return API._request(method="DELETE", endpoint=endpoint) == b"true"


@dataclass(kw_only=True)
class Node:
    """
    Abstract class to represent a node from the Grooper tree.
    Properties:
    - `id`: The unique ID of this node.
    - `name`: The name of the node.
    - `node_index`: A 0-based index indicating the node's position
    within its parent.
    - `num_children`: Indicates how many children the node has.
    - `parent_id`: The unique ID of the node's parent.
    - `type_name`: The type of node.
    """

    id: str  # pylint: disable=W0622
    name: str
    node_index: int | None = None
    num_children: int | None = None
    parent_id: Optional[str] = None
    type_name: Optional[str] = None

    def __repr__(self) -> str:
        properties: list[str] = [
            f"{key}={value}" if isinstance(value, int) else f'{key}="{value}"'
            for key, value in self.__dict__.items()
            if key != "base_path"
        ]
        return f"Batch({', '.join(properties)})"

    def __str__(self) -> str:
        return json.dumps(obj=self.__dict__, indent=4)


class Batch(Node):
    """
    Class for interacting with batches.

    Properties:
    - `id`: The unique ID of this node.
    - `name`: The name of the node.
    - `node_index`: A 0-based index indicating the node's position
    within its parent.
    - `num_children`: Indicates how many children the node has.
    - `parent_id`: The unique ID of the node's parent.
    - `type_name`: The type of node.
    - `created`: The date and time the batch was created.
    - `created_by`: The name of the user who created the batch.
    - `priority`: The priority of the batch.
    - `root_folder_id`: The ID of the root folder of the batch.
    - `status`: The current processing status of the batch.
    - `step_no`: The 0-based index of the step the batch is currently
    processing through.
    """

    base_path: str = f"{API.base_path}/Batches"

    STATUSES: dict[int, str] = {
        0: "None",
        1: "Ready",
        2: "Working",
        3: "Complete",
        4: "Paused",
        5: "Error",
    }

    def __init__(self, **kwargs) -> None:
        assert "id" in kwargs, "`id` is a required argument"
        assert "name" in kwargs, "`name` is a required argument"
        Node.__init__(
            self=self,
            id=kwargs.get("id"),  # type: ignore
            name=kwargs.get("name"),  # type: ignore
            node_index=kwargs.get("node_index"),
            num_children=kwargs.get("num_children"),
            parent_id=kwargs.get("parent_id"),
            type_name=kwargs.get("type_name"),
        )
        self.created: str = kwargs.get("created", None)
        self.created_by: str = kwargs.get("created_by", None)
        self.priority: int = kwargs.get("priority", None)
        self.root_folder_id: str = kwargs.get("root_folder_id", None)
        self._status: int = kwargs.get("status", None)
        self.step_no: int = kwargs.get("step_no", None)

    @property
    def status(self) -> str:
        """
        Return the status of the batch by its status code.
        """
        return self.STATUSES[self._status]

    @status.setter
    def status(self, value: str | int) -> None:
        if isinstance(value, str):
            value = {v: k for k, v in self.STATUSES.items()}[value]
        self._status = value

    @staticmethod
    def find(id: str) -> "Batch":  # pylint: disable=W0622
        """
        Gets information about a batch. Requires a batch ID.
        """
        batch: JSONType = API.get(endpoint=f"{Batch.base_path}/{id}")
        if not isinstance(batch, dict):
            raise GrooperError(f"Batch {id} not found.")
        batch = {to_snake_case(name=key): value for key, value in batch.items()}
        return Batch(**batch)

    @staticmethod
    def all() -> list["Batch"]:
        """
        Gets information about all batches.
        """
        response: JSONType = API.get(endpoint=f"{Batch.base_path}/All")

        if not isinstance(response, list):
            raise GrooperError("Error retrieving batches.")

        batches: list["Batch"] = []
        for batch in response:
            if not isinstance(batch, dict):
                raise GrooperError("Error retrieving batches.")
            batches.append(
                Batch(
                    **{to_snake_case(name=key): value for key, value in batch.items()}
                )
            )

        return batches

    @staticmethod
    def create(process_name: str, batch_name: Optional[str] = None) -> "Batch":
        """
        Creates an empty batch. Requires the name of a published batch process,
        and a name to use on batch creation.
        """
        endpoint: str = f"{API.base_path}/Processes/{process_name}/CreateBatch"
        batch: JSONType = API.post(
            endpoint=endpoint, params={"BatchName": batch_name if batch_name else ""}
        )

        if not isinstance(batch, dict):
            raise GrooperError("Error creating batch.")

        batch = {to_snake_case(name=key): value for key, value in batch.items()}
        return Batch(**batch)

    def start(self) -> "Batch":
        """
        Starts or resumes a batch. The statuses are:

        - None
        - Ready
        - Working
        - Complete
        - Paused
        - Error
        """
        response: JSONType = API.get(endpoint=f"{Batch.base_path}/{self.id}/Start")
        if not isinstance(response, dict):
            raise GrooperError("Error starting batch.")
        self.status = response["Status"] if isinstance(response["Status"], int) else 0
        self.step_no = response["StepNo"] if isinstance(response["StepNo"], int) else 0
        return self

    def pause(self) -> "Batch":
        """
        Pauses a batch. The statuses are:

        - None
        - Ready
        - Working
        - Complete
        - Paused
        - Error
        """
        response: JSONType = API.get(endpoint=f"{Batch.base_path}/{self.id}/Pause")
        if not isinstance(response, dict):
            raise GrooperError("Error starting batch.")
        self.status = response["Status"] if isinstance(response["Status"], int) else 0
        self.step_no = response["StepNo"] if isinstance(response["StepNo"], int) else 0
        return self

    def delete(self) -> bool:
        """
        Deletes a batch.
        """
        response: JSONType = API.delete(endpoint=f"{Batch.base_path}/{self.id}")

        if not isinstance(response, bool):
            raise GrooperError("Error deleting batch.")

        return response is True

    def get_batch_process_info(self, verbose=True) -> JSONType:
        """
        Gets information about the process associated with a batch. May be set
        to verbose. When verbose is set to true, will return information about
        the steps in the batch process as well.
        """
        return API.get(
            endpoint=f"{Process.base_path}es/{self.id}", params={"Verbose": verbose}
        )


class Process(Node):
    """
    Class for interacting with processes.

    Properties:

    - `id`: The unique ID of this node.
    - `name`: The name of the node.
    - `node_index`: A 0-based index indicating the node's position
    within its parent.
    - `num_children`: Indicates how many children the node has.
    - `parent_id`: The unique ID of the node's parent.
    - `type_name`: The type of node.
    - `parent_process_id`: The ID of the parent process.
    - `published_date`: The date and time the process was published.
    - `steps`: A list of steps in the process.
    """

    base_path: str = f"{API.base_path}/Process"

    def __init__(self, **kwargs) -> None:
        assert "id" in kwargs, "`id` is a required argument"
        assert "name" in kwargs, "`name` is a required argument"
        Node.__init__(
            self=self,
            id=kwargs.get("id"),  # type: ignore
            name=kwargs.get("name"),  # type: ignore
            node_index=kwargs.get("node_index"),
            num_children=kwargs.get("num_children"),
            parent_id=kwargs.get("parent_id"),
            type_name=kwargs.get("type_name"),
        )
        self.parent_process_id: str = kwargs.get("parent_process_id", None)
        self.published_date: str = kwargs.get("published_date", None)
        self.steps: list[dict] = kwargs.get("steps", None)

    @staticmethod
    def all(verbose: bool = False) -> list["Process"]:
        """
        Gets information about all processes. Can be set to verbose.
        """
        endpoint: str = f"{Process.base_path}es"

        response: JSONType = API.get(
            endpoint=endpoint,
            params={"Verbose": "true" if verbose else "false"},
        )

        if not isinstance(response, list):
            raise GrooperError("Error retrieving processes.")

        processes: list["Process"] = []
        for process in response:
            if not isinstance(process, dict):
                raise GrooperError("Error retrieving processes.")
            processes.append(
                Process(
                    **{to_snake_case(name=key): value for key, value in process.items()}
                )
            )

        return processes

    @staticmethod
    def find(name: str) -> "Process":
        """
        Gets information about a process. Requires a name.
        """
        response: JSONType = API.get(
            endpoint=f"{Process.base_path}", params={"Process": name}
        )

        if not isinstance(response, dict):
            raise GrooperError(f"Process {name} not found.")

        process: dict[str, PrimitiveJSONType] = {
            to_snake_case(name=key): value for key, value in response.items()
        }

        return Process(**process)


@dataclass(kw_only=True)
class Page(Node):
    """
    Class for interacting with folders.

    Properties:
    - `id`: The unique ID of this node.
    - `name`: The name of the node.
    - `node_index`: A 0-based index indicating the node's position within its
    parent.
    - `num_children`: Indicates how many children the node has.
    - `parent_id`: The unique ID of the node's parent.
    - `type_name`: The type of node.
    - `pixel_format`: The pixel format of the page.
    - `width`: The width of the page.
    - `height`: The height of the page.
    - `original_page_no`: The original page number of the page.
    - `primary_image`: The name of a resource which returns the primary image
    for this page.
    - `display_image`: The name of a resource which returns the display image
    for this page.
    """

    pixel_format: Optional[str] = None
    width: int | None = None
    height: int | None = None
    original_page_no: int | None = None
    primary_image: Optional[str] = None
    display_image: Optional[str] = None

    def __init__(self, **kwargs) -> None:
        assert "id" in kwargs, "`id` is a required argument"
        assert "name" in kwargs, "`name` is a required argument"
        Node.__init__(
            self=self,
            id=kwargs.get("id"),  # type: ignore
            name=kwargs.get("name"),  # type: ignore
            node_index=kwargs.get("node_index"),
            num_children=kwargs.get("num_children"),
            parent_id=kwargs.get("parent_id"),
            type_name=kwargs.get("type_name"),
        )
        self.pixel_format: Optional[str] = kwargs.get("pixel_format")
        self.width: int | None = kwargs.get("width")
        self.height: int | None = kwargs.get("height")
        self.original_page_no: int | None = kwargs.get("original_page_no")
        self.primary_image: Optional[str] = kwargs.get("primary_image")
        self.display_image: Optional[str] = kwargs.get("display_image")


class Folder(Node):  # pylint: disable=too-many-instance-attributes
    """
    Class for interacting with folders.

    Properties:
    - `id`: The unique ID of this node.
    - `name`: The name of the node.
    - `node_index`: A 0-based index indicating the node's position within its
    parent.
    - `num_children`: Indicates how many children the node has.
    - `parent_id`: The unique ID of the node's parent.
    - `type_name`: The type of node.
    - `attachment`: The name of a resource which returns the attachment for
    this document.
    - `data_is_valid`: Indicates whether all data elements were valid when the
    document was lasted saved.
    - `flag`: The flag message attached to the folder. A NULL value indicates
    the item is not flagged.
    - `json_data`: The name of a resource which returns the document metadata
    in JSON format.
    - `mime_type`: The MIME type of the attachment.
    - `pdf_version`: The name of a resource which returns the PDF version for
    this document.
    - `type_id`: The ID of the content type assigned to the item.
    - `xml_data`: The name of a resource which returns the document metadata
    in XML format.
    """

    base_path: str = f"{API.base_path}/Folders"

    def __init__(self, **kwargs) -> None:
        assert "id" in kwargs, "`id` is a required argument"
        assert "name" in kwargs, "`name` is a required argument"
        Node.__init__(
            self=self,
            id=kwargs.get("id"),  # type: ignore
            name=kwargs.get("name"),  # type: ignore
            node_index=kwargs.get("node_index"),
            num_children=kwargs.get("num_children"),
            parent_id=kwargs.get("parent_id"),
            type_name=kwargs.get("type_name"),
        )
        self.attachment: Optional[str] = kwargs.get("attachment")
        self.data_is_valid: bool | None = kwargs.get("data_is_valid")
        self.flag: Optional[str] = kwargs.get("flag")
        self.json_data: Optional[str] = kwargs.get("json_data")
        self.mime_type: Optional[str] = kwargs.get("mime_type")
        self.pdf_version: Optional[str] = kwargs.get("pdf_version")
        self.type_id: Optional[str] = kwargs.get("type_id")
        self.xml_data: Optional[str] = kwargs.get("xml_data")

    @staticmethod
    def find(id: str) -> "Folder":  # pylint: disable=W0622
        """
        Gets information about a batch folder. Requires a Folder ID.
        """
        response: JSONType = API.get(endpoint=f"{Folder.base_path}/{id}")

        if not isinstance(response, dict):
            raise GrooperError(f"Folder {id} not found.")

        folder: dict[str, PrimitiveJSONType] = {
            to_snake_case(name=key): value for key, value in response.items()
        }

        return Folder(**folder)

    def create_child_folder(self, metadata: dict | None = None) -> "Folder":
        """
        Creates and empty folder. A json object containing a classification and
        metadata may be included, which will classify and populate the folder
        index data.
        """
        endpoint: str = f"{Folder.base_path}/{self.id}/CreateFolder"
        if metadata is not None:
            self.validate_metadata(metadata=metadata)
            folder: JSONType = API.post(endpoint=endpoint, json=metadata)
        else:
            # Creates a folder with no metadata
            folder: JSONType = API.post(endpoint=endpoint)

        if not isinstance(folder, dict):
            raise GrooperError("Error creating folder.")

        folder = {to_snake_case(name=key): value for key, value in folder.items()}

        return Folder(**folder)

    def validate_metadata(self, metadata: dict) -> None:
        """
        Validates the metadata of the folder.
        """
        if not isinstance(metadata, dict):
            raise TypeError("Metadata is not a dictionary")
        if len(metadata.keys()) == 0:
            raise ValueError("Metadata can't be an empty dictionary")
        if "ContentTypeId" in metadata:
            self.validate_content_type(content_type=metadata["ContentTypeId"])
        if "FieldValues" in metadata:
            self.validate_field_values(field_values=metadata["FieldValues"])

    @staticmethod
    def validate_content_type(content_type: str) -> None:
        """
        Validates the content type of the metadata.
        """
        if not isinstance(content_type, str):
            raise TypeError("Content Type is not a string")
        if not re.match(
            pattern=r"^[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$", string=content_type
        ):
            raise GrooperError("Correct the format of Content Type")

    @staticmethod
    def validate_field_values(field_values: list) -> None:
        """
        Validates the field values of the metadata.
        """
        if not isinstance(field_values, list):
            raise TypeError("Field Values is not a list")
        if len(field_values) > 0:
            for field_value in field_values:
                if not isinstance(field_value, dict):
                    raise ValueError("Each Field Value must be a dictionary")
                if "Key" not in field_value:
                    raise ValueError("Key must be present in field value")
                if "Value" not in field_value:
                    raise ValueError("Value must be present in field value")
                if not isinstance(field_value["Key"], str):
                    raise ValueError("Key must be a string")
                if not isinstance(field_value["Value"], (str, int, float)):
                    raise ValueError("Value must be a string, integer or float")

    def get_child_folders(self, level: int) -> list["Folder"]:
        """
        Gets information about child folders. Requires a child level. It will
        return information about all child folders AT THE SPECIFIED LEVEL ONLY.
        """
        if level < 0:
            raise GrooperError("Level must be greater than or equal to 0.")

        response: JSONType = API.get(
            endpoint=f"{Folder.base_path}/{self.id}/Folders",
            params={"Level": level},
        )

        if not isinstance(response, list):
            raise GrooperError("Error retrieving folders.")

        folders: list["Folder"] = []
        for folder in response:
            if not isinstance(folder, dict):
                raise GrooperError("Error retrieving folders.")
            folders.append(
                Folder(
                    **{to_snake_case(name=key): value for key, value in folder.items()}
                )
            )
        return folders

    def create_page(self, file: bytes) -> bool:
        """
        Creates a page inside a batch folder.
        Requires a local PDF or image file to stream.
        """
        response: JSONType = API.post(
            endpoint=f"{Folder.base_path}/{self.id}/CreatePage", data=file
        )

        if not isinstance(response, bool):
            raise GrooperError("Error creating page.")

        return response is True

    def get_pages(self, recursive: bool = False) -> list[Page]:
        """
        Gets information about page children of a folder.
        May be run recursively.
        """
        response: JSONType = API.get(
            endpoint=f"{Folder.base_path}/{self.id}/Pages",
            params={"Recursive": recursive},
        )

        if not isinstance(response, list):
            raise GrooperError("Error retrieving pages.")

        pages: list = []
        for page in response:
            if not isinstance(page, dict):
                raise GrooperError("Error retrieving pages.")
            pages.append(
                Page(**{to_snake_case(name=key): value for key, value in page.items()})
            )

        return pages

    def set_metadata(self, metadata: dict[str, str | list]) -> JSONType:
        """
        Updates the Index Data Associated with a document. Requires a JSON
        containing the index data. The JSON must contain a ContentTypeID and a
        list of FieldValues. The FieldValues list must contain a Key and a Value.
        The Key must be a string, of a field name that exists in the content
        type referenced by the ContentTypeID.
        """
        if "ContentTypeId" not in metadata:
            raise ValueError("Content Type ID is a required field")

        if "FieldValues" not in metadata:
            raise ValueError("Field Values is a required field")

        if not isinstance(metadata["FieldValues"], list):
            raise TypeError("Field Values must be a list of objects")

        for field_value in metadata["FieldValues"]:
            if not isinstance(field_value, dict):
                raise TypeError("Field Values must be a list of objects")
            if "Key" not in field_value:
                raise ValueError("Key is a required field in Field Values")
            if "Value" not in field_value:
                raise ValueError("Value is a required field in Field Values")

        return API.post(
            endpoint=f"{Folder.base_path}/{self.id}/Metadata", json=metadata
        )

    def get_metadata(self) -> dict[str, PrimitiveJSONType]:
        """
        Gets the Index Data associated with a batch folder.
        """
        response: JSONType = API.get(endpoint=f"{Folder.base_path}/{self.id}/Metadata")

        if not isinstance(response, dict):
            raise GrooperError("Error retrieving metadata.")

        data: dict[str, PrimitiveJSONType] = {
            to_snake_case(name=key): value for key, value in response.items()
        }
        return data

    def create_document(
        self, file: bytes, filename: str, mime_type: Optional[str] = None
    ) -> JSONType:
        """
        Creates a document (a batch folder with an attached file). Requires a
        local file to stream, and a filename for the Grooper file attachment.
        If the file extension does not match the desire MIMe type, you may
        optionally set the MIME type manually.
        """
        endpoint: str = f"{Folder.base_path}/{self.id}/CreateDocument/{filename}"

        response: JSONType = API.post(
            endpoint=endpoint,
            data=file,
            params={"MimeType": mime_type} if mime_type else {},
        )

        return response

    def set_attachment(
        self, file: bytes, filename: str, mime_type: Optional[str] = None
    ) -> bool:
        """
        Sets the attachment file on a folder object. Requires a local file to
        stream and a filename for the Grooper file attachment. If the file
        extension does not match desired MIME type, you may optionally set the
        MIME type manually.
        """
        endpoint: str = f"{Folder.base_path}/{self.id}/{filename}"

        response: JSONType = API.post(
            endpoint=endpoint,
            data=file,
            params={"MimeType": mime_type} if mime_type else {},
        )

        if not isinstance(response, bool):
            raise GrooperError("Error setting attachment.")

        return response is True


class File(Node):
    """
    Class for interacting with files.
    """

    base_path: str = f"{API.base_path}/Files"

    @staticmethod
    def find(item_id: str, filename: str) -> bytes:
        """
        Retrieves the file attached to a batch folder. Requires an item ID
        (folder or page) and filename.
        """
        endpoint: str = f"{File.base_path}/{item_id}/{filename}"
        response: JSONType = API.get(endpoint=endpoint)
        if not isinstance(response, bytes):
            raise GrooperError("Error retrieving file.")
        return response


class ContentType(Node):
    """
    Class for interacting with content types.
    """

    base_path: str = f"{API.base_path}/ContentTypes"

    def __init__(self, **kwargs) -> None:
        assert "id" in kwargs, "`id` is a required argument"
        assert "name" in kwargs, "`name` is a required argument"
        Node.__init__(
            self=self,
            id=kwargs.get("id"),  # type: ignore
            name=kwargs.get("name"),  # type: ignore
            node_index=kwargs.get("node_index"),
            num_children=kwargs.get("num_children"),
            parent_id=kwargs.get("parent_id"),
            type_name=kwargs.get("type_name"),
        )
        self.children: list["ContentType"] | None = kwargs.get("children")

    @staticmethod
    def all() -> list["ContentType"]:
        """
        Gets information about all available content types.
        """
        response: JSONType = API.get(endpoint=ContentType.base_path)

        if not isinstance(response, list):
            raise GrooperError("Error retrieving content types.")

        content_types: list["ContentType"] = []
        for content_type in response:
            if not isinstance(content_type, dict):
                raise GrooperError("Error retrieving content types.")
            content_types.append(
                ContentType(
                    **{
                        to_snake_case(name=key): value
                        for key, value in content_type.items()
                    }
                )
            )

        return content_types
