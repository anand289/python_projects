def find_hacker(logs):
    frequency = {}
    for i in logs:
        if i in frequency.keys():
            frequency[i] += 1
        else:
            frequency[i] = 1

    for i in frequency.keys():
        if frequency[i] == 1:
            emp_id = i

    return emp_id

logs = [4,4,5,15,10,3,3,2,2]
print(find_hacker(logs))