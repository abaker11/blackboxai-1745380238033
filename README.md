
Built by https://www.blackbox.ai

---

```markdown
# Code Explainer MCP

## Project Overview
Code Explainer MCP is a versatile tool designed to provide clear and concise explanations of Python code and Snowflake SQL queries in plain English. This project aims to bridge the gap for developers and analysts who seek to understand complex code snippets and queries without deep programming knowledge.

## Installation
To set up the Code Explainer MCP on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/code-explainer-mcp.git
   cd code-explainer-mcp
   ```

2. **Install dependencies**:
   You need Python and pip installed on your system. Install the necessary packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

   *Note: Make sure you have FastMCP and any additional libraries listed in `requirements.txt` file installed.*

## Usage
To start the Code Explainer MCP application, run the following command in your terminal:
```bash
python main.py
```

Once the application is running, you can use the following endpoints to explain SQL queries and Python code:

### Explain SQL Query
To explain a Snowflake SQL query, use the `explain_sql_query` method:
- **Input Parameter**: `query` (string) - The SQL query to explain.
- **Output**: A human-readable explanation of what the query does.

### Explain Python Code
To get a line-by-line explanation of Python code, use the `explain_python_code` method:
- **Input Parameter**: `code` (string) - The Python code snippet to explain.
- **Output**: A detailed explanation in plain English.

## Features
- **SQL Query Explanation**: Understand Snowflake SQL queries with simple English explanations.
- **Python Code Explanation**: Get comprehensive line-by-line insights into Python code snippets.
- **Error Handling**: The application includes error handling to manage exceptions and provide meaningful error messages.
  
## Dependencies
Ensure you have the following dependencies installed for the application to work correctly:

- FastMCP

You can find the complete list of dependencies in the `requirements.txt` file.

## Project Structure
The project directory has the following structure:

```
code-explainer-mcp/
├── main.py               # Main application file
├── explainers.py         # Module containing logic for explaining SQL and Python code
├── requirements.txt      # List of package dependencies
└── mcp.json              # Metadata and function definitions for the project
```

Feel free to contribute to this project by submitting issues or pull requests on GitHub.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
```

This README provides a comprehensive guide to the Code Explainer MCP project, including installation instructions, usage details, features, dependencies, and the project structure.