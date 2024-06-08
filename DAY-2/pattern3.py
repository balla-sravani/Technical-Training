'''ip:7
 1 1 1 1 1 1 1
 1 2 2 2 2 2 1
 1 2 3 3 3 2 1
 1 2 3 4 3 2 1
 1 2 3 3 3 2 1
 1 2 2 2 2 2 1
 1 1 1 1 1 1 1'''
''
n = int(input())

for i in range(n):
    for j in range(n):
        a = min(i, j, n-1-i, n-1-j) + 1
        print(a, end=" ")
    print()
