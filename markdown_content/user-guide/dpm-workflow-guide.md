# DPM Workflow Guide

## Overview

The DPM (Data Point Model) Workflow is a specialized 3-step process for creating DPM output layer structures and combinations. This workflow integrates seamlessly with the Main Workflow to provide enhanced DPM functionality, enabling you to design custom output layers and mapping structures for your regulatory reporting needs.

## Prerequisites

Before starting the DPM Workflow, you need to ensure your system is properly configured. First, configure your instance with the model type you want to work with, selecting either EIL (European Input Layer) or ELDM (European Logical Data Model). You'll also need to set up your repository connection and configure other mandatory parameters required for running the application. Next, run the fetch artifacts command and execute the setup database operation from the quick action command panel. Optionally, you can run the Main Workflow Step 1 to get reference artifacts loaded into the system, which can be helpful for certain mapping scenarios.

## Workflow Structure

The DPM Workflow consists of three sequential steps that build upon each other. The workflow can optionally start with Step 0 from the Main Workflow, which loads reference data into the database. Step 1 prepares the DPM data for import by formatting and validating it according to the application's requirements. Step 2 imports the prepared DPM data into the database, creating the necessary metadata structures. Finally, Step 3 creates the output layers based on the imported data, redirecting you to the subworkflow for detailed output layer configuration.

```
(Main Workflow) Step 0: optional - load reference data into the database
    ↓
Step 1: Prepare DPM Data
    ↓
Step 2: Import DPM Data
    ↓
Step 3: Create Output Layers
```

Similar to the main workflow, you have flexibility in how you execute these steps. You can trigger the steps one at a time, reviewing the results after each step before proceeding to the next. Alternatively, you can run the complete workflow by clicking the "Run Complete DPM Workflow" button, which automatically executes all steps in sequence, including the optional first step from the Main Workflow.

When the workflow completes successfully, Step 3 will redirect you to the Output Layer Mapping subworkflow. This subworkflow provides an interactive interface for designing your custom mappings and output layer structures. You can find more information about this subsequent step in the Next Steps section below.

## Outcome

After running the complete DPM workflow, your application will contain a full import of the latest DPM Database, formatted according to the application's metadata format. This comprehensive import enables diverse subsequent operations and facilitates semantic integration between multiple regulatory frameworks. The structured metadata allows you to create mappings between different regulatory requirements, design custom output layers that meet specific reporting needs, and maintain consistency across various regulatory submissions.

## Conclusion

The DPM workflow provides a streamlined approach for importing the latest branch of the DPM database into your regulatory reporting system. Beyond simple data import, this workflow opens up a new and interactive way to design mappings between different regulatory frameworks. The output layer creation capabilities allow you to customize your reporting structures to match evolving regulatory requirements while maintaining the semantic relationships that ensure data consistency and accuracy across different reporting contexts.

## Next Steps

After completing the DPM Workflow, explore these related guides to continue your work. The [Workflow Dashboard Guide](user-guide/workflow-dashboard-guide.html) provides an overview of all available workflows and helps you understand how the DPM workflow fits into your broader regulatory reporting strategy. Proceed to the [Output Layer Mapping Workflow](user-guide/output-layer-mapping-workflow.html) for the detailed 7-step process that follows DPM import, allowing you to design custom mapping structures and output layers.
