
print("Enter No of Days: ")

N = int(input())

complete_paths = 0

def find_paths(n):
    global complete_paths
    
    if n == N:
        complete_paths += 1
        return 1
         
    p3 = p4 = 0
    
    p1 = find_paths(n+1)
    
    if N-n >=2:
        p2 = find_paths(n+2)
        if N-n >= 3:
            p3 = find_paths(n+3)
            if N-n >= 4:
                p4 = find_paths(n+4)
            else:
                p4 = 1
        else:
            p3 = 1
    else:
        p2 = 1

    res = p1 + p2 + p3 + p4

    return res

total_paths = find_paths(0)

res = str(total_paths-complete_paths) + '/' + str(total_paths)
print(res)
