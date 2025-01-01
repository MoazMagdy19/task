def apply_operations(operations):
    result = 0  
    for op in operations:
        if op == "++":
            result += 1  
        elif op == "--":
            result -= 1  
    return result  

operations = ["++", "++", "--", "++"]
print(apply_operations(operations))  
