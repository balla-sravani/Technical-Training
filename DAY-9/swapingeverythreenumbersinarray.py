'''
#input:[4,9,8,2,14,3,5,6]
#       4 8 9 2 14 3 5 6
#         2 8 9 14 3 5 6
#           8 9 14 3 5 6
#             3 9 14 5 6
#               5 9 14 6
#                 6 9 14
#output:4 2 8 3 5 6 9 14
'''

a=[4,9,8,2,14,3,5,6]
for i in range(len(a)-2):
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
    if(a[i+1]>a[i+2]):
        a[i+1],a[i+2]=a[i+2],a[i+1]
    if(a[i]>a[i+1]):
       a[i],a[i+1]=a[i+1],a[i]
print(a)
        
    
    