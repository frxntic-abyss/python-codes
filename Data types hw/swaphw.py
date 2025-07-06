x = 5
y = 9
z = 1
print("the value of x is", x)
print("the value of y is", y)
print("the value is z is", z)

temp = x
x = z
z = temp
z = y
temp = y
y=x


print("the value of x after swapping is", x)
print("the value of y after swapping is", y)
print("the value of z after swapping is", z)