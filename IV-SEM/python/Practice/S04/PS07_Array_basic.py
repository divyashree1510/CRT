
li = [12,25.4,6+5j,"Hello",12,25.4]
print(li,type(li))
print(li[3])
print(li[3:6:1])
print(li[::-1])
print(len(li))
li.append(100)
print(li)
li.insert(2,"World")
print(li)
'''read a number from  the user and display no of digits in that number'''
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Number of digits:", count)