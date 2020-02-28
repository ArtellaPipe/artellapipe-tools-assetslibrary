#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to easily import and reference assets file into DCC scene
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-assetslibrary'

# We skip the reloading of this module when launching the tool
no_reload = True


class AssetsLibraryTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(AssetsLibraryTool, self).__init__(*args, **kwargs)


class AssetsLibraryToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(AssetsLibraryToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from artellapipe.tools.assetslibrary.widgets import assetslibrary

        assets_library = assetslibrary.ArtellaAssetsLibrary(project=self._project, config=self._config)
        return [assets_library]
