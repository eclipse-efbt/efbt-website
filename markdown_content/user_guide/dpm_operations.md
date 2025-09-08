# DPM Operations User Guide

DPM (Data Point Model) Operations provides a 3-step workflow for processing regulatory data according to European Banking Authority (EBA) standards. This guide covers the essential steps to prepare, import, and create output layers from DPM data.

## Access DPM Operations

1. Launch FreeBIRD Application → Home → **"DPM Data Operations"**
2. Follow the 3-step sequential process

![DPM Operations](images/screenshots/dpm_operations.png)

## 3-Step DPM Workflow

Execute steps in order: **Prepare → Import → Create Output Layers**

| Step                         | Purpose                                           | Action                            | Result                                                  |
|------------------------------|---------------------------------------------------|-----------------------------------|-------------------------------------------------------------|
| Step 1: Prepare DPM Data     | Validates and stages source data for processing   | Click "Prepare DPM Data" card     | Source data validated and ready for import                |
| Step 2: Import DPM Data      | Processes source data and applies transformations | Click "Import DPM Data" card      | Source data imported into DPM structures with validation  |
| Step 3: Create Output Layers | Generates final regulatory reporting outputs      | Click "Create Output Layers" card | All regulatory reports generated and ready for submission |

When clicking on **Create Output Layers**, you will see the following screen:

![DPM Output Layer Generation](images/screenshots/dpm_operations_output_layer_generation.png)

**Selection Options:**
1. **Framework** - Choose regulatory framework (COREP, FINREP, LCR, etc.)
2. **Framework Version** - Select specific version of the chosen framework
3. **Table Code** - Pick specific table codes for targeted output generation

**Process:**
1. Select your desired framework, version, and/or table codes
2. System generates regulatory reports in required smcube format
3. ✅ Selected regulatory outputs generated and ready for integration

## Essential Best Practices

| **Sequential Processing** | **Data Quality Management** | **Performance Optimization** |
|----------|----------|----------|
| Execute steps in order: Prepare → Import → Create Output | Address quality issues in Prepare step before import | Process data in appropriate batch sizes for system capacity |
| Complete each step before proceeding to the next | Monitor validation error rates during Import process | Monitor system resources during operations to prevent overload |
| Validate results at each stage before moving forward | Verify output compliance in final step against EBA standards | Schedule intensive operations during off-peak hours |

## Troubleshooting

| **Preparation Failures** | **Import Processing Errors** | **Output Generation Problems** |
|-------|-------------------|----------|
| Source data validation fails | High error rates during import | Output creation fails |
| • Check file formats and encoding<br>• Verify required data elements present<br>• Review preparation logs for errors | • Confirm preparation completed successfully<br>• Check transformation rule configurations<br>• Analyze exception reports for patterns | • Verify import completed successfully<br>• Check output template configurations<br>• Review calculation rules and logic |

## Integration Features

| **Workflow Dashboard** | **External Systems** | **Quality Management** | **Compliance Monitoring** |
|-------------|---------|----------|----------|
| Integrate with broader reporting workflows | Connect to core banking and reporting platforms | Link to data governance systems | Maintain audit trails for supervision |
