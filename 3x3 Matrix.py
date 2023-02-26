# Inverse of a 3x3 matrix
#26 February 2023 - 27 February 2023

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))
num4 = float(input("Enter a number: "))
num5 = float(input("Enter a number: "))
num6 = float(input("Enter a number: "))
num7 = float(input("Enter a number: "))
num8 = float(input("Enter a number: "))
num9 = float(input("Enter a number: "))

lo = (float(num1)*(float(num5)*float(num9)-float(num8)*float(num6)))   -   (float(num2)*(float(num4)*float(num9)- float(num7)*float(num6)))   +  (float(num3)*(float(num4)*float(num8) - float(num7)*float(num5)))

print("The determinant is: " + str(lo))
matrix = [
    [num1,num2,num3],
    [num4,num5,num6],
    [num7,num8,num9],
]

c11 = (pow(-1, 2))*(float(num5)*float(num9)-float(num8)*float(num6))
c12 = (pow(-1, 3))*(float((num4)*float(num9))- (float((num7)*float(num6))))
c13 = (pow(-1, 4))*(float((num4)*float(num8))- (float((num7)*float(num5))))
c21 = (pow(-1, 3))*(float((num2)*float(num9))- (float((num8)*float(num3))))
c22 = (pow(-1, 4))*(float((num1)*float(num9))- (float((num7)*float(num3))))
c23 = (pow(-1, 5))*(float((num1)*float(num8))- (float((num7)*float(num2))))
c31 = (pow(-1, 4))*(float((num2)*float(num6))- (float((num5)*float(num3))))
c32 = (pow(-1, 5))*(float((num1)*float(num6))- (float((num4)*float(num3))))
c33 = (pow(-1, 6))*(float((num1)*float(num5))- (float((num4)*float(num2))))



num1 = float(c11)/lo
num4 = float(c21)/lo
num7 = float(c31)/lo
num2 =float(c12)/lo
num5 = float(c22)/lo
num8 = float(c32)/lo
num3 = float(c13)/lo
num6 = float(c23)/lo
num9 =float(c33)/lo


Inverse = [num1 , num4 , num7]
inverse2 = [num2 , num5 , num8]
inverse3 = [num3 , num6 , num9]

print(Inverse)
print(inverse2)
print(inverse3)