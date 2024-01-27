"""Shared test resource manager
"""

from silx.resources import ExternalResources


test_resources = ExternalResources(
    project="xsocs",
    url_base="http://www.silx.org/pub/xsocs/test_data",
    env_key="XSOCS_DATA",
)
"""Shared test resources manager"""
