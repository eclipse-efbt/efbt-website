## Feature Overview

The Eclipse Free BIRD Tools Workflow Dashboard is your central control center for managing and executing regulatory reporting workflows. It provides a streamlined interface for processing BIRD data through a systematic 4-task sequential workflow, enabling efficient regulatory compliance and data transformation.

## Purpose

The Workflow Dashboard serves as the primary orchestration point for your regulatory reporting processes. It eliminates the complexity of manual data processing by providing:
- **Automated Sequential Processing**: Execute complex workflows with a single click
- **Progress Tracking**: Monitor each step of your data transformation journey
- **Configuration Management**: Centralize all workflow settings in one place
- **Error Prevention**: Built-in validation ensures tasks execute in the correct order
- **Quick Actions**: Accelerate common operations with one-click automation

This feature is essential for organizations that need to maintain compliance with European regulatory standards while minimizing manual effort and reducing the risk of processing errors.

## Getting Started

### Prerequisites
Before using the Workflow Dashboard, ensure you have:
- FreeBIRD Application installed and running
- Valid GitHub repository access with appropriate permissions
- Database connectivity established
- Configuration files prepared in your repository

### Accessing the Dashboard

To access the dashboard, launch the FreeBIRD Application, navigate to the Home page, and click on **"Task Workflow Dashboard"**.

![Homepage](images/screenshots/homepage/homepage_click_on_task_workflow_dashboard.png)

## Step-by-Step Guide

### Configuration Setup

Before starting any tasks, you must configure your workflow settings.

![Configuration Menu](images/screenshots/configuration/configurationmenu_click_on_save.png)

Start by selecting "EIL (Input Layer)" as your data model type. Enter your GitHub repository URL and specify the branch you want to use, which defaults to "main" if not specified. Set both the configuration files source and technical export source to "GitHub Repository". After entering all settings, click the save button to store your configuration.

### Quick Actions Panel

![Quick Actions Menu](images/screenshots/quickaction/quickactionmenu_setup_not_started_click_on_retrieve_artifacts.png)

The Quick Actions panel provides several important functions. Use **Retrieve Artifacts** to download configuration files from your GitHub repository. The **Setup Database** button initializes your database environment. You can select any task from 1 to 4 as your target endpoint and then use **Run Automode** to automatically execute from Task 1 up to your selected target. The panel also displays your current database and configuration status, along with a session ID for tracking. If you need to start over, use **Reset Tasks 1-4** to clear task history while keeping your configuration, or **Reset Everything** for a complete reset.

### 4-Task Sequential Workflow

The workflow consists of four sequential tasks that must be executed in order.

![Task Dashboard](images/screenshots/workflow_dashboard/taskdashboard.png)

#### Task 1: SMCubes Core Creation

This task creates foundational data structures and cube definitions.

![Task 1 Review](images/screenshots/dataset/step1_do.png)

To execute Task 1, click the **"Do"** button to start the execution. The system will then clear the database by running "Delete Database", create cube structures through "Import Input Model", generate report templates, import LDM/EIL hierarchies, and process semantic integrations. Alternatively, you can use the Quick Actions panel by selecting "Task 1" as your target and clicking "Run Automode" for automatic execution. After completion, click **"Review"** to verify that over 50 cubes and 100 templates have been created.

![Task 1 Review](images/screenshots/dataset/step1_review_part1.png)

#### Task 2: SMCubes Transformation Rules Creation

This task generates transformation rules and metadata for your data processing.

![Task 2 Do](images/screenshots/dataset/step2_do.png)

Start Task 2 by clicking the **"Do"** button. The system will generate filters and create join metadata for your transformations. You can also use Quick Actions by selecting "Task 2" as your target and running automode, which will execute both Task 1 and Task 2 automatically. Review the results to confirm that filter and join metadata creation has completed successfully.

![Task 2 Review](images/screenshots/dataset/step2_review.png)

#### Task 3: Python Transformation Rules Creation

This task converts your transformation rules into executable Python code.

![Task 3 Do](images/screenshots/dataset/step3_do.png)

Click the **"Do"** button to begin Task 3. The system will generate filter code and join code based on the metadata created in Task 2. For automated execution, select "Task 3" in Quick Actions and run automode to execute Tasks 1 through 3 sequentially. Verify that the executable Python transformation code has been generated successfully.

#### Task 4: Full Execution with Test Suite

This final task validates your regulatory templates with comprehensive testing.

![Task 4 Do](images/screenshots/dataset/step4_do.png)

Start Task 4 by clicking the **"Do"** button, then run the configuration file tests. Alternatively, select "Task 4: Full Execution" in Quick Actions and run automode to execute the complete workflow from Task 1 through Task 4 automatically. Review the test execution reports to check pass/fail statistics and ensure all validations have completed successfully.

![Task 4 Review - Part 1](images/screenshots/dataset/step4_review_part1.png)
![Task 4 Review - Part 2](images/screenshots/dataset/step4_review_part2.png)
![Task 4 Review - Part 3](images/screenshots/dataset/step4_review_part3.png)

## Best Practices

Always execute tasks in sequential order from Task 1 through Task 4. Complete each task before proceeding to the next and use the Review function to validate completion. Save your configuration before starting any workflow execution and verify that your GitHub credentials are valid and current. Check that the system status shows "Ready" and "Configured" before beginning execution.

## Troubleshooting

### Common Issues and Solutions

**Task Execution Failures:**
- Verify your database connectivity and status
- Check your GitHub repository access permissions
- Confirm that your configuration has been saved properly
- Ensure tasks are executed in sequential order

**Configuration Problems:**
- Always click "Save Configuration" after making changes
- Verify that repository URLs are correctly formatted
- Check that your GitHub token has the necessary permissions
- Confirm branch names are valid and accessible

**Database Issues:**
- Use the "Setup Database" option in Quick Actions to reinitialize
- Verify that the database service is running
- Check your connection parameters
- Clear database and restart if corruption is suspected

**Quick Actions Not Responding:**
- Ensure all prerequisites are met
- Check system status indicators
- Verify network connectivity to GitHub
- Try using "Reset Tasks 1-4" to clear task history

## Conclusion

The Workflow Dashboard streamlines your regulatory reporting process by providing a unified interface for executing complex data transformations. By following the 4-task sequential workflow, you can efficiently process BIRD data while maintaining compliance with regulatory standards.

### Next Steps
- Explore the [DPM Operations Guide](dpm-operations-guide.html) for alternative workflows
- Learn about [Pull Request Creation](pull-request-creation-guide.html) to submit your processed data
- Review the [Execute Datapoint Guide](execute-datapoint-guide.html) for advanced execution options

For additional support, contact the Eclipse Free BIRD Tools community through our [Eclipse Chat](https://chat.eclipse.org/#/room/%23technology.efbt:matrix.eclipse.org) or email us at [efbt-dev@eclipse.org](mailto:efbt-dev@eclipse.org).