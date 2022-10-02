class calculator(): 
    def sum(a,b): 
        return a+b 
    def subtract(a,b): 
        return a-b 
    def multiply(a,b): 
        return a*b 
    def divide(a,b): 
        return (a/b) 
x=int(input("Enter the first value: ")) 
y=int(input("Enter the second value: ")) 
print("The sum is:",calculator.sum(x,y)) 
print("Difference is:",calculator.subtract(x,y)) 
print("Multiplication is:",calculator.multiply(x,y)) 
print("Division is:",calculator.divide(x,y))
