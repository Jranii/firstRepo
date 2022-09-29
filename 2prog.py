a=int(input("enter a consume unit "))
Base_charge=150
if(a<=100):
    UCC=2.50*a
elif(100<a<=250):
    UCC=2.50*100+4.50*(a-100)
elif(250<a<=400):
    UCC=2.50*100+4.50*(250-100)+6.00*(a-250)
elif(400<a<=600):
    UCC=2.50*100+4.50*(250-100)+6.00*(400-250)+8.50*(a-400)
else:
    UCC=2.50*100+4.50*(250-100)+6.00*(400-250)+(600-400)*8.50+(a-600)*10.00
Bill=Base_charge+UCC
print("Bill=",Bill)
