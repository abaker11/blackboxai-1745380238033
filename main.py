from fastmcp import FastMCP
from explainers import explain_sql, explain_python

app = FastMCP()

@app.tool()  # Fixed: Added parentheses to call the decorator
class CodeExplainer:
    """A tool that explains Python code and SQL queries in plain English"""
    
    async def explain_sql_query(self, query: str) -> str:
        """
        Explains a Snowflake SQL query in plain English.
        
        Args:
            query: The SQL query to explain
            
        Returns:
            A human-readable explanation of what the query does
        """
        try:
            return explain_sql(query)
        except ValueError as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    async def explain_python_code(self, code: str) -> str:
        """
        Provides a line-by-line explanation of Python code.
        
        Args:
            code: The Python code snippet to explain
            
        Returns:
            A line-by-line explanation in plain English
        """
        try:
            return explain_python(code)
        except ValueError as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    app.run()
