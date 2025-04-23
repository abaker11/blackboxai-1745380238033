from typing import Dict, List

def _analyze_sql_parts(query: str) -> Dict[str, bool]:
    """Analyze SQL query parts to determine which clauses are present."""
    upper_query = query.upper()
    return {
        "select": "SELECT" in upper_query,
        "from": "FROM" in upper_query,
        "where": "WHERE" in upper_query,
        "group_by": "GROUP BY" in upper_query,
        "having": "HAVING" in upper_query,
        "order_by": "ORDER BY" in upper_query,
        "join": any(join in upper_query for join in ["JOIN", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN"]),
        "limit": "LIMIT" in upper_query
    }

def explain_sql(query: str) -> str:
    """
    Generate a plain English explanation of a Snowflake SQL query.
    
    Args:
        query: The SQL query string to explain
        
    Returns:
        A human-readable explanation of what the query does
        
    Raises:
        ValueError: If the query is empty or invalid
    """
    if not query.strip():
        raise ValueError("SQL query cannot be empty")
    
    parts = _analyze_sql_parts(query)
    explanations: List[str] = []
    
    # Build the explanation based on query parts
    if parts["select"]:
        explanations.append("This query retrieves data")
        
    if parts["from"]:
        explanations.append("from one or more tables")
        
    if parts["join"]:
        explanations.append("and combines it with related data from other tables")
        
    if parts["where"]:
        explanations.append("filtering for specific conditions")
        
    if parts["group_by"]:
        explanations.append("then groups the results")
        
    if parts["having"]:
        explanations.append("applying additional filters to the grouped data")
        
    if parts["order_by"]:
        explanations.append("and sorts the output")
        
    if parts["limit"]:
        explanations.append("returning a limited number of rows")
    
    # Combine all parts into a coherent explanation
    explanation = " ".join(explanations)
    return f"{explanation}." if explanation else "Unable to explain this SQL query structure."
