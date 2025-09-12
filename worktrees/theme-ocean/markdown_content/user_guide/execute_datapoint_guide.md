The Execute Datapoint feature enables you to run calculations and transformations on populated template cells within the FreeBIRD application for regulatory reporting.

## Overview

Execute Datapoint functionality allows you to view and manage populated templates, execute calculations on template cells, generate transformed data for regulatory reporting, and track execution status and results.

## Accessing Execute Datapoint

To access the Execute Datapoint functionality, navigate to the FreeBIRD application homepage and click on **"View Populated Templates"**.

![Homepage - Click on View Populated Templates](images/screenshots/execute_datapoints/homepage_click_on_view_populated_templates.png)

After clicking, you'll see a list of all populated templates available in the system. Each template represents a collection of data cells ready for execution.

![List of Populated Templates](images/screenshots/execute_datapoints/list_of_populated_templates.png)

## Working with Populated Templates

The populated templates list displays the template name which identifies the specific regulatory template, the current status showing whether it's populated, executed, or pending, when the template was last modified, and the number of cells within the template.

Click on any template to view its individual cells. Each cell contains specific datapoints that can be executed.

![List of Populated Template Cells](images/screenshots/execute_datapoints/list_of_populated_template_cells.png)

Each cell shows a unique cell reference like R010C010, the specific datapoint to be calculated, the current or calculated value, the execution status indicating if it's pending, completed, or has an error, and the underlying calculation or transformation formula.

## Executing Datapoints

### Individual Cell Execution

To execute a specific datapoint, select the desired cell from the template cell list, review the cell details and formula, click the **"Execute"** button to run the calculation, and monitor the execution progress.

![Populated Template Cell Execution](images/screenshots/execute_datapoints/populated_template_cell_execution.png)

### Batch Execution

For multiple datapoints, select multiple cells using checkboxes, click **"Execute Selected"** to run calculations in batch, and track progress through the execution status panel.

During execution, the system validates input data, applies transformation rules, calculates results based on formulas, updates cell values, and logs execution details for audit purposes.

## Monitoring Execution

Watch for status indicators during execution. A "Pending" status means the datapoint is awaiting execution and you should initiate it when ready. "In Progress" indicates the calculation is currently running and you should wait for completion. "Completed" means the execution was successful and you can review the results. An "Error" status indicates the execution failed and you should check the logs and retry. "Validated" means the results have been verified and are ready for submission.

After successful execution, cell values are updated with calculated results, execution timestamps are recorded, audit trails are maintained, and results become available for export.

## Best Practices

Before execution, ensure your input data is complete by reviewing source data completeness. Verify you've selected the correct regulatory template by checking the template version and requirements. Understand the calculation logic by reviewing the formula documentation. Identify any linked datapoints by checking cell relationships and dependencies.

During execution, monitor system resources when running large batch executions. Execute critical datapoints individually for better control. Keep execution logs for audit purposes and validate intermediate results when possible.

After execution, verify results by cross-checking calculated values against expected outcomes. Review execution logs for any warnings or issues. Export data in the required format for reporting and document any discrepancies for investigation.

## Troubleshooting

If execution fails, it's often due to missing input data, so verify all required data is populated. Incorrect results may be caused by outdated formulas, requiring you to update the template to the latest version. Performance issues with large datasets can be resolved by executing in smaller batches. Access denied errors require contacting your administrator for proper permissions. If a template is not found, ensure you've run the population process first.

Common error messages include "Missing Required Data" when input cells are empty or invalid, "Formula Error" when the calculation formula contains errors, "Timeout Error" when execution exceeds the time limit, and "Validation Failed" when results don't meet validation rules.

## Advanced Features

Use filters to find specific templates or cells quickly. Search by cell reference, datapoint name, or value. Sort results by status, date, or cell reference for better organization. Export your results in various formats including CSV for data analysis, Excel for regulatory submission, JSON for system integration, or XML for XBRL reporting.

All executions maintain a complete audit trail recording who initiated the execution, when it occurred, what input values were used, which formula was applied, what result was generated, and any errors or warnings encountered.

## Integration with Other Features

Execute Datapoint integrates with the Workflow Dashboard where you can track execution tasks, set up automated schedules, and monitor performance metrics. It also works with DPM Operations to link executed datapoints to DPM models, validate against regulatory requirements, and generate compliance reports. The feature connects with Dataset Transformation to use executed results as input for transformations, chain multiple execution processes, and create complex reporting pipelines.

## Compliance Considerations

Ensure all executions comply with ECB regulatory requirements, data quality standards, audit requirements, reporting deadlines, and your organization's data governance policies. Regular validation and proper documentation are essential for maintaining compliance throughout the execution process.
