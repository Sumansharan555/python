# -*- coding: utf-8 -*-
"""list.assignment1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LARNUNhoxYwOAbqGG75UZoJ4XW0AGvpw
"""

# Q1. Program to interchange first and last element in list
l1= [1, 2, 3, 4, 5]
l1[0], l1[-1] = l1[-1], l1[0]
print(l1)

# Q2. Program to swap two element in a list
l1 = [1, 2, 3, 4, 5]
l1[1], l1[2] = l1[2], l1[1]
print(l1)

# Q3. swap elemets in string list
l1 = ["apple", "banana", "cherry"]
l1[0], l1[1] = l1[1], l1[0]
print(l1)

# Q4. Ways to find length of list
# Way 1
l1 = [1, 2, 3, 4, 5]
length = len(l1)
print(length)
# Way 2
l1 = [1, 2, 3, 4, 5]
count = 0
for _ in l1:
    count += 1
print(count)
# Way 3
l1= [1, 2, 3, 4, 5]
length = sum(1 for _ in l1)
print(length)
# Way 4
l1= [1, 2, 3, 4, 5]
length = 0
for _ in l1:
    length += 1
print(length)

# Q5. Maximum of two numbers
num1 = 10
num2 = 5
max_num = max(num1, num2)
print(max_num)

# Q6. Minimum of two numbers
num1 = 10
num2 = 5
min_num = min(num1, num2)
print(min_num)

# Q7.ways to check if element exists in list
l1 = [1, 2, 3, 4, 5]
l1.count(3)
# Way 2
if 3 in l1:
    print("Element exists in the list")
else:
    print("Element does not exist in the list")

# Q8.Different ways to clear list in python
l1 = [1, 2, 3, 4, 5]
# Way 1
l1.clear()
print(l1)

# Way 2
#del l1[:]
print(l1)
# Way 3
#l1.remove()
print(l1)

# Q9. Reversing a list
l1 = [1, 2, 3, 4, 5]
# Way 1
l1.reverse()
print(l1)
# Way 2
l1.sort(reverse=True)
print(l1)

# Q10. cloning or copying a list
l1 = [1, 2, 3, 4, 5]
# Way 1
l1= l1.copy()
print(l1)
# Way 2
new_l1 = l1[:]
print(new_l1)
# Way 3
new_l1 = list(l1)
print(new_l1)

# Q11. count occurences of an element in a list
l1 = [1, 2, 3, 4, 5]
l1.count(3)

# Q12. Program to find sum and average of a list in python
l1 = [1, 2, 3, 4, 5]
sum = l1[0] + l1[1] + l1[2] + l1[3] + l1[4]
average = sum / len(l1)
print(sum)
print(average)

# Q13. sum of number digits in list
l1=[654,1111,444444]
           # separating digits
digits = []
for i in l1:
    for j in str(i):
        digits.append(int(j))
print(digits)
           # adding digits
sum=0
for i in digits:
    sum = sum + i
print(sum)

# Q14. Multiply all numbers in list
l1=[1,2,3,4,5]
product = 1
for i in l1:
    product *= i
print(product)

# Q15. program to find smallest number in list
# Way 1
l1=[1,2,3,4,5]
x=min(l1)
print(x)
# Way 2
y=sorted(l1)
print(y[0])

# Q16.program to find largest number in list
# Way 1
l1=[1,2,3,4,5]
x=max(l1)
print(x)
# Way 2
y=sorted(l1)
print(y[-1])

# Q17. program to find second largest number in list
l1=[1,2,3,4,5]
l1.sort()
print(l1[-2])

# Q18. program to print even numbers in list
l1=[1,2,3,4,5]
for i in l1:
    if i%2==0:
        print(i)

# Q19. program to print odd numbers in list
l1=[1,2,3,4,5]
for i in l1:
    if i%2!=0:
        print(i)

# Q20. program to print all even numbers in a range
for i in range(1,10):
    if i%2==0:
        print(i)

# Q21. program to print all add numbers in a range
for i in range(1,10):
    if i%2!=0:
        print(i)

# Q22. program to count even and odd numbers in a list
l1=[1,2,3,4,5]
even=0
odd=0
for i in l1:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)

# Q23.program to print positive numbers in list
l1=[1,2,3,4,5]
for i in l1:
    if i>0:
        print(i)

# Q24.program to print negative numbers in list
l1=[1,2,3,4,5]
for i in l1:
    if i<0:
        print(i)

# Q25. program to print all positive numbers in a range
for i in range(1,10):
    if i>0:
        print(i)

# Q26. program to print all nagative numbers in a range
for i in range(1,10):
    if i<0:
        print(i)

# Q27. program to count positive and negative numbers in a list
l1=[1,2,3,4,5]
positive=0
negative=0
for i in l1:
    if i>0:
        positive += 1
    else:
        negative += 1
print(positive)
print(negative)

# Q28. remove multiple elements from a list
l1 = [1, 2, 3, 4, 3,1]
for i in l1:
    if l1.count(i)>1:
        l1.remove(i)
print(l1)

# Q29. remove empty tuples from a list
# Way 1
l1 = [(1, 2), (), (3, 4), (), (5, 6)]
l1 = [t for t in l1 if t]
print(l1)
# Way 2
l1 = [(1, 2), (), (3, 4), (), (5, 6)]
l1 = list(filter(None, l1))
print(l1)
# Way 3
l1 = [(1, 2), (), (3, 4), (), (5, 6)]
l1 = [t for t in l1 if t != ()]
print(l1)

# Q30. print duplicates from a list of integers
# Way 1
l1=[1,1,2,2,3,4,4,3,5,5,6]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        print(i)
# way 2
l1=[1,1,2,2,3,4,4,3,5,5,6]
for i in l1:
    if l1.count(i)>1:
        print(i)

