
a=int(input("finansmanGelir"))
b=int(input("pazarGelir"))
c=int(input("kiraGelir"))
if a+b+c:
   print("İsletme karı:",a+b+c)

x=int(input("ucret"))
y=int(input("finansmanGider"))
z=int(input("pazarGider"))
t=int(input("kiraGider"))
s=int(input("muhasebeGider"))

if x+y+z+t+s:
    print("isletme gideri",x+y+z+t+s)

if (a+b+c)-(x+y+z+t+s)<=1000:
    print("Zarar edilmiştir.")
else:
    print("Kar edilmiştir.")


 
