The Eclipse Free BIRD Tools Workflow Dashboard is your central hub for regulatory reporting workflows. This guide explains how to execute the 4-task sequential process for BIRD data processing.

## Access the Dashboard

To access the dashboard, launch the FreeBIRD Application, navigate to the Home page, and click on **"Task Workflow Dashboard"**.

![Homepage](images/screenshots/homepage/homepage_click_on_task_workflow_dashboard.png)

## Configuration Setup

Before starting any tasks, you must configure your workflow settings.

![Configuration Menu](images/screenshots/configuration/configurationmenu_click_on_save.png)

Start by selecting "EIL (Input Layer)" as your data model type. Enter your GitHub repository URL and specify the branch you want to use, which defaults to "main" if not specified. Set both the configuration files source and technical export source to "GitHub Repository". After entering all settings, click the save button to store your configuration.

## Quick Actions Panel

![Quick Actions Menu](images/screenshots/quickaction/quickactionmenu_setup_not_started_click_on_retrieve_artifacts.png)

The Quick Actions panel provides several important functions. Use **Retrieve Artifacts** to download configuration files from your GitHub repository. The **Setup Database** button initializes your database environment. You can select any task from 1 to 4 as your target endpoint and then use **Run Automode** to automatically execute from Task 1 up to your selected target. The panel also displays your current database and configuration status, along with a session ID for tracking. If you need to start over, use **Reset Tasks 1-4** to clear task history while keeping your configuration, or **Reset Everything** for a complete reset.

## 4-Task Sequential Workflow

The workflow consists of four sequential tasks that must be executed in order.

![Task Dashboard](images/screenshots/workflow_dashboard/taskdashboard.png)

### Task 1: SMCubes Core Creation

This task creates foundational data structures and cube definitions.

![Task 1 Review](images/screenshots/dataset/step1_do.png)

To execute Task 1, click the **"Do"** button to start the execution. The system will then clear the database by running "Delete Database", create cube structures through "Import Input Model", generate report templates, import LDM/EIL hierarchies, and process semantic integrations. Alternatively, you can use the Quick Actions panel by selecting "Task 1" as your target and clicking "Run Automode" for automatic execution. After completion, click **"Review"** to verify that over 50 cubes and 100 templates have been created.

![Task 1 Review](images/screenshots/dataset/step1_review_part1.png)

### Task 2: SMCubes Transformation Rules Creation

This task generates transformation rules and metadata for your data processing.

![Task 2 Do](images/screenshots/dataset/step2_do.png)

Start Task 2 by clicking the **"Do"** button. The system will generate filters and create join metadata for your transformations. You can also use Quick Actions by selecting "Task 2" as your target and running automode, which will execute both Task 1 and Task 2 automatically. Review the results to confirm that filter and join metadata creation has completed successfully.

![Task 2 Review](images/screenshots/dataset/step2_review.png)

### Task 3: Python Transformation Rules Creation

This task converts your transformation rules into executable Python code.

![Task 3 Do](images/screenshots/dataset/step3_do.png)

Click the **"Do"** button to begin Task 3. The system will generate filter code and join code based on the metadata created in Task 2. For automated execution, select "Task 3" in Quick Actions and run automode to execute Tasks 1 through 3 sequentially. Verify that the executable Python transformation code has been generated successfully.

### Task 4: Full Execution with Test Suite

This final task validates your regulatory templates with comprehensive testing.

![Task 4 Do](images/screenshots/dataset/step4_do.png)

Start Task 4 by clicking the **"Do"** button, then run the configuration file tests. Alternatively, select "Task 4: Full Execution" in Quick Actions and run automode to execute the complete workflow from Task 1 through Task 4 automatically. Review the test execution reports to check pass/fail statistics and ensure all validations have completed successfully.

![Task 4 Review - Part 1](images/screenshots/dataset/step4_review_part1.png)
![Task 4 Review - Part 2](images/screenshots/dataset/step4_review_part2.png)
![Task 4 Review - Part 3](images/screenshots/dataset/step4_review_part3.png)

## Best Practices

Always execute tasks in sequential order from Task 1 through Task 4. Complete each task before proceeding to the next and use the Review function to validate completion. Save your configuration before starting any workflow execution and verify that your GitHub credentials are valid and current. Check that the system status shows "Ready" and "Configured" before beginning execution.

## Troubleshooting

If tasks fail to execute, verify your database connectivity and status, check your GitHub repository access permissions, and confirm that your configuration has been saved properly. For configuration issues, make sure to click "Save Configuration" after any changes, verify that repository URLs are correct, and check that your GitHub token has the necessary permissions. If you encounter database problems, use the "Setup Database" option in Quick Actions, verify that the database service is running, and check your connection parameters.
