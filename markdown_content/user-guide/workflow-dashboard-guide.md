# PyBIRD AI Workflows - User Guide

## What are Workflows?

PyBIRD AI provides three specialized workflows for processing banking regulatory data, each designed for different reporting requirements. All workflows use a consistent dashboard interface with sequential steps and built-in review capabilities.

## Understanding the Workflow Dashboard

All workflows in PyBIRD AI share a common dashboard interface structure:

**Dashboard Layout:**
- **Step Column:** Lists all workflow steps in sequential order
- **Do Column:** Contains "Do" or "Execute" buttons to run each step
- **Review Column:** Contains "Review" buttons to view results and access editors

**How It Works:**
1. Execute steps sequentially using the "Do" buttons
2. Review results and make adjustments using "Review" buttons
3. Each step depends on successful completion of previous steps
4. Progress is tracked automatically within each workflow

This consistent interface makes it easy to switch between different workflows while maintaining familiar navigation patterns.

---

## Choose Your Workflow

### Main Workflow - FINREP Reporting

**Use for:** Standard financial regulatory reports (FINREP/DPM) based on ECB Financial Reporting Framework

**Purpose:**
The Main Workflow processes BIRD data through a systematic 4-task sequence, creating foundational data structures, transformation rules, and executable code for regulatory compliance. It focuses on the EIL (European Input Layer) and provides automated execution options for efficiency.

**4-Task Sequential Process:**

1. **Task 1: SMCubes Core Creation**
   - Creates foundational data structures and cube definitions
   - Imports input model and generates report templates
   - Processes LDM/EIL hierarchies and semantic integrations
   - Output: 50+ cubes and 100+ templates

2. **Task 2: SMCubes Transformation Rules Creation**
   - Generates transformation rules and metadata
   - Creates filters and join metadata
   - Prepares data processing specifications

3. **Task 3: Python Transformation Rules Creation**
   - Converts transformation rules into executable Python code
   - Generates filter code and join code
   - Creates production-ready transformation scripts

4. **Task 4: Full Execution with Test Suite**
   - Validates regulatory templates with comprehensive testing
   - Runs configuration file tests
   - Provides pass/fail statistics and validation reports

**Key Features:**
- **Configuration Setup:** Centralized settings for GitHub repository, data model type (EIL), and sources
- **Quick Actions Panel:**
  - Retrieve Artifacts from GitHub
  - Setup Database initialization
  - Run Automode for automated multi-task execution
  - Reset options for tasks or complete workflow
- **Automated Execution:** Select target task and run automode to execute all tasks up to that point
- **Progress Tracking:** Database and configuration status displayed in dashboard
- **Session Management:** Track workflows with unique session IDs

**Access:** Navigate to **Workflows** > **Main Workflow** or visit `/pybirdai/workflow/`

**Prerequisites:**
- Valid GitHub repository access with permissions
- Configuration files prepared in repository
- Database connectivity established

**Best For:** Organizations processing standard FINREP regulatory reports requiring compliance with European regulatory standards.

---

### Dataset Transformation (ANCRDT) Workflow

**Use for:** Dataset submissions to ECB, including AnaCredit (Analytical Credit Datasets) - loan-level credit data reporting

**Note:** This workflow is also labeled "DATASET TRANSFORMATION (ANACREDIT)" in the interface. Dataset and ANCRDT refer to the same workflow with different names.

**Purpose:**
The Dataset Transformation Workflow automates the processing of ECB Dataset specifications, from fetching the latest metadata to generating and executing production-ready transformations. It provides comprehensive editing capabilities for metadata and code, with built-in deployment management.

**5-Step Sequential Process:**

0. **Step 0: Fetch Metadata CSV**
   - Downloads latest Dataset specifications directly from ECB repository
   - Retrieves authoritative regulatory requirements
   - Saves metadata locally for processing
   - Requires internet connection

1. **Step 1: Import Metadata**
   - Processes CSV files and builds local Dataset data model
   - Creates database structures (cubes, cube structures, variables)
   - Imports all Dataset specifications into database
   - Review page displays import statistics

2. **Step 2: Generate Joins Metadata**
   - Analyzes data model and generates join specifications
   - Creates cube links, structure item links, and member links
   - Auto-generates relationships based on ECB specifications
   - **Embedded Editors Available:**
     - Edit Cube Links (table-to-table relationships)
     - Edit Cube Structure Item Links (variable-to-variable joins)
     - Edit Member Links (dimension value mappings)
     - View Diagram (interactive network visualization)

3. **Step 3: Generate Execution Code**
   - Transforms join metadata into production-ready Python code
   - Generates optimized scripts with error handling and logging
   - **Code Editing Features:**
     - Individual Code Editor (Monaco editor with syntax highlighting)
     - Unified Filter Code Editor (multi-file editing with auto-save)
     - Deployment Status tracking (synced/not synced)
     - Code validation and syntax checking
   - **Deployment System:**
     - Deploy individual files or all files at once
     - Backup management for production files
     - Manual edit tracking
     - Files staged in `results/generated_python_joins/`
     - Production location: `pybirdai/process_steps/filter_code/`

4. **Step 4: Execute Tables**
   - Executes Dataset table transformations with deployed code
   - **Table Selection:** Choose from implemented Dataset tables
   - **Dimension Filters:** Apply optional filters for targeted processing
   - **Filter Interface:** Grid layout with searchable dropdowns for each dimension
   - **Execution Options:** Single table, batch execution, or scheduled execution
   - **Results:** View statistics, data preview, download CSV/Excel
   - **Comparison Mode:** Compare executions with different filter sets

**Key Features:**
- **ECB Metadata Integration:** Direct fetch from ECB website
- **Comprehensive Editors:** Cube links, structure items, member mappings, and code
- **Code Deployment Management:** Track sync status, deploy selectively, maintain backups
- **Advanced Execution:** Dimension filtering, batch processing, scheduling
- **Data Quality:** Built-in validation and comparison tools

**Access:** Navigate to **Workflows** > **Dataset Workflow** or visit `/pybirdai/dataset-workflow/`

**Prerequisites:**
- Internet connection for Step 0 (ECB metadata fetch)
- Database setup completed
- Python environment verified

**Best For:** Financial institutions required to submit Dataset or AnaCredit reports to the ECB, needing automated compliance and operational efficiency.

---

### DPM Workflow - Custom Output Layers

**Use for:** Creating specialized DPM (Data Point Model) output layer structures and combinations

**Purpose:**
The DPM Workflow imports the latest DPM database and formats it to the application's metadata format. It enables semantic integration between multiple regulatory frameworks and provides an interactive way to design mappings.

**3-Step Sequential Process:**

1. **Step 1: Prepare DPM Data**
   - Prepares DPM data for import
   - Formats data for metadata structure

2. **Step 2: Import DPM Data**
   - Imports formatted DPM data into database
   - Creates DPM metadata structures

3. **Step 3: Create Output Layers**
   - Generates output layer structures
   - Redirects to Output Layer Mapping subworkflow
   - Enables interactive mapping design

**Key Features:**

The DPM Workflow offers several key features that enhance its flexibility and power. Integration with Main Workflow allows it to run as either a standalone process or integrated with the main workflow. The Complete Workflow Option provides a "Run Complete DPM Workflow" button that executes all steps including Main Workflow Step 1 automatically. Automated Execution gives you the choice to run the full workflow in one go or progress through it step-by-step. Subworkflow Access leads you directly to the Output Layer Mapping Subworkflow after Step 3 completion. Semantic Integration capabilities allow you to integrate between multiple regulatory frameworks seamlessly.

**Access:** Through main workflow dashboard

**Prerequisites:**

Before starting the DPM Workflow, ensure your instance is configured with the appropriate model type (either EIL or ELDM), your repository and mandatory parameters are properly configured, you've run the fetch artifacts command, the setup database command has been executed, and optionally, you've completed Main Workflow Step 1 if you need reference artifacts loaded.

**Outcome:**
After completion, you'll have a full import of the latest DPM database in the application's metadata format, enabling diverse subsequent operations and semantic integration.

**Best For:** Organizations needing custom DPM output structures or specialized mapping designs beyond standard regulatory templates.

---

## Quick Workflow Comparison

| Feature | Main Workflow | Dataset Transformation | DPM Workflow |
|---------|--------------|------------------------|--------------|
| **Purpose** | FINREP/Financial reporting | Dataset/AnaCredit submissions | Custom DPM structures |
| **Data Source** | SQLDev files, GitHub | ECB CSV metadata | DPM database |
| **Steps** | 4 tasks | 5 steps (0-4) | 3 steps |
| **Numbering** | Tasks 1-4 | Steps 0-4 | Steps 1-3 |
| **Configuration** | Required (GitHub, EIL) | Optional (filters) | Required (model type) |
| **Metadata Editing** | Basic | Advanced (cube/member links) | None |
| **Code Editing** | Generated only | Full editor + deployment | None |
| **Execution** | Task 4 (testing) | Step 4 (table execution) | Leads to subworkflow |
| **Automation** | Quick Actions automode | Step-by-step | Complete workflow option |
| **Review Pages** | After each task | After Steps 1-3 | After each step |
| **Dashboard Interface** | Task | Do | Review | Step | Do | Review | Step | Do | Review |

---

## Common Features Across All Workflows

### Dashboard Navigation

All workflows share common navigation patterns that make them intuitive to use. Sequential Execution means that all workflows require steps to be completed in order. Do and Execute Buttons trigger step execution when you're ready to proceed. Review Buttons provide access to results, statistics, and embedded editors for refinement. Progress Tracking uses visual indicators to show completion status at a glance. Step Dependencies ensure that each step builds properly on the previous step's outputs, maintaining data integrity throughout the process.

### Metadata Management

Metadata Management features are available in both the Main and Dataset Transformation Workflows to help you refine your data relationships. You can perform cube link editing to manage table relationships, cube structure item link editing to define variable joins, and member link editing to create value mappings. The Dataset workflow additionally provides network diagram visualization to help you understand and verify your data structure visually.

### Code Management

Code Management capabilities are available in both the Main and Dataset Transformation Workflows to help you work with generated transformation code. These workflows provide Python code generation from metadata, code review and validation tools, and syntax highlighting with error detection to catch issues early. The Dataset workflow offers additional advanced features including an advanced code editor with a deployment system that manages staging and production versions, as well as manual modification tracking to help you keep track of changes made to generated code.

### Review Capabilities
**All workflows include:**
- Execution statistics and metrics
- Result verification pages
- Import/processing logs
- Success/failure indicators

### Execution Options
- **Manual:** Step-by-step execution with review between steps
- **Automated:** (Main Workflow) Quick Actions automode; (DPM) Complete workflow option
- **Filtered:** (Dataset) Dimension-based filtering for targeted execution

---

## Navigation Between Workflows

### Accessing Workflows
1. From the **Home page**, click **"Workflows"** or **"Task Workflow Dashboard"**
2. Select your desired workflow:
   - **Main Workflow** for FINREP reporting
   - **Dataset Workflow** for Dataset/AnaCredit submissions
   - **DPM Workflow** for custom output layers

### Switching Workflows
- Use the main navigation menu to switch between workflows
- Each workflow maintains its own execution state
- You can work on multiple workflows simultaneously
- Progress is saved independently for each workflow

### Workflow Integration
- **DPM Workflow** integrates with **Main Workflow** Step 1
- **DPM Workflow** leads to **Output Layer Mapping Subworkflow**
- All workflows can use common configuration settings

---

## Getting Started

### Step 1: Identify Your Requirement

**Choose Main Workflow if:**
- You need standard FINREP regulatory reports
- You're processing DPM-based financial reporting
- You work with EIL (European Input Layer) data
- You need automated multi-task execution

**Choose Dataset Transformation if:**
- You submit Dataset or AnaCredit reports to ECB
- You need granular loan-level credit data reporting
- You require advanced code editing and deployment
- You want dimension-based filtering for execution

**Choose DPM Workflow if:**
- You need custom DPM output layer structures
- You're designing specialized mapping combinations
- You require semantic integration across frameworks
- You're extending standard regulatory templates

### Step 2: Verify Prerequisites

**For Main Workflow:**
- GitHub repository access and credentials
- Configuration files prepared
- Database connectivity established

**For Dataset Transformation:**
- Internet connection (for ECB metadata fetch)
- Database setup completed
- Python environment active

**For DPM Workflow:**
- Model type configured (EIL/ELDM)
- Repository parameters set
- Artifacts retrieved and database setup

### Step 3: Navigate to Workflow Dashboard

1. Launch FreeBIRD Application
2. Click **"Workflows"** or **"Task Workflow Dashboard"** from home page
3. Select your workflow from the dashboard

### Step 4: Execute Sequentially

1. Start with the first step/task
2. Click the **"Do"** or **"Execute"** button
3. Wait for completion
4. Click **"Review"** to verify results
5. Proceed to next step
6. Repeat until workflow completion

### Step 5: Review and Validate

- Use Review pages after each step
- Check statistics and metrics
- Validate data quality
- Use embedded editors if adjustments needed (Dataset workflow)
- Download results when complete

---

## Dashboard Features

### Status Indicators
- **Ready:** System is ready for execution
- **Configured:** Settings are saved and valid
- **In Progress:** Step is currently executing
- **Completed:** Step finished successfully
- **Failed:** Step encountered errors

### Action Buttons
- **Do/Execute:** Start step processing
- **Review:** View results and access tools
- **Deploy:** (Dataset) Push code to production
- **Reset:** (Main) Clear task history or complete reset

### Information Displays
- **Session ID:** Unique identifier for current workflow session
- **Database Status:** Connection and setup status
- **Configuration Status:** Settings validation status
- **Execution Time:** Duration for each step
- **Row Counts/Statistics:** Quantitative results

---

## Best Practices

### General Workflow Tips
1. **Execute in Order:** Always complete steps sequentially
2. **Review Every Step:** Use Review pages to validate before proceeding
3. **Save Configuration:** Ensure settings are saved before execution
4. **Monitor Status:** Check status indicators throughout execution
5. **Document Changes:** Keep notes on manual edits and customizations

### Main Workflow Specific
- Use Quick Actions automode for efficiency
- Select appropriate target task before running automode
- Verify GitHub credentials are current
- Check configuration shows "Ready" and "Configured"

### Dataset Transformation Specific
- Start with filtered executions to test
- Review generated code before deploying
- Deploy incrementally, not all at once
- Use embedded editors to refine auto-generated metadata
- Keep backups of manual code edits

### DPM Workflow Specific
- Complete prerequisites before starting
- Run complete workflow for full integration
- Proceed to Output Layer Mapping subworkflow after completion

---

## Troubleshooting

### Cannot Execute Step
- Verify previous steps completed successfully
- Check prerequisites are met
- Review error messages in logs
- Ensure database connectivity

### Review Page Not Loading
- Check browser JavaScript console
- Disable ad blockers or browser extensions
- Clear browser cache
- Try different browser

### Execution Takes Too Long
- Apply filters to reduce data volume (Dataset workflow)
- Check system resources and load
- Execute during off-peak hours
- Review optimization opportunities

### Configuration Issues
- Verify GitHub credentials (Main workflow)
- Check internet connection (Dataset Step 0)
- Validate configuration file format
- Review setup logs for errors

---

## Next Steps

Explore the individual workflow guides to dive deeper into each regulatory reporting process. The [Main Workflow Guide](user-guide/main-workflow-guide.html) provides detailed instructions for FINREP reporting and the 4-task sequential process. The [Dataset Transformation Guide](user-guide/dataset-transformation-guide.html) covers the complete AnaCredit workflow from ECB metadata fetch to code generation. Review the [Execute Dataset Guide](user-guide/execute-dataset-guide.html) for comprehensive instructions on Step 4 table execution with filtering options. The [DPM Workflow Guide](user-guide/dpm-workflow-guide.html) explains how to create custom DPM output layer structures. Learn about [Pull Request Creation](user-guide/pull-request-creation-guide.html) to submit your processed data for collaborative review. Finally, explore the [Output Layer Mapping Workflow](user-guide/output-layer-mapping-workflow.html) for the 7-step process of creating custom data transformations.

---

## Need Help?

### Documentation Resources
- **[Main Workflow Guide](user-guide/main-workflow-guide.html)** - Detailed FINREP workflow instructions
- **[Dataset Transformation Guide](user-guide/dataset-transformation-guide.html)** - Steps 0-3 comprehensive guide
- **[Dataset Execution Guide](user-guide/execute-dataset-guide.html)** - Step 4 execution instructions
- **[DPM Workflow Guide](user-guide/dpm-workflow-guide.html)** - DPM workflow details
- **[Output Layer Mapping Guide](user-guide/output-layer-mapping-workflow.html)** - Subworkflow documentation
- **[Edit Links Features](user-guide/edit-links-features.html)** - Metadata editor instructions
- **[Code Editing and Publishing](user-guide/code-editing-and-publishing.html)** - Code management guide

### Technical Support
- **Eclipse EFBT Wiki:** https://github.com/eclipse/efbt/wiki
- **Getting Started:** https://github.com/eclipse-efbt/efbt/wiki/Getting-Started-with-PyBIRD-AI
- **ECB Resources:**
  - FINREP: https://www.ecb.europa.eu/stats/ecb_statistics/finrep/
  - AnaCredit: https://www.ecb.europa.eu/stats/ecb_statistics/anacredit/

---

## Quick Tips

**First-time users:**
- Start with Main Workflow if processing standard reports
- Use Dataset Transformation for ECB credit reporting
- Complete prerequisites before beginning any workflow

**Experienced users:**
- Use automation features (automode, complete workflow)
- Leverage embedded editors for customization
- Apply filters for efficient testing
- Maintain documentation of customizations

**All users:**
- Review outputs at every step
- Keep configuration backed up
- Monitor execution times for performance trends
- Document workflow decisions for auditing

---

## Summary

PyBIRD AI workflows provide comprehensive, automated solutions for regulatory reporting:

- **Main Workflow:** Streamlines FINREP reporting with 4 automated tasks
- **Dataset Transformation:** Handles ECB Dataset/AnaCredit submissions with 5 flexible steps
- **DPM Workflow:** Creates custom output layers with 3 integrated steps

All workflows share a consistent dashboard interface, making it easy to navigate between different regulatory requirements while maintaining familiar patterns. Choose the workflow that matches your reporting needs, follow the sequential steps, and leverage the built-in review and editing capabilities for successful regulatory compliance.
