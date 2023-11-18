
i = int(input())  
j = int(input())  
k = int(input())  
n = int(input())  

coordinates = [
    [x, y, z]
    for x in range(i + 1)
    for y in range(j + 1)
    for z in range(k + 1)
    if x + y + z != n
]

print(coordinates)
