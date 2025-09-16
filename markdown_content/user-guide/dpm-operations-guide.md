## Feature Overview

DPM (Data Point Model) Operations is a specialized module within Eclipse Free BIRD Tools that provides a streamlined 3-step workflow for processing regulatory data according to European Banking Authority (EBA) standards. This feature transforms raw financial data into compliant regulatory reports through a systematic preparation, import, and output generation process.

## Purpose

DPM Operations addresses the critical need for standardized regulatory reporting in the financial sector. This feature enables:
- **Regulatory Compliance**: Ensure your data meets EBA DPM specifications and reporting requirements
- **Data Validation**: Automated checks throughout the process prevent non-compliant submissions
- **Efficient Processing**: Transform complex financial data into structured regulatory formats
- **Framework Flexibility**: Support for multiple regulatory frameworks including COREP, FINREP, and LCR
- **Quality Assurance**: Built-in validation at each step reduces errors and rework

Financial institutions use DPM Operations to streamline their regulatory reporting obligations, reduce manual processing errors, and maintain compliance with evolving European banking regulations.

## Getting Started

### Prerequisites
Before using DPM Operations, ensure:
- Your source data is prepared in the required format
- You have selected the appropriate regulatory framework
- Database connectivity is established
- You understand the 3-step sequential process

### Accessing DPM Operations

To access DPM Operations, launch the FreeBIRD Application, navigate to the Home page, and click on **"DPM Data Operations"**. You will then follow a 3-step sequential process.

![DPM Operations](images/screenshots/dpm_operations/dpm_operations.png)

## Step-by-Step Guide

### Overview of the 3-Step DPM Workflow

The DPM workflow consists of three sequential steps that must be executed in order: Prepare, Import, and Create Output Layers.

### Step 1: Prepare DPM Data

Click the "Prepare DPM Data" card to validate and stage your source data for processing. This step ensures your data meets all requirements before moving to the import phase. The system will validate your source data and confirm it is ready for import.

### Step 2: Import DPM Data

Click the "Import DPM Data" card to process your source data and apply the necessary transformations. During this step, the system imports your data into DPM structures while performing validation checks. Once complete, your data will be properly structured according to DPM specifications.

### Step 3: Create Output Layers

Click the "Create Output Layers" card to generate your final regulatory reporting outputs. This step produces all required regulatory reports that are ready for submission to authorities.

![DPM Output Layer Generation](images/screenshots/dpm_operations/dpm_operations_output_layer_generation.png)

When creating output layers, you need to select your regulatory framework such as COREP, FINREP, or LCR. Then choose the specific version of your selected framework. You can also pick specific table codes if you want targeted output generation. After making your selections, the system will generate regulatory reports in the required smcube format, and your selected outputs will be ready for integration.

## Best Practices

Always execute the three steps in sequential order: Prepare, then Import, then Create Output Layers. Complete each step fully before proceeding to the next one. Address any data quality issues during the Prepare step before attempting to import. Monitor validation error rates during the Import process to catch issues early. Verify that your final outputs comply with EBA standards before submission.

## Troubleshooting

### Common Issues and Solutions

**Data Preparation Failures:**
- Check that your file formats and encoding are correct
- Verify that all required data elements are present
- Review the preparation logs for specific error messages
- Ensure source data meets DPM specifications

**Import Errors:**
- Confirm that the preparation step completed successfully
- Check your transformation rule configurations
- Analyze exception reports for patterns
- Verify data type compatibility

**Output Generation Problems:**
- Verify that the import completed successfully
- Check your output template configurations
- Review the calculation rules and logic for accuracy
- Ensure selected framework version is correct

**Performance Issues:**
- Consider processing smaller data batches
- Check available system resources
- Verify database performance
- Review network connectivity for remote data sources

## Conclusion

DPM Operations simplifies the complex task of regulatory reporting by providing a structured, validated approach to data processing. The 3-step workflow ensures that your financial data is properly prepared, imported, and transformed into compliant regulatory reports ready for submission to authorities.

### Next Steps
- Review the [Workflow Dashboard Guide](workflow-dashboard-guide.html) for comprehensive workflow management
- Explore [Execute Datapoint Guide](execute-datapoint-guide.html) for detailed execution options
- Learn about [Pull Request Creation](pull-request-creation-guide.html) to submit your reports

For regulatory framework updates or technical support, reach out through [Eclipse Chat](https://chat.eclipse.org/#/room/%23technology.efbt:matrix.eclipse.org) or contact us at [efbt-dev@eclipse.org](mailto:efbt-dev@eclipse.org).