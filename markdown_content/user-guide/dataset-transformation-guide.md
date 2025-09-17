The Dataset Transformation Process converts regulatory data models into executable transformations for Dataset reporting, ensuring compliance with ECB (European Central Bank) analytical credit data requirements.

## Access Dataset Transformation

To access Dataset Transformation, launch the FreeBIRD Application, navigate to the Home page, and click on **"Dataset Transformation"**. You will then follow a 4-step sequential process.

![Dataset Transformation Process](images/screenshots/dataset/dataset_do.png)

## 4-Step Dataset Workflow

The Dataset workflow consists of four sequential steps that must be executed in order: Fetch Metadata CSV, Import Metadata, Create Joins, and Generate Code.

### Step 0: Fetch Metadata CSV

Click "Step 0: Fetch Dataset CSV" to download the latest Dataset specifications from the ECB. This step retrieves the current CSV files containing the Dataset data model definitions. The system will download and store these files locally, making them ready for the import process.

### Step 1: Import Metadata

Click "Step 1: Import Metadata" to process the downloaded CSV files and import the Dataset data model into your system. During this step, the system validates the CSV data, creates the necessary database structures, and imports all Dataset specifications. Once complete, your data model will be ready for join creation.

### Step 2: Create Joins Metadata

Click "Step 2: Create Joins Metadata" to analyze the imported data model and generate join specifications. The system examines the relationships between different data elements and creates metadata that defines how these elements should be connected. This metadata forms the foundation for the executable code generation in the next step.

### Step 3: Create Executable Joins

Click "Step 3: Create Executable Joins" to convert the join metadata into executable Python code. This final step transforms the abstract join specifications into concrete Python scripts that can process actual data. The generated code will be optimized and ready for production use in your regulatory reporting pipeline.

## Best Practices

Always execute the four steps in sequential order from Step 0 through Step 3. Complete each step fully before proceeding to the next one. Verify your internet connectivity before attempting to fetch data from the ECB. Monitor the import validation results to ensure data accuracy. Review the generated join metadata to confirm proper relationships are established. Test the generated Python code thoroughly before deploying it to production.

## Troubleshooting

If you're unable to fetch CSV files from the ECB, verify your internet connectivity and firewall settings, check if the ECB repository is available, and review your proxy settings if applicable. When import failures occur, validate that the CSV files are complete and properly formatted, check your database connectivity and permissions, and review the import logs for specific error messages. If join metadata generation produces incorrect relationships, verify that the import step completed successfully, check for any data model inconsistencies, and ensure you're using the latest ECB specifications. For code generation problems, confirm that the join metadata was created properly, check your Python environment and required dependencies, and review the code generation logs for detailed error information.

## Compliance and Integration

Maintaining ECB compliance requires staying current with specification updates and regulatory requirement changes. The system provides audit trails for supervision purposes. You can integrate Dataset transformation with your broader workflow dashboard, connect it to core banking systems for source data, link it to regulatory submission platforms, and incorporate it into your data governance framework. For advanced usage, consider setting up automated scheduling for regular ECB data fetching, implementing institution-specific validation rules, and optimizing the generated code for your specific data volumes and environment.
