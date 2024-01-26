#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Snyk RegScale integration"""
from pathlib import Path

import click

from regscale.core.app.application import Application
from regscale.models.integration_models.snyk import Snyk


@click.group()
def snyk():
    """Performs actions on Snyk export files."""


@snyk.command(name="import_snyk")
@click.option(
    "--folder_path",
    help="File path to the folder containing Snyk .xlsx files to process to RegScale.",
    prompt="File path for Snyk files",
    type=click.Path(exists=True, dir_okay=True, resolve_path=True),
)
@click.option(
    "--regscale_ssp_id",
    type=click.INT,
    help="The ID number from RegScale of the System Security Plan.",
    prompt="Enter RegScale System Security Plan ID",
    required=True,
)
def import_snyk(folder_path: click.Path, regscale_ssp_id: click.INT):
    """
    Import scans, vulnerabilities and assets to RegScale from Snyk export files

    """
    app = Application()
    if len(list(Path(folder_path).glob("*.xlsx"))) == 0:
        app.logger.warning("No Snyk files found in the specified folder.")
        return
    for file in Path(folder_path).glob("*.xlsx"):
        Snyk(name="Snyk", app=app, file_path=file, regscale_ssp_id=regscale_ssp_id)
