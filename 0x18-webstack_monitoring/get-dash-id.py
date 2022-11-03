#!/usr/bin/python3
"""
Get all dashboards returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.list_dashboards(
        filter_shared=False,
    )

    print(response)


# DD_SITE="datadoghq.com" DD_API_KEY="e8c8ce9f907a0b9fef2a6fbbc6be0cde" DD_APP_KEY="e29d7ad76f8249b9f6bea0a134aae8f42047ebd9" python3 "get-dash-id.py"