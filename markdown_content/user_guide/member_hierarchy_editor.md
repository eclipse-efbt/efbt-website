# Member Hierarchy Editor User Guide

## Overview

The Member Hierarchy Editor is a visual tool within the FreeBIRD Application designed for creating, managing, and visualizing hierarchical relationships between data members. This interface provides an intuitive drag-and-drop environment for building complex parent-child relationships and organizational structures within your data taxonomy.

![Member Hierarchy Editor Main Interface](images/screenshots/member_hierarchy_editor/MemberHierarchy_Editor_Screenshot__4.20.03PM.png)

## Interface Components

### Header Section

#### Navigation Bar
- **FreeBIRD Application**: Application title in the top-left corner
- **Home**: Quick navigation to return to the main dashboard
- **Trail Lineage**: Access to data lineage and audit trail features

#### Status Indicator
- Displays current hierarchy being edited (e.g., `CRDT_QLTY_HIER_3`)
- **Back to Review**: Link to return to the review screen

### Control Panel

#### Action Buttons (Top Right)

- **Create Arrow** (White icon): Establishes parent-child relationships between nodes
- **Delete Arrow** (White icon): Removes existing relationships between nodes
- **Export** (Blue): Exports the hierarchy structure to external formats
- **Save to Database** (Blue): Persists the current hierarchy to the database
- **Clear** (Red): Resets the workspace and removes all unsaved changes
- **60%** (Gray): Progress indicator showing completion status
- **Fit All** (White): Adjusts zoom to display the entire hierarchy in view

### Left Panel - Hierarchy Manager

#### Hierarchy Selection
- **Select Hierarchy**: Dropdown menu to choose from available hierarchies
  - Displays currently selected hierarchy (e.g., `CRDT_QLTY_HIER_3`)
  - Provides quick access to switch between different hierarchy structures

#### Member Search
- **Search Members**: Text input field with placeholder "Type to filter members..."
  - Real-time filtering of available members
  - Helps locate specific members in large datasets

#### Member List
The left panel displays available members organized by status:

##### Not in Hierarchy
- **Orange indicator**: Members available but not yet added to the hierarchy
- Shows member codes and descriptions
- Example: `CRDT\_QLTY\_14 Already in hierarchy`

##### Default Members
- **Yellow highlighting**: Pre-defined default members
- Cannot be removed from the hierarchy
- Examples:
  - `Default\_because\_both\_unlikely\_to\_pay\_and\_more\_than\_90\_180\_days\_past\_due`
  - `Default\_because\_unlikely\_to\_pay`
  - `Default\_because\_more\_than\_90\_180\_days\_past\_due`
  - `Default`

## Visual Hierarchy Canvas

![Hierarchy Visualization with Relationships](images/screenshots/member_hierarchy_editor/MemberHierarchy_Editor_Screenshot__4.21.46PM.png)

### Node Structure

Each node in the hierarchy contains:
- **Red pin icon**: Visual indicator for the node
- **Node name**: Primary identifier (e.g., `root_gcm_4`)
- **NAME field**: Display name or label
- **DESCRIPTION field**: Detailed description of the member
- Additional metadata fields as configured

### Hierarchy Visualization

The canvas displays the hierarchical structure with:
- **Parent nodes** at higher levels
- **Child nodes** connected below with relationship lines
- **Visual connectors** showing parent-child relationships
- Interactive nodes that can be selected and modified

## Key Functions

### Creating a New Hierarchy

1. Select "Choose a hierarchy..." from the dropdown
2. Click on empty option to start a new hierarchy
3. Begin adding members from the left panel

### Adding Members to Hierarchy

1. **Search or browse** for members in the left panel
2. **Drag** the member from the left panel
3. **Drop** it onto the canvas workspace
4. The member will appear as a node with editable fields

### Creating Relationships

1. Click **Create Arrow** button to enter relationship mode
2. **Click** on the parent node
3. **Drag** to the child node
4. **Release** to create the relationship
5. A connecting line will appear between the nodes

### Deleting Relationships

1. Click **Delete Arrow** button to enter deletion mode
2. **Click** on the relationship line you want to remove
3. The connection will be deleted immediately
4. Exit deletion mode by clicking another tool

### Editing Node Information

1. **Click** on any node to select it
2. **Edit fields** directly within the node:
   - Update NAME field
   - Modify DESCRIPTION
   - Edit any custom metadata fields
3. Changes are saved automatically to the workspace

### Navigating the Canvas

- **Pan**: Click and drag on empty canvas space to move the view
- **Zoom**: Use mouse wheel or zoom controls
- **Fit All**: Click the Fit All button to see the entire hierarchy
- **Select**: Click on nodes to select them for editing

### Searching for Members

1. Click in the **Search Members** field
2. Type part of the member name or code
3. The list filters in real-time
4. Select from filtered results

### Saving Your Work

1. Complete your hierarchy modifications
2. Click **Save to Database** button
3. Confirm the save operation if prompted
4. Wait for confirmation message

### Exporting Hierarchies

1. Click **Export** button
2. Select export format from options
3. Choose destination for the file
4. The hierarchy will be exported with all relationships intact

## Working with Complex Hierarchies

### Best Practices for Large Hierarchies

1. **Start from the top**: Build from root nodes downward
2. **Group related items**: Keep similar members close together
3. **Use consistent naming**: Maintain naming conventions across levels
4. **Regular saves**: Save to database frequently to prevent data loss

### Managing Multiple Levels

- Create clear parent-child relationships
- Avoid circular dependencies
- Maintain consistent depth where possible
- Use descriptions to clarify complex relationships

## Visual Indicators

### Node States
- **Orange text**: Members not yet in hierarchy
- **Yellow background**: Default members
- **Red pin icon**: Active node marker
- **Connected lines**: Established relationships

### Progress Tracking
- The **60%** indicator shows overall completion
- Helps track progress on large hierarchy projects
- Updates as you add members and relationships

## Tips for Efficient Usage

1. **Use search extensively**: Quickly find members instead of scrolling
2. **Keyboard shortcuts**: Learn available shortcuts for faster editing
3. **Batch operations**: Select multiple nodes for group actions
4. **Visual organization**: Arrange nodes logically for better readability
5. **Regular exports**: Create backups through the export function

## Troubleshooting

### Common Issues and Solutions

1. **Nodes not connecting**: Ensure Create Arrow mode is active
2. **Cannot delete relationship**: Activate Delete Arrow mode first
3. **Members not appearing**: Check if already in hierarchy (orange text)
4. **Save fails**: Verify database connectivity and permissions
5. **Canvas performance**: Use Fit All to reset view if navigation becomes sluggish

### Data Validation

- The system prevents circular relationships
- Default members cannot be removed
- Duplicate members are automatically detected
- Invalid relationships are highlighted

## Advanced Features

### Filtering and Views
- Filter members by type or category
- Show/hide different relationship types
- Adjust visual layout for presentation

### Collaboration
- Multiple users can work on different hierarchies
- Changes are tracked in the trail lineage
- Export function enables sharing with stakeholders
