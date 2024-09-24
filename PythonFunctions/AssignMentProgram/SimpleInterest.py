def SimpleInterest(price=2000,rate=12,time=1):
    return (price*rate*time)/100


print("Enter Price,Interest,and time :")
price  =  float(input())     # here take input as String and Convert into integer formet
interest = float(input())
time =  float(input())

result = SimpleInterest(price,interest,time)
print("\nSimple Interest is : ",result)
