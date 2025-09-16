## Feature Overview

The Mapping Editor is a sophisticated data transformation tool within Eclipse Free BIRD Tools that enables users to create, manage, and modify complex mappings between source and target data variables. This interface serves as the bridge between various source systems and regulatory reporting structures, facilitating precise data alignment and transformation for compliance purposes.

## Purpose

The Mapping Editor addresses the critical challenge of data transformation in regulatory environments by providing:
- **Data Alignment**: Map source system data to regulatory reporting requirements
- **Transformation Rules**: Define complex business logic for data conversion
- **Variable Management**: Control both source and target variable definitions
- **Validation Framework**: Ensure mapping accuracy and completeness
- **Audit Capability**: Track all mapping changes for compliance purposes
- **Batch Operations**: Efficiently manage multiple mappings simultaneously

This feature is essential for data engineers, compliance officers, and business analysts who need to ensure accurate data flow from operational systems to regulatory reports while maintaining full transparency and control over transformation processes.

## Getting Started

### Prerequisites
Before using the Mapping Editor, ensure:
- Understanding of source data structures and formats
- Knowledge of target regulatory requirements
- Appropriate permissions for mapping creation and modification
- Access to both source and target variable definitions
- Familiarity with transformation business rules

### Accessing the Mapping Editor
Navigate to the FreeBIRD Application and access the Mapping Editor from the main dashboard. The interface provides comprehensive tools for creating and managing data transformations between systems.

![Mapping Editor Main Interface](images/screenshots/mapping_editor/Mapping_Editor_Screenshot__4.20.17PM.png)

## Step-by-Step Guide

### Understanding the Interface

The Mapping Editor consists of several key areas:

#### Control Panel Components
- **Select Mapping ID**: Dropdown menu to choose from existing mappings (e.g., `DPM_BAS_MCY_SST_AE_F32.03.b`)
- **Apply Filters**: Filter criteria to focus on specific mapping data
- **Navigation**: Quick access to home, lineage tracking, and review functions

#### Action Buttons
**Row Management:**
- **Add Mapping Row** (Green): Creates new mapping entries
- **Edit Mapping Row** (Green): Modifies existing selected rows
- **Delete Mapping Row** (Red): Removes selected mapping rows

**Mapping Operations:**
- **Duplicate Mapping** (Green): Creates copies of existing mappings

**Variable Management:**
- **Add Target Variable** (Orange): Defines new target variables and members
- **Add Source Variable** (Blue): Adds new source variables and members

### Creating New Mappings

**Step 1: Initialize Mapping**
- Select an existing mapping from the **Select Mapping ID** dropdown as a template, or
- Create a new mapping by using **Duplicate Mapping** with a new name
- Choose appropriate naming conventions that reflect the data flow

**Step 2: Define Source Variables**
- Click **Add Source Variable** to open the variable definition dialog
- Specify variable name, data type, and source system details
- Add member variables if the source represents hierarchical data
- Define data validation rules and constraints

**Step 3: Define Target Variables**
- Click **Add Target Variable** to create target definitions
- Map to specific regulatory reporting requirements
- Configure target data formats and validation rules
- Establish hierarchical relationships if needed

**Step 4: Create Mapping Rows**
- Click **Add Mapping Row** to establish source-to-target relationships
- Select source variables from available options
- Map to corresponding target variables
- Define transformation logic and business rules

### Managing Existing Mappings

![Mapping Editor with Data](images/screenshots/mapping_editor/Mapping_Editor_Screenshot__4.20.27PM.png)

**Viewing Mapping Details:**
- Use the dropdown to select specific mappings
- Apply filters to focus on relevant mapping rows
- Review the data grid showing complete source-to-target relationships
- Examine transformation rules and validation logic

**Modifying Mappings:**
- Select specific rows in the data grid
- Click **Edit Mapping Row** to modify transformation rules
- Update variable definitions using the variable management buttons
- Save changes to persist modifications

**Removing Mappings:**
- Select unwanted rows or entire mapping sets
- Use **Delete Mapping Row** to remove selected items
- Confirm deletion to prevent accidental data loss
- Review impact on dependent systems before finalizing

### Working with Variables

**Source Variable Management:**
- Define variables that represent your source system data
- Specify data types, formats, and validation rules
- Create hierarchical relationships between variables
- Document business context and usage guidelines

**Target Variable Management:**
- Map to specific regulatory reporting elements
- Ensure compliance with reporting standards
- Define aggregation and calculation rules
- Establish quality validation checkpoints

### Advanced Mapping Operations

**Duplicate and Customize:**
- Use **Duplicate Mapping** to create variations of existing mappings
- Modify duplicate mappings for different regulatory frameworks
- Maintain consistency while adapting to specific requirements
- Document changes for audit and maintenance purposes

**Batch Operations:**
- Apply filters to select multiple related mappings
- Perform bulk updates on transformation rules
- Export mapping definitions for backup or migration
- Import mapping templates for standardization

## Best Practices

### Mapping Design
- **Standardize Naming**: Use consistent conventions for mapping IDs and variable names
- **Document Logic**: Clearly describe transformation rules and business rationale
- **Test Thoroughly**: Validate mappings with sample data before production use
- **Version Control**: Maintain records of mapping changes and evolution

### Performance Optimization
- **Filter First**: Use filters to focus on relevant mapping subsets
- **Batch Similar**: Group related variable definitions and mapping operations
- **Regular Cleanup**: Remove obsolete mappings to maintain system performance
- **Monitor Usage**: Track which mappings are actively used for optimization

### Quality Assurance
- **Validation Rules**: Implement comprehensive data validation at both source and target
- **Cross-Reference**: Verify mappings against regulatory documentation
- **Peer Review**: Have mapping logic reviewed by business and technical experts
- **Regular Audits**: Periodically review mapping accuracy and completeness

## Troubleshooting

### Common Issues and Solutions

**Mapping Not Found:**
- Verify the mapping ID exists in the system
- Check filter settings that might hide the desired mapping
- Confirm you have permissions to view the specific mapping
- Refresh the interface if data appears outdated

**Variable Definition Errors:**
- Validate source variable definitions against actual source systems
- Check target variable alignment with regulatory requirements
- Verify data type compatibility between source and target
- Review hierarchical relationships for logical consistency

**Transformation Failures:**
- Test transformation logic with sample data
- Validate business rules implementation
- Check for missing or incomplete mapping rows
- Review data quality validation rules

**Performance Issues:**
- Apply appropriate filters to reduce dataset size
- Limit the number of concurrent mapping operations
- Check system resources during complex transformations
- Consider breaking large mappings into smaller, manageable components

### Data Validation
The system automatically validates:
- Source-to-target variable compatibility
- Transformation rule syntax and logic
- Required field completion
- Circular reference prevention
- Duplicate mapping detection

## Conclusion

The Mapping Editor provides comprehensive capabilities for managing complex data transformations in regulatory environments. By offering both detailed control over individual mappings and powerful batch operations, it enables organizations to maintain accurate, auditable data flows from source systems to regulatory reports while ensuring compliance with evolving requirements.

### Next Steps
- Explore the [Cube Links View and Edit](cube-links-view-and-edit.html) feature for understanding data relationships
- Review the [Member Hierarchy Editor](member-hierarchy-editor.html) for hierarchical data organization
- Learn about [Workflow Dashboard](workflow-dashboard-guide.html) integration for automated processing

For complex transformation logic support or advanced mapping strategies, connect with our community via [Eclipse Chat](https://chat.eclipse.org/#/room/%23technology.efbt:matrix.eclipse.org) or email [efbt-dev@eclipse.org](mailto:efbt-dev@eclipse.org).