a=int(input("Enter the number:"))
ns=str(a)

#To check whether the number is palindrome or not

if ns==ns[::-1]:
    print("palindrome")
else:
    print("not palindrome")