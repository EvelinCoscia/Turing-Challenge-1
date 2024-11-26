def calPoints(ops) -> int:
    """
    :type ops: List[str] - List of operations
    :rtype: int -sum of scores after performing all operations
    """
    
    # Initialize an empty List to track scores
    
    record = []
    
    # Process each operation in the input List
    
    for op in ops:
        
        if op == "C":
            record.pop() # Remove the Last score
            
        elif op == "D":
            record.append(2*record[-1]) # Double the Last score
            
        elif op == "+":
            record.append(record[-1] + record[-2]) # Add the Last two scores
            
        else:
            record.append(int(op)) # Add the integer score to the record
            
    # return the sum of the scores
    return sum(record)
    
if __name__ == '__main__':
    line = input("Enter list items separated by spaces: ")
    ops = line.strip().split()
        
    print(calPoints(ops))

   
    