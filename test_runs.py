def find_hacker(logs):
    logs_orig = logs.copy()
    for i in range(0,len(logs)):
        logs.pop(i)
        if logs_orig[i] not in logs:
            emp_id = logs_orig[i] 
        logs = logs_orig.copy()
    return emp_id

logs = [4,4,5,10,10,3,3,2,2]
print(find_hacker(logs))