#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Model for Catalog in the application"""

from typing import Optional, List, Union
from urllib.parse import urljoin

from pydantic import ConfigDict

from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.utils.api_handler import APIInsertionError, APIRetrieveError
from .regscale_model import RegScaleModel


class Catalog(RegScaleModel):
    """Catalog class"""

    _model_slug = "catalogues"

    id: Optional[int] = 0
    abstract: Optional[str] = None
    datePublished: Optional[str] = None
    description: Optional[str] = None
    keywords: Optional[str] = None
    lastRevisionDate: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    tenantsId: Optional[int] = None
    uuid: Optional[str] = None
    createdById: Optional[str] = None
    dateCreated: Optional[str] = None
    dateLastUpdated: Optional[str] = None
    lastUpdatedById: Optional[str] = None
    master: Optional[bool] = False
    sourceOscalURL: Optional[str] = None
    archived: Optional[bool] = False
    isPublic: Optional[bool] = True

    @staticmethod
    def _get_additional_endpoints() -> ConfigDict:
        """
        Get additional endpoints for the Catalogues model

        :return: A dictionary of additional endpoints
        :rtype: ConfigDict
        """
        return ConfigDict(
            get_count="/api/{model_slug}/getCount",
            get_list="/api/{model_slug}/getList",
            get_catalog_with_all_details="/api/{model_slug}/getCatalogWithAllDetails/{intID}",
            filter_catalogues="/api/{model_slug}/filterCatalogues",
            graph="/api/{model_slug}/graph",
            convert_mappings="/api/{model_slug}/convertMappings/{intID}",
            find_by_guid="/api/{model_slug}/findByGUID/{strID}",
            get_titles="/api/{model_slug}/getTitles",
            get_nist="/api/{model_slug}/getNIST",
        )

    @classmethod
    def get_list(cls) -> Union[List[dict], List]:
        """
        Retrieves basic data for the catalog list

        :return: The response from the API or None
        :rtype: List[dict]
        """
        endpoint = cls.get_endpoint("get_list").format(model_slug=cls._model_slug)
        response = cls._model_api_handler.get(endpoint)

        if response and response.ok and response.status_code not in [204, 404]:
            return response.json()
        return []

    def insert_catalog(self, app: Application) -> "Catalog":
        """
        Insert catalog into database

        :param Application app: Application
        :raises APIInsertionError: API request failed
        :return: Catalog
        :rtype: Catalog
        """
        # Convert the model to a dictionary
        api = Api(app)
        data = self.dict()
        api_url = urljoin(app.config["domain"], "/api/catalogues")
        # Make the API call
        response = api.post(api_url, json=data)

        # Check the response
        if not response.ok:
            api.logger.debug(
                f"API request failed with status: {response.status_code}: {response.reason} {response.text}"
            )
            raise APIInsertionError(
                f"API request failed with status {response.status_code}"
            )

        return self.from_dict(response.json())

    @staticmethod
    def get_catalogs(app: Application) -> list:
        """
        Get all catalogs from database

        :param Application app: Application
        :raises APIRetrieveError: API request failed
        :return: list of catalogs
        :rtype: list
        """
        api = Api(app)
        api_url = urljoin(app.config["domain"], "/api/catalogues")
        response = api.get(api_url)
        if not response.ok:
            api.logger.debug(
                f"API request failed with status: {response.status_code}: {response.reason} {response.text}"
            )
            raise APIRetrieveError(
                f"API request failed with status {response.status_code}"
            )
        return response.json()

    @staticmethod
    def from_dict(obj: dict) -> "Catalog":
        """
        Create Catalog object from dict

        :param dict obj: dictionary
        :return: Catalog class
        :rtype: Catalog
        """
        return Catalog(**obj)

    @classmethod
    def get_with_all_details(cls, catalog_id: int) -> Optional[list]:
        """
        Retrieves a catalog with all details by its ID.

        :param catalog_id: The ID of the catalog
        :return: The response from the API or None
        :rtype: Optional[list]
        """
        endpoint = cls.get_endpoint("get_catalog_with_all_details").format(
            model_slug=cls._model_slug, intID=catalog_id
        )
        response = cls._model_api_handler.get(endpoint)

        if response and response.ok and response.status_code not in [204, 404]:
            return response.json()
        return None
