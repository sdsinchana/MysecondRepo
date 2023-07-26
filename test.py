a=int(input("Enter the number:"))
ns=str(a)

#To check whether the number is palindrome or not

if ns==ns[::-1]:
    print("palindrome")
else:
    print("not palindrome")

print("the number is :",a)
print("the reverse ig a number is :",ns[::-1])
print("the sum of num and the reverse is:",a+int(ns[::-1]))