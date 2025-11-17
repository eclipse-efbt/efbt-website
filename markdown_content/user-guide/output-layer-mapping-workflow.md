# Output Layer Mapping Workflow

## Feature Overview

Output Layer Mapping is a 7-step wizard that helps you create custom connections between your source data and regulatory reporting formats. The workflow guides you through defining exactly how your data transforms into required output structures for FINREP, COREP, or custom reporting frameworks.

## Purpose

This workflow provides a comprehensive set of features for managing output layer mappings. Structured Mapping Creation guides you through a step-by-step process for defining data transformations, while Multi-Dimensional Support allows you to handle complex report structures with multiple axes. Code List Management capabilities enable you to map source values to target codes automatically, and Transformation Logic features let you apply calculations and conversions during the mapping process. Validation Tools help you verify mappings before generation to ensure accuracy.

Use this workflow when creating new output structures or updating existing mappings.

## Getting Started

### Prerequisites

Before beginning the Output Layer Mapping workflow, ensure that your source data tables are imported in the system, you have a clear understanding of the target report structure, you've prepared a field mappings list that defines source to target relationships, and you have member value mappings prepared for code translations.

### Accessing the Workflow

Navigate to **Tools** > **Output Layer Mapping** or visit `/pybirdai/output-layer-mapping/`

**Time required**: 15-45 minutes depending on complexity

## The 7-Step Process

### Step 1: Choose Your Report

Select which report table you want to create mappings for.

**Steps**:
1. Choose **Framework** (FINREP, COREP, etc.)
2. Select **Version** (e.g., 3.0)
3. Pick specific **Table** (e.g., F_01_01 - Balance Sheet)
4. Review preview to confirm
5. Click **Continue**

**Tips**: Dropdowns filter automatically as you select. Verify you're selecting the correct version.

---

### Step 2: Check Existing Mappings

Review any existing mappings for this table and decide your approach.

**Scenarios**:
- **No existing mappings**: Green message - proceed
- **Existing mappings found**: Choose to delete, update, or select different table

**Options**:
- **Delete old mappings**: Start fresh (recommended for new versions)
- **Update existing**: Modify current mappings
- **Choose different table**: Go back to Step 1

**Tip**: Document why you're replacing mappings for future reference.

---

### Step 3: Select Report Cells

Choose which specific cells (combinations) in your report you want to create.

**Understanding Axes**:
Reports are multi-dimensional. For example:
- **Axis X** (Rows): Asset types - Loans, Securities, Cash
- **Axis Y** (Columns): Maturities - Up to 1 year, 1-5 years, Over 5 years
- **Axis Z** (Sheets): Currencies - EUR, USD, GBP

**How to Select**:
1. For each axis, tick the values you need
2. System calculates total combinations
3. Preview shows report cells to be created

**Example**: 3 asset types × 2 maturities × 2 currencies = 12 report cells

**Tips**: Select only what you need. More selections = more combinations = longer processing.

---

### Step 4: Organize Your Variables

Group variables by type to make mapping easier.

**Three Variable Types**:

**Dimensions** - Categories that classify data
- Examples: Country, Currency, Instrument Type, Date
- Usually need value mappings (EUR → Euro)

**Observations** - Actual measured values
- Examples: Amount, Quantity, Balance, Count
- Typically numbers to be reported

**Attributes** - Additional information
- Examples: Status flags, Confidentiality markers, Quality indicators
- Provide metadata about the data

**Process**:
- System suggests groupings automatically
- Review and adjust if needed
- Give each group a clear name
- These become separate mapping sets

**Tips**: Use descriptive names like "Account_Dimensions" not "Group1". Accept suggested groupings unless you have specific needs.

---

### Step 5: Create the Mappings

Define exactly how source data maps to target report fields.

**The Interface**: One tab for each variable group from Step 4.

**For Each Target Variable**:

**1. Select Source Variable**
- Choose matching field from your source data
- Example: Your "GL_ACCOUNT" → Report's "INSTRUMENT_TYPE"

**2. Add Transformation** (if needed)
- Leave blank for direct copy
- Add formula for calculations
- Examples: Convert currency, apply text functions, conditional rules

**3. Map Member Values** (for dimensions)
- Click "Add Member Mapping"
- Match source codes to report codes
- Example: Your "001" → Report "LOANS"

**Common Transformations**:
- Scale amounts: `source_amount / 1000` (report in thousands)
- Convert text: Change case or format
- Conditional logic: Different outputs based on value
- Combine fields: Add multiple sources

**Tips**: Work through one tab at a time. Start with simple direct mappings. System auto-saves your work.

---

### Step 6: Review and Name

Check all mappings and give them meaningful names.

**Review Checklist**:
- Total mapping sets created
- Total variable mappings
- Total member mappings
- All names clear and descriptive

**Naming Mappings**:

System suggests: `F_01_01_Group_1_20250117`

Change to: `F_01_01_GL_to_FINREP_Dimensions`

**Good Names Include**:
- Table reference (F_01_01)
- Purpose (GL_to_FINREP)
- Type (Dimensions, Amounts, Attributes)

**Validation**:
1. Click **"Validate All Mappings"**
2. Fix any errors shown
3. Address warnings
4. Green checkmarks = ready

**Tips**: Use consistent naming across your organization. Include dates for multiple versions.

---

### Step 7: Generate Everything

Create all structures in the database.

**Before Generating**:
Review the summary:
- Number of mappings to create
- Variable connections
- Member mappings
- Report cells (combinations)
- Estimated structures

**Generate Process**:
1. Click **"Generate All Structures"**
2. Confirm you're ready
3. Wait for progress bar (10-60 seconds)
4. Review results

**Success Screen Shows**:
- ✓ Mappings created
- ✓ Variables mapped
- ✓ Member mappings added
- ✓ Report structure built
- ✓ All connections made

**Next Actions**:
- **View Mappings**: Check created mappings
- **Test Execution**: Run test to verify
- **Create Another**: Start new mapping
- **Return to Dashboard**: Go back to main menu

**Tips**: Generate during quiet times for large mappings. Verify immediately after generation. Run a test before full execution.

---

## Complete Example: FINREP Balance Sheet

**Step 1**: Framework: FINREP, Version: 3.0, Table: F_01_01 (Balance Sheet - Assets)

**Step 2**: Found 1 old mapping, deleted to start fresh

**Step 3**: Selected 10 asset types × 5 maturities × 3 currencies = 150 report cells

**Step 4**: Created 3 groups:
- Dimensions: 8 variables (Country, Currency, Instrument, etc.)
- Amounts: 2 variables (Balance, Transaction Count)
- Flags: 3 variables (Status, Confidentiality, Quality)

**Step 5**: Created mappings:
- GL_COUNTRY → COUNTRY (27 member mappings)
- GL_CURRENCY → CURRENCY (5 member mappings)
- GL_ACCOUNT → INSTRUMENT (150 mappings)
- GL_BALANCE → AMOUNT (transformation: divide by 1000)
- TRANSACTION_COUNT → QUANTITY (direct)
- RECORD_STATUS → STATUS (A→Active, I→Inactive)

**Step 6**: Renamed to:
- `F_01_01_GL_to_FINREP_Dimensions`
- `F_01_01_Balance_Amounts`
- `F_01_01_Status_Flags`

**Step 7**: Generated in 15 seconds - 3 mapping sets, 13 variable mappings, 187 member mappings

---

## Best Practices

### Planning
- Map requirements on paper first
- List all source-to-target matches
- Prepare member mappings in advance
- Understand transformations before starting

### Variable Grouping
- Keep related variables together
- Separate dimensions from amounts
- Don't create too many groups (3-5 typical)
- Use clear, searchable names

### Creating Mappings
- Start with direct mappings
- Test transformations before applying
- For large code lists, use spreadsheet first
- Document complex logic

### Naming Convention
- Include table reference
- Add descriptive purpose
- Keep under 100 characters
- Use underscores, not spaces
- Example: `TableCode_Source_to_Target_Type`

---

## Troubleshooting

**Can't see source table**: Verify data is imported, check correct framework, confirm table in database

**Dropdowns not loading**: Refresh page, check network connection, verify previous selection made

**Too many combinations warning**: Reduce ordinate selections, consider if all necessary, split into smaller mappings

**Member mapping not saving**: Check both values selected, verify dimension type, try refreshing

**Generation fails**: Review error message, check required fields mapped, verify source variables exist

**Validation errors**: Read error messages, go back to relevant step, fix issues, re-validate

---

## Common Questions

**Q: Can I edit mappings after creation?**
A: Yes, return to Step 2 and choose "Continue (Regenerate)" to update.

**Q: What if I make a mistake?**
A: Use "Back" button to previous steps, or delete and recreate if already generated.

**Q: How to handle large code lists (100+ mappings)?**
A: Prepare in spreadsheet first, then consider bulk upload in Step 5.

**Q: What happens to unmapped source values?**
A: They typically result in null/empty output. Add default mapping or transformation to handle.

**Q: How long does generation take?**
A: Usually 10-60 seconds. Large mappings with thousands of combinations may take longer.

---

## Quick Reference

**Access**: Tools > Output Layer Mapping (`/pybirdai/output-layer-mapping/`)

**Time**: 15-45 minutes

**Steps**:
1. Choose Report (Framework, Version, Table)
2. Check Existing (Delete or Update)
3. Select Cells (Axis ordinates)
4. Organize Variables (Dimensions, Observations, Attributes)
5. Create Mappings (Source→Target, Transformations, Members)
6. Review and Name (Validate and name)
7. Generate (Create structures)

**After Completion**:
- View mappings in mapping management
- Test execution before production
- Document for future reference

---

## Conclusion

The Output Layer Mapping Workflow provides a structured approach to creating complex data transformations for regulatory reporting. By following the 7-step process, you can efficiently define how your source data maps to target reporting formats while ensuring accuracy through validation at each stage.

### Next Steps

After completing the Output Layer Mapping workflow, continue with related processes to finalize your custom DPM structures. Review the [DPM Workflow Guide](user-guide/dpm-workflow-guide.html) to understand the complete 3-step process that leads to this mapping subworkflow and how it integrates with the main workflow. Return to the [Workflow Dashboard Guide](user-guide/workflow-dashboard-guide.html) to explore other available workflows and understand how output layer mapping fits into your broader regulatory reporting strategy.

### Support Resources

- Eclipse EFBT Wiki: https://github.com/eclipse/efbt/wiki
- Getting Started: https://github.com/eclipse-efbt/efbt/wiki/Getting-Started-with-PyBIRD-AI
- Technical Support: https://github.com/eclipse/efbt/issues
- Community Chat: [Eclipse Chat](https://chat.eclipse.org/#/room/%23technology.efbt:matrix.eclipse.org)
- Email: [efbt-dev@eclipse.org](mailto:efbt-dev@eclipse.org)

**Remember**: Take your time, plan ahead, and validate at each step. Good mappings save hours of debugging later!
