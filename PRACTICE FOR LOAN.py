a=float(input("ENTER THE LOAN AMOUNT="))
b=5
c=(a*(b/100))
print("LOAN KE AMOUNT KA 5%=",c)
d=a-c
print("5% KAT KE LOAN AMOUNT=",d)
# 2% of the amount/ 1st INT
f=(a*(2/100))
g=float(input("ENTER THE MONTH="))
h=f*g
print("2 % into month=",h)
#per month EMI+INT
i=((a+h)/g)
print("PER MONTH EMI=%0.2f"%i)
# 1ST EMI
j=i-f
print("1st EMI %0.2f"%j,"AND INT",f)
#2nd INT
p=float(input("CLIENT NE KITNA EMI DIYA="))
k=a-p
l=(k*(2/100))
m=(l*(g-1))
n=((k+l)/g-1)
o=n-l
print("2nd EMI=%0.2f"%o,"AND INT",l)
# 3rd EMI
q=float(input("CLIENT NE KITNA EMI DIYA="))
r=k-q
s=(r*(2/100))
t=(s*(g-2))
u=((k+l)/g-2)
v=u-s
print("3nd EMI=%0.2f"%v,"AND INT",s)
#4th EMI
q=float(input("CLIENT NE KITNA EMI DIYA="))
r=k-q
s=(r*(2/100))
t=(s*(g-3))
u=((k+l)/g-3)
v=u-s
print("4nd EMI=%0.2f"%v,"AND INT",s)
#5th EMI
q=float(input("CLIENT NE KITNA EMI DIYA="))
r=k-q
s=(r*(2/100))
t=(s*(g-4))
u=((k+l)/g-4)
v=u-s
print("5nd EMI=%0.2f"%v,"AND INT",s)
#6th EMI
q=float(input("CLIENT NE KITNA EMI DIYA="))
r=k-q
s=(r*(2/100))
t=(s*(g-5))
u=((k+l)/g-5)
v=u-s
print("6nd EMI=%0.2f"%v,"AND INT",s)
#7th EMI
q=float(input("CLIENT NE KITNA EMI DIYA="))
r=k-q
s=(r*(2/100))
t=(s*(g-6))
u=((k+l)/g-6)
v=u-s
print("7nd EMI=%0.2f"%v,"AND INT",s)
#8th EMI
q=float(input("CLIENT NE KITNA EMI DIYA="))
r=k-q
s=(r*(2/100))
t=(s*(g-7))
u=((k+l)/g-7)
v=u-s
print("8nd EMI=%0.2f"%v,"AND INT",s)
#9th EMI
q=float(input("CLIENT NE KITNA EMI DIYA="))
r=k-q
s=(r*(2/100))
t=(s*(g-8))
u=((k+l)/g-8)
v=u-s
print("9nd EMI=%0.2f"%v,"AND INT",s)
#10th EMI
q=float(input("CLIENT NE KITNA EMI DIYA="))
r=k-q
s=(r*(2/100))
t=(s*(g-9))
u=((k+l)/g-9)
v=u-s
print("10nd EMI=%0.2f"%v,"AND INT",s)
#11th EMI
q=float(input("CLIENT NE KITNA EMI DIYA="))
r=k-q
s=(r*(2/100))
t=(s*(g-10))
u=((k+l)/g-10)
v=u-s
print("11nd EMI=%0.2f"%v,"AND INT",s)
#12th EMI
q=float(input("CLIENT NE KITNA EMI DIYA="))
r=k-q
s=(r*(2/100))
t=(s*(g-11))
u=((k+l)/g-11)
v=u-s
print("12nd EMI=%0.2f"%v,"AND INT",s)
#13th EMI
q=float(input("CLIENT NE KITNA EMI DIYA="))
r=k-q
s=(r*(2/100))
t=(s*(g-12))
u=((k+l)/g-12)
v=u-s
print("13nd EMI=%0.2f"%v,"AND INT",s)
l=input("THANK YOU")





