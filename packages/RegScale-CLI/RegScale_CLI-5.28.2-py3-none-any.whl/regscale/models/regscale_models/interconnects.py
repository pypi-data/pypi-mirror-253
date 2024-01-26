#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" [Deprecated] Model for Interconnects in the application """

import warnings
from .interconnect import (
    Interconnect as Interconnects,
)  # Import everything from the new module

# Issue a deprecation warning
warnings.warn(
    "The module 'interconnects' is deprecated and will be removed in future versions. "
    "Use 'interconnect' instead.",
    DeprecationWarning,
    stacklevel=2,
)
