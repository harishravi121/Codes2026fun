import random

for i in range(10):
    a=random.randint(10,100);
    b=random.randint(10,100);

    c=bin(a)
    d=bin(b)
    e=a+b
    f=bin(e)
    print(c,'+',d,'=',f)

for i in range(10):
    a=random.randint(10,100);
    b=random.randint(10,100);

    c=hex(a)
    d=hex(b)
    e=a+b
    f=hex(e)
    print(c,'+',d,'=',f)
