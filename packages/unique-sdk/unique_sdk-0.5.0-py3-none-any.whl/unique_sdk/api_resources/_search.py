from typing import ClassVar, List, Literal, cast

from typing_extensions import NotRequired, Unpack

from unique_sdk._api_resource import APIResource
from unique_sdk._request_options import RequestOptions


class Search(APIResource["Search"]):
    OBJECT_NAME: ClassVar[Literal["search.search"]] = "search.search"

    class CreateParams(RequestOptions):
        chatId: str
        searchString: str
        searchType: Literal["VECTOR", "COMBINED"]
        scopeIds: NotRequired[List[str]]
        chatOnly: NotRequired[bool]

    text: str
    createdAt: str
    updatedAt: str

    @classmethod
    def create(
        cls, user_id: str, company_id: str, **params: Unpack["Search.CreateParams"]
    ) -> "Search":
        return cast(
            "Search",
            cls._static_request(
                "post",
                "/search/search",
                user_id,
                company_id,
                params=params,
            ),
        )
