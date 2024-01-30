#!/usr/bin/env python3
# -*- coding: latin-1 -*-

"""
Get Terraform Workspace and Run usage statistics.

Call the Terraform Cloud API to retrieve Workspace and Run data.
Visualization functions are available, but not recommended.
Better to use the CSV output and plot the charts / tables elsewhere.

USAGE

Command line:
python </path/to>/terraform_usage -o <organization> -t <token> -k <keyword> -f <filename> -s <start_date> -e <end_date> -m <mode> -u <api_url> -p <page_size> -d <delay>

Python shell:
import terraform_usage as tfu
workspaces = tfu.list_workspaces(
    <organization>,
    <token>,
    <keyword>,
    <api_url>,
    <page_size>,
    <delay>
)
runs = tfu.analyze_runs(
    workspaces,
    <token>,
    <start_date>,
    <end_date>,
    <mode>,
    <api_url>,
    <page_size>,
    <delay>
)
create_csv(
    [run.values() for run in runs],
    <filename>,
    <mode>
)

Arguments:
<organization> - Terraform Cloud Organization name. Required.
<token> - Terraform Cloud API token. Required.
<keyword> - Workspace name keyword to filter by. Default is "all".
<filename> - CSV filename to save the output data to. Default is "report.csv".
<start_date> - Start date for Run lookups. Default is "all".
<end_date> - End date for Run lookups. Default is "all".
<mode> - Execution mode ("basic" or "advanced"). Default is "basic".
<api_url> - Terraform Cloud API URL. Default is "https://app.terraform.io/api/v2".
<page_size> - Number of items per page. Default is 50.
<delay> - Delay (in seconds) between API calls. Default is 1.0.

Dependencies:
requests - https://pypi.org/project/requests/
matplotlib - https://pypi.org/project/matplotlib/

API documentation:
https://developer.hashicorp.com/terraform/cloud-docs/api-docs

CAUTION
This may take a while to run if the Organization
has a large number of Workspaces and / or Runs.
"""
import __init__

if __name__ == "__main__":
    __init__.main()
