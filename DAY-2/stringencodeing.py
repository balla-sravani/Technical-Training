s=input()
key=int(input())
c=key%26
d=""
for i in s:
    if((ord(i)-c)>=97):
        d=d+chr(ord(i)-c)
    else:
        d=d+chr(ord(i)-c+26)
print(d)
"khoor"
" in a to z compare given String like 1st letter is k and give key is 3 so move 3 steps back from k so it is h next from h move 3 steps back it e like that it will continue "
"3"
"output:hello"

        

