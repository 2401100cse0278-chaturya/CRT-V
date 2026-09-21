a=10
b=15.5
c="Ram"
d=[1,2,3,4,5,6]
e=(1,2,3,10,45,0)
f={1,2,3,4,5,6}
g={"name":"chaturya"}
print(isinstance(a,int))
print(isinstance(b,float))
print(isinstance(c,str))
print(isinstance(d,list))
print(isinstance(e,list))
print(isinstance(f,set))
print(isinstance(g,dict))

#checking with multiple data types

x="Ram"
if isinstance(x,(int,float)):
    print("x is a number")
else:
    print("x is a string")