# Cube Links View and Edit User Guide

## Overview

The Cube Links View and Edit interface is a powerful tool within the FreeBIRD Application that enables users to create, manage, and visualize relationships between data cubes and their components. This feature provides both tabular and graphical representations of how data flows from source cubes through various transformations to target cubes, making it essential for understanding and maintaining complex data relationships in the regulatory reporting framework.

![Cube Links View Main Interface](images/screenshots/cube_links_view/CubeLinksView_Screenshot__4.38.32PM.png)

## Interface Components

### Header Section

#### Navigation Bar
- **FreeBIRD Application**: Application title in the top-left corner
- **Home**: Quick navigation to return to the main dashboard
- **Trail Lineage**: Access to data lineage tracking and audit capabilities
- **Back to Review**: Return link to the previous review screen

### Main Control Panel

#### Selection Filters

##### Foreign Cube Selector
- **Dropdown menu**: Select the source cube for viewing/editing links
- Example: `F_05_01_REF_FINREP_3_0`
- Lists all available foreign cubes in the system

##### Product Identifier Selector
- **Dropdown menu**: Filter cube links by product type
- Example: `Other loans`
- Dynamically updates based on selected foreign cube

#### Filter Controls (Top Right)

- **Apply Filters** (Blue button): Apply selected filter criteria to the data grid
- **Reset Filters** (Gray button): Clear all applied filters and return to default view

### Action Buttons

#### Data Management
- **Add New Cube Link** (Green button): Opens dialog to create new cube link relationships

#### Visualization Options
- **View Network Graph** (Blue button): Display graphical representation of cube relationships
- **Export Diagram** (Purple button): Export the network diagram to various formats

## Data Grid

The main data grid displays cube link information with the following columns:

### Grid Columns

1. **Maintenance Agency**: Entity responsible for maintaining the cube link (typically "None")
2. **Cube Link ID**: Unique identifier for each cube link relationship
   - Format: `ForeignCube::TargetItem`
   - Example: `F_01_01_REF_FINREP_3_0::CLLTRL::Other loans`
3. **Code**: Classification code (typically "None")
4. **Name**: Descriptive name of the link relationship
   - Format: `INSTRUMENT:Description:TARGET`
   - Example: `INSTRMNT:Other loans:CLLTRL`

## Network Graph Visualization

![Network Graph Visualization](images/screenshots/cube_links_view/CubeLinksView_Screenshot__4.38.39PM.png)

### Understanding the Visual Legend

The network graph uses specific shapes and colors to represent different components:

#### Node Types
- **Source Cube** (Orange cylinder): The originating data cube
- **Source Item** (Blue rectangle): Individual data elements from the source
- **Target Item** (Green diamond): Transformation or mapping points
- **Target Cube** (Yellow cylinder): The destination data cube

#### Data Flow
- Arrows indicate the direction of data flow
- Lines connect related components
- Hierarchical layout shows transformation stages

### Reading the Network Diagram

#### Example: F_05_01_REF_FINREP_3_0_Other_loans

The diagram shows:
1. **Left Panel (INSTRMNT)**:
   - Source node (orange circle) labeled "INSTRMNT"
   - Branches to two blue rectangles:
     - `TYP_INSTRMNT` � connects to green diamond `TYP_INSTRMNT`
     - `RPYMNT_RGHTS` � connects to green diamond `RPYMNT_RGHTS`

2. **Right Panel (F_05_01_REF_FINREP_3_0)**:
   - Shows the target cube structure
   - Green diamonds represent mapped target items
   - Connections flow into the yellow target cube

3. **Bottom Panel (PRTY)**:
   - Additional relationship layer
   - Shows party-related mappings

## Key Functions

### Creating a New Cube Link

1. Click **Add New Cube Link** button
2. In the dialog:
   - Select source cube from dropdown
   - Choose source items to link
   - Define target items for mapping
   - Specify transformation rules if applicable
3. Click **Save** to create the link
4. The new link appears in the data grid

### Viewing Cube Link Details

1. Select a row in the data grid
2. View complete link information including:
   - Full path from source to target
   - Intermediate transformations
   - Associated metadata

### Filtering Cube Links

1. Use the **Foreign Cube** dropdown to filter by source
2. Use the **Product Identifier** to filter by product type
3. Click **Apply Filters** to update the view
4. Use **Reset Filters** to clear all filters

### Visualizing Relationships

1. Select cube links in the grid (or use filters)
2. Click **View Network Graph**
3. The network diagram opens in a modal window:
   - Pan by clicking and dragging the canvas
   - Zoom using mouse wheel or controls
   - Click nodes for additional details
4. Click **Close** (red button) to exit the visualization

### Exporting Diagrams

1. With network graph open, click **Export Diagram**
2. Choose export format:
   - PNG for images
   - SVG for scalable graphics
   - PDF for documentation
3. Select destination and save

## Understanding Cube Link Relationships

### Hierarchical Structure

Cube links follow a hierarchical pattern:
- **Level 1**: Source cube definition
- **Level 2**: Source items and attributes
- **Level 3**: Transformation/mapping layer
- **Level 4**: Target items and attributes
- **Level 5**: Target cube destination

### Link Naming Convention

Links follow the pattern:
```
[SourceCube]::[TransformationType]::[TargetDescription]
```

Example breakdown:
- `F_01_01_REF_FINREP_3_0` - Source cube identifier
- `INSTRMNT` - Transformation type (Instrument)
- `Tangible assets` - Target description

## Best Practices

### Data Management
1. **Consistent Naming**: Use clear, descriptive names for cube links
2. **Documentation**: Export diagrams when making significant changes
3. **Regular Review**: Periodically review links for accuracy
4. **Testing**: Validate links with sample data before production use

### Visualization Tips
1. **Start Simple**: Begin with filtered views of specific relationships
2. **Use Colors**: Leverage the color coding to quickly identify component types
3. **Export Key Diagrams**: Save important relationship diagrams for documentation
4. **Layer Analysis**: Review each hierarchical level separately for complex cubes

### Performance Optimization
1. **Filter First**: Apply filters before generating large network graphs
2. **Batch Operations**: Group related cube link creations
3. **Regular Cleanup**: Remove obsolete or duplicate links

## Common Use Cases

### Regulatory Reporting Setup
1. Map source system cubes to regulatory templates
2. Define transformation rules for data aggregation
3. Visualize complete data flow for audit purposes

### Data Quality Validation
1. Trace data lineage through cube links
2. Identify potential gaps in mappings
3. Verify completeness of transformations

### Change Impact Analysis
1. View all relationships for a specific cube
2. Assess impact of proposed changes
3. Document current state before modifications

## Troubleshooting

### Common Issues

1. **Missing Cube Links**:
   - Verify filter settings
   - Check user permissions
   - Refresh the page

2. **Visualization Not Loading**:
   - Reduce data set with filters
   - Check browser compatibility
   - Clear browser cache

3. **Cannot Create New Link**:
   - Verify source and target cubes exist
   - Check for duplicate links
   - Ensure proper permissions

4. **Export Failures**:
   - Check available disk space
   - Verify export permissions
   - Try different format

### Data Validation

The system automatically validates:
- Circular reference prevention
- Duplicate link detection
- Required field completion
- Data type compatibility

## Advanced Features

### Multi-Level Mappings
- Create complex transformation chains
- Define conditional mappings
- Implement business rules in links

### Bulk Operations
- Import cube links from templates
- Export link definitions for backup
- Mass update link properties

### Integration Points
- Connect with data quality rules
- Link to validation frameworks
- Interface with reporting engines

## Tips for Efficient Usage

1. **Keyboard Shortcuts**: Learn available shortcuts for faster navigation
2. **Template Usage**: Create template links for common patterns
3. **Regular Exports**: Maintain diagram library for documentation
4. **Collaborative Review**: Share network graphs with stakeholders
5. **Version Tracking**: Document changes to critical cube links

## Security and Governance

- All cube link modifications are logged
- Changes tracked in trail lineage
- Role-based access control for editing
- Approval workflow for critical links
