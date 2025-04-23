import ast
from typing import List, Optional

def _analyze_line(line: str) -> str:
    """Analyze a single line of Python code and return its explanation."""
    line = line.strip()
    if not line:
        return "Empty line"
    
    # Try to parse as AST to detect basic patterns
    try:
        tree = ast.parse(line)
        node = tree.body[0]
        
        # Function definition
        if isinstance(node, ast.FunctionDef):
            return f"Defines a function named '{node.name}'"
            
        # Class definition    
        elif isinstance(node, ast.ClassDef):
            return f"Defines a class named '{node.name}'"
            
        # Assignment
        elif isinstance(node, ast.Assign):
            return "Assigns a value to a variable"
            
        # Return statement    
        elif isinstance(node, ast.Return):
            return "Returns a value from the function"
            
        # If statement
        elif isinstance(node, ast.If):
            return "Starts a conditional block (if statement)"
            
        # For loop
        elif isinstance(node, ast.For):
            return "Starts a for loop"
            
        # While loop    
        elif isinstance(node, ast.While):
            return "Starts a while loop"
            
    except SyntaxError:
        # Line might be a continuation or incomplete statement
        pass
        
    # Basic keyword detection for cases AST can't handle
    if line.startswith('import '):
        return "Imports a module"
    elif line.startswith('from '):
        return "Imports specific items from a module"
    elif line.startswith('#'):
        return "A comment explaining the code"
    elif 'return' in line:
        return "Returns a value from the function"
    elif 'raise' in line:
        return "Raises an exception"
    elif ':' in line:
        return "Starts a new code block"
    
    return "Performs an operation"  # Generic fallback

def explain_python(code: str) -> str:
    """
    Generate a line-by-line explanation of Python code.
    
    Args:
        code: The Python code snippet to explain
        
    Returns:
        A string containing line-by-line explanations
        
    Raises:
        ValueError: If the code is empty
    """
    if not code.strip():
        raise ValueError("Python code cannot be empty")
    
    lines = code.strip().splitlines()
    explanations: List[str] = []
    
    for i, line in enumerate(lines, 1):
        if line.strip():  # Skip empty lines
            explanation = _analyze_line(line)
            explanations.append(f"Line {i}: {line.strip()}\n   → {explanation}")
    
    return "\n".join(explanations) if explanations else "Unable to explain this Python code."
