def pascal_triangle(n):
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    for i in range(1, n):
        # Get the previous row
        prev_row = triangle[-1]
        # Initialize the current row
        current_row = [1]
        
        # Calculate the values for the current row
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])
        
        # Add the last 1 in the current row
        current_row.append(1)
        
        # Add the current row to the triangle
        triangle.append(current_row)
    
    return triangle
