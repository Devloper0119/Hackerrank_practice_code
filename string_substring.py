
"""def count_substring(string, sub_string):

    count = 0  
    for i in range(len(string) - len(sub_string) + 1): 
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count  

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

    """
if __name__ == '__main__':
    print("Enter number")
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result=[]
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    result.append([i,j,k])
    #result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    
  
    print(result)
