"""StakeHolders pydantic BaseModel."""
import logging
from typing import Optional
from urllib.parse import urljoin

from pydantic import BaseModel, validator

from regscale.core.app.api import Api
from regscale.core.app.application import Application

logger = logging.getLogger("rich")


class StakeHolder(BaseModel):
    id: Optional[int] = 0
    name: Optional[str] = ""
    shortname: Optional[str] = ""
    title: Optional[str] = ""
    phone: Optional[str] = ""
    email: Optional[str] = ""
    address: Optional[str] = ""
    otherID: Optional[str] = ""
    notes: Optional[str] = ""
    parentId: int  # Required
    parentModule: str  # Required

    @classmethod
    @validator("email", pre=True, always=True)
    def convert_email_none_to_empty_str(cls, value) -> str:
        """
        Convert a none email to an empty string

        :param value: The email value
        :return: The email value or an empty string
        :rtype: str
        """
        return value if value is not None else ""

    @classmethod
    @validator("shortname", pre=True, always=True)
    def convert_shortname_none_to_empty_str(cls, value) -> str:
        """
        Convert a none shortname to an empty string

        :param value: The shortname value
        :return: The shortname value or an empty string
        :rtype: str
        """
        return value if value is not None else ""

    @classmethod
    @validator("notes", pre=True, always=True)
    def convert_notes_none_to_empty_str(cls, value) -> str:
        """
        Convert a none notes to an empty string

        :param value: The notes value
        :return: The notes value or an empty string
        :rtype: str
        """
        return value if value is not None else ""

    @staticmethod
    def from_dict(data: dict) -> "StakeHolder":
        """Convert dict to StakeHolders object

        :param dict data: dict to create object from
        :return: A StakeHolders object
        :rtype: StakeHolder
        """
        return StakeHolder(**data)

    def post(self, app: Application) -> Optional[dict]:
        """
        Post a StakeHolders to RegScale

        :param Application app: The application instance
        :return: The response from the API or None
        :rtype: dict or None
        """
        api = Api(app)
        url = urljoin(app.config.get("domain"), "/api/stakeholders")
        data = self.dict()
        response = api.post(url, json=data)
        return response.json() if response.ok else None

    @staticmethod
    def get_all_by_parent(
        app: Application, parent_module: str, parent_id: int
    ) -> Optional[list[dict]]:
        """
        Get all stakeholders in parentModule with parentId

        :param Application app: The application instance
        :param str parent_module: The parentModule
        :param int parent_id: The parentId
        :return: A list of StakeHolders objects
        :rtype: list[StakeHolders]
        """
        api = Api(app)
        url = urljoin(
            app.config.get("domain"),
            f"/api/stakeholders/getAllByParent/{parent_id}/{parent_module}",
        )
        response = api.get(url)
        return [StakeHolder(**_) for _ in response.json()] if response.ok else None
