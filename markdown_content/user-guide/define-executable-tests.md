# Define Executable Tests

## Overview

The Define Executable Tests feature in Eclipse Free BIRD Tools allows you to create, configure, and run automated tests for your regulatory data processing workflows. This functionality helps ensure data accuracy, validate business rules, and verify that your regulatory reports meet compliance requirements across different scenarios.

## Purpose

Testing in regulatory environments is critical for:
- **Data Validation**: Ensure calculations produce expected results
- **Scenario Testing**: Test different business scenarios (loans, guarantees, etc.)

## Getting Started

### Prerequisites
Before defining executable tests, ensure:
- Your Eclipse Free BIRD Tools environment is properly configured
- Data cubes and regulatory templates are set up
- You have completed the initial workflow setup steps

### Accessing Test Features

From the FreeBIRD Application homepage, you have access to test-related features:

![FreeBIRD Homepage](images/screenshots/homepage/homepage.png)

- **Task Workflow Dashboard**: Access the main workflow for test execution

## Step-by-Step Guide

### Understanding Test Scenarios

Eclipse Free BIRD Tools supports customizable test scenarios for various business cases.

### Creating a Test Definition

**Step 1: Choose Your Test Parameters**

When defining a test, you need to specify:
- **Regulatory Template ID**: The template you want to test (e.g., `F_05_01_REF_FINREP_3_0`)
- **Datapoint Value**: Expected result value for validation
- **Scenario Name**: Descriptive name for your test case
- **Cell Reference**: Specific cell or datapoint identifier

**Step 2: Configure Test Scenarios**

For different business scenarios, you can create specialized tests:

**Example: Loan Scenario Test**
- Template: `F_05_01_REF_FINREP_3_0`
- Scenario: `loan_and_guarantee_scenario_2`
- Expected Value: Custom value based on your data
- Cell Reference: `152457_REF`
- define a sql insert fixture at `birds_nest/tests/fixtures/templates/F_05_01_REF_FINREP_3_0/152457_REF/loan_and_guarantee_scenario_2/sql_inserts.sql`. This allows the database to have the data necessary for the calculation

**Example: Base Scenario Test**
- Template: `F_05_01_REF_FINREP_3_0`
- Scenario: `base`
- Expected Value: Standard calculation result
- Cell Reference: `152589_REF`
- define a sql insert fixture at `birds_nest/tests/fixtures/templates/F_05_01_REF_FINREP_3_0/152589_REF/base/sql_inserts.sql`. This allows the database to have the data necessary for the calculation

After all this information has been defined, you can run the pybirdai/utils/datapoint_test_ruin/generator_for_tests.py to generate the test cases and pybirdai/utils/datapoint_test_ruin/generator_delete_fixtures.py to generate the cleanup fixtures for after the test.

The generated tests will look like this

```python

# Imports for the well function of the application.
import os
import logging
os.environ['DJANGO_SETTINGS_MODULE'] = 'birds_nest.settings'
from django.conf import settings
import pytest
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Imports to run the testing application
from pybirdai.entry_points.execute_datapoint import RunExecuteDataPoint
from pybirdai.process_steps.pybird.execute_datapoint import ExecuteDataPoint

# Imports of the template cell which is getting tested
from pybirdai.process_steps.filter_code.report_cells import Cell_F_05_01_REF_FINREP_3_0_152457_REF

# function to test the actual datapoint
def test_execute_datapoint(value: int=83491250):
    data_point_id = 'F_05_01_REF_FINREP_3_0_152457_REF'
    result = RunExecuteDataPoint.run_execute_data_point(data_point_id)
    ExecuteDataPoint.delete_lineage_data()
    assert result == str(value)
```

### Running Tests

Normally the tests are all preconfigured in the json : tests/configuration_file_tests.json

in case your custom test is not yet added, please add the information of your test following the underlying template

```json
    {
      "reg_tid": "F_05_01_REF_FINREP_3_0", template id in the reference SMCube terminology
      "dp_suffix": "152457_REF", template cell id in the reference SMCube terminology
      "dp_value": 83491250, result of the test
      "scenario": "loan_and_guarantee_scenario_2", name of the scenario
    }
```

**Execute Your Test**
Once your test is defined and as above configured, the system will:
1. Process the specified datapoint
2. Execute calculations using your data
3. Compare results with expected values
4. Generate detailed test reports available and shareable

### Viewing Test Results

**Accessing Test Reports**
1. Click **Browse Test Reports** from the homepage
2. Navigate to your specific test results
3. Review detailed execution logs

**Understanding Results**

Test results include:
- **Pass/Fail Status**: Whether the test met expectations
- **Execution Details**: Step-by-step processing information
- **Data Lineage**: What data was used in calculations
- **Error Messages**: Any issues encountered during execution

**Example Test Output:**
```
Test: test_execute_datapoint
Status: FAILED
Expected: 11
Actual: 0
Execution Time: 1.92s
```

### Managing Multiple Test Scenarios

**Organizing Tests**
- Use descriptive scenario names
- Group related tests together
- Document expected outcomes for each scenario

**Best Practices**
- **Start Simple**: Begin with basic scenarios before complex ones
- **Test Incrementally**: Add one scenario at a time
- **Document Assumptions**: Record why you expect certain values
- **Regular Validation**: Run tests after data updates

### Next Steps

After setting up your tests:
- Review the [Create Pull Request Guide](create-pull-request-guide.html) for detailed explanations, how to participate to the efbt community by sharing your tests configurations

For additional support with test definition or troubleshooting complex scenarios, connect with the community via [Eclipse Chat](https://chat.eclipse.org/#/room/%23technology.efbt:matrix.eclipse.org) or email [efbt-dev@eclipse.org](mailto:efbt-dev@eclipse.org).
