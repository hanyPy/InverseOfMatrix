# Inverse of a 3x3 matrix
#26 February 2023 - 27 February 2023
# Cleaned up code on 3rd March, 2023.

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))
num4 = float(input("Enter a number: "))
num5 = float(input("Enter a number: "))
num6 = float(input("Enter a number: "))
num7 = float(input("Enter a number: "))
num8 = float(input("Enter a number: "))
num9 = float(input("Enter a number: "))

#Finding the deteriminant
lo = ((num1)*(num5)*(num9)-(num8)*(num6)) - ((num2)*((num4)*(num9)- (num7)*(num6))) + ((num3)*(((num4)*(num8)) - ((num7)*(num5))))




c11 = (pow(-1, 2))*((num5)*(num9)-(num8)*(num6))
c12 = (pow(-1, 3))*((num4)*(num9)-(num7)*(num6))
c13 = (pow(-1, 4))*((num4)*(num8)-(num7)*(num5))
c21 = (pow(-1, 3))*((num2)*(num9)-(num8)*(num3))
c22 = (pow(-1, 4))*((num1)*(num9)-(num7)*(num3))
c23 = (pow(-1, 5))*((num1)*(num8)-(num7)*(num2))
c31 = (pow(-1, 4))*((num2)*(num6)-(num5)*(num3))
c32 = (pow(-1, 5))*((num1)*(num6)-(num4)*(num3))
c33 = (pow(-1, 6))*((num1)*(num5)-(num4)*(num2))


num1 = c11/lo
num4 = c21/lo
num7 = c31/lo
num2 = c12/lo
num5 = c22/lo
num8 = c32/lo
num3 = c13/lo
num6 = c23/lo
num9 = c33/lo


Inverse = [num1 , num4 , num7]
inverse2 = [num2 , num5 , num8]
inverse3 = [num3 , num6 , num9]

print(Inverse)
print(inverse2)
print(inverse3)