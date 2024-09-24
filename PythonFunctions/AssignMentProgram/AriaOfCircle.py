pi = 3.14

def AriaOfCircle(radius):    
        return pi*(radius*radius)




print("Enter Radius of Circle : ")
getValue = int(input())           # Converted String to Integer
print(type(getValue))             # cheking its type after Conversion
result = AriaOfCircle(getValue)    # calling function and passing user argument;
print("Aria Of circle : ",result)