num = int(input("Enter your number:"))
dest = num
sum = 0
n = len(str(num))

# i referenced this code from mygreatlerning.com
while num > 0:
    digit = num % 10
    sum += digit ** n
    num //= 10

if sum == dest:
    print(dest, "is an armstrong number.")

else:
    print(dest, "is not an armstrong number.")

