===================
**terraform_usage**
===================

Overview
--------

A Python module to call the Terraform Cloud API and retrieve data for total and applied Runs of Workspaces.

Usage
-----

Installation:

.. code-block:: BASH

   pip3 install terraform_usage
   # or
   python3 -m pip install terraform_usage

Usage instructions are in the script built-in help document. Run the following to see options and default parameters.

Bash:

.. code-block:: BASH

   python </oath/to>/terraform_usage -h

Python:

.. code-block:: PYTHON

   import terraform_usage as tfu
   help(tfu)

Execution example:

.. code-block:: BASH

   python </path/to>/terraform_usage -o abdahmad -t $TFE_TOKEN -k "*abdahmad-*" -m advanced -f abdahmad.csv -s 2023-11-01 -e 2023-11-30

   Run parameters:
   Organization: abdahmad
   Keyword: *abdahmad-*
   Filename: abdahmad.csv
   Start date: 2023-11-01
   End date: 2023-11-30
   Mode: advanced
   API URL: https://app.terraform.io/api/v2
   Page size: 50
   Delay: 1.0
   -------
   Getting page 1 of Workspaces.
   Found 3 Workspaces.
   Getting Run data for Workspace ids-aws-abdahmad-dev.
   Getting page 1 of Runs.
   Getting Run data for Workspace ids-aws-abdahmad-prod.
   Getting page 1 of Runs.
   Getting Run data for Workspace ids-aws-abdahmad-test.
   Getting page 1 of Runs.
   Creating CSV file abdahmad.csv.
   Writing data to abdahmad.csv.
    
Output in CSV file example:

.. code-block:: TXT

   workspace,all_runs,successful_applies,total_time
   abdahmad-dev,4,0,53
   abdahmad-prod,0,0,0
   abdahmad-test,0,0,0

Execution Modes
---------------

- basic
    - Function
        - Get total number of Runs and successful Applies for all time.
    - Available filters
        - Workspace name pattern
    - Pros and cons
        - Faster execution
        - Less details

- advanced
    - Function
        - Get total number of Runs, successful Applies, and total Run time.
    - Available filters
        - Workspace name pattern
        - Start date
        - End date
    - Pros and cons
        - Potentially slower execution for a large number of Workspaces and Runs.
        - More details

Error Handling
--------------

- Error: Skipping run due to missing attribute(s).
    - A Run is missing a timestamp for a status. Normally caused by Runs stuck in Pending state, which should be discarded if they aren't meant to complete, successfully or otherwise.
- Error: One or more Python exceptions.
    - Multiple possible causes. One of the most common is due to the script hitting the Terraform Cloud API rate limit (30 requests per second). There is a safeguard that slows down execution to avoid this.

API Documentation
-----------------

https://developer.hashicorp.com/terraform/cloud-docs/api-docs
