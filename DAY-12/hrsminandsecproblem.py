#input:7262 sec  ----- convert into hrs min and sec
#output:2h:1m:2s
a=7262
b=60*60
h=a//b
k=a%b
print("Hours:",h)
m=k//60
print("Minutes:",m)
s=k%60
print("Sec:",s)
print(h,"h:",m,"m:",s,"s")
