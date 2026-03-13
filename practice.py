#===============reverse a string===================

# s = input("enter a string: ")
# print(s[::-1])

#===============prime or not=======================

# s = int(input("enter the number: "))
# if s > 1:
#     for i in range(2, s):
#         if s % i == 0:
#             print("not prime")
#             break
#         else:
#             print("prime")
#             break
# else:
#     print("not a prime")

#===============fact of number====================

#--------------using for loop---------------------

# no = int(input("enter the number: "))
# fact = 1
# for i in range(1, no+1):
#     fact = fact*i
# print(fact)

#--------------using while loop-------------------

# no = 5
# fact = 1
# while no > 1:
#     fact = fact * no
#     no = no-1
# print(fact)

#--------------using recursion--------------------

# def fact(no):
#     if no == 1:
#         return 1
#     else:
#         return no*fact(no-1)
# print(fact(5))

#===============largest element in list===========

#---------------using inbuilt func----------------

# lst = [3, 8, 1, 5]
# print(max(lst))

#---------------w/o using inbuilt func------------

# lst = [3, 8, 1, 5]
# largest = lst[0]
# for i in lst:
#     if i > largest:
#         largest = i
# print(largest)

#===============minimum element in list===========

#----------w/o using inbuilt method---------------

# lst = [4, 2, 9, 1, 7]
# minimum = lst[-1]
# for i in lst:
#     if i < minimum:
#         minimum = i
# print(minimum)


#====================print 1 to 100 numbers==============

#-------------using recursion----------------------------

# def num(n):
#     if n > 100:
#         return
#     print(n)
#     num(n+1)
# num(1)

#---------------------using while------------------------

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

#---------------------using for--------------------------

# for i in range(1, 101):
#     print(i)

#============remove repeated elements in list============

# lst = [1,1,2,4,6,6,7]
# lt=[]
# for i in lst:
#     if i not in lt:
#         lt.append(i)
# print(lt)

#===========commom values in two list====================

# list1 = [1, 2, 3, 4, 3]
# list2 = [3, 4, 5, 6]
#
# common = []
# for i in list1:
#     if i in list2 and i not in common:
#         common.append(i)
#
# print(common)

#=============reverse a string========================
# def rev(n):
#     if len(n) <= 1:
#         return n
#     else:
#         return rev(n[1:])+n[0]
# print(rev("hai hello"))

#==============nested list to linear list=============

# lst = [1, 2, [3, 4], [5, 6]]
#
# # typecast to string
# s = str(lst)
#
# # remove square brackets and commas
# s = s.replace('[', '').replace(']', '').replace(',', '')
#
# # split by spaces and convert back to int
# linear_list = [int(x) for x in s.split()]
#
# print(linear_list)

#*****************armstrong number*******************

# no = 153
# num = no
# sum = 0
# count = len(str(no))
# while no > 0:
#     rem = no % 10
#     sum = sum+rem**count
#     no = no//10
# if num == sum:
#     print("armstrong number")
# else:
#     print("not a armstrong number")


#*****************fibanacci series*******************

# no = 10
# a,b = 0,1
# for _ in range(no):
#     print(a,end=" ")
#     a,b=b,a+b

#*****************xylem & phloem*********************

# n = input("enter a number: ")
# first = int(n[0])
# last = int(n[-1])
# mid = n[1:-1]
# first_value = first + last
# second = sum(int(i) for i in mid)
# if first_value == second:
#     print("xylem")
# else:
#     print("phloem")

#*****************happy number***********************

# no = 13
# while no > 9:
#     sum = 0
#     while no >0:
#         rem = no%10
#         sum = sum+rem ** 2
#         no = no//10
#     no = sum
# if no == 1:
#     print('happy')
# else:
#     print('not happy')

#****************perfect number**********************

# n = 6
# i = 1
# perfect = 0
# while i < n:
#     if n % i == 0:
#         perfect += i
#     i = i+1
# if perfect == n:
#     print("perfect")
# else:
#     print("not perfect")

#===============second largest number================

# lst = [1, 3, 8, 7, 6, 9]
# first = second = float('-inf')
# for num in lst:
#     if num > first:
#         second = first
#         first = num
#     elif num > second and num != first:
#         second = num
#
# print("Second Largest:", second)

#****************strong number***********************

# no = 145
# temp = no
# sum = 0
# while no > 0:
#     rem = no%10
#     fact = 1
#     while rem > 0:
#         fact = fact * rem
#         rem = rem-1
#     sum = sum + fact
#     no = no//10
# if temp == sum:
#     print("strong number")
# else:
#     print("not a strong number")

#===============count vowels=================

# s = "suriyaprakash"
# vowels = "aeiouAEIOU"
# count = 0
# for i in s:
#     if i in vowels:
#         count +=1
# print(count)

#==============palindrome or not=============

# s = "dad"
# rev = ""
# i = len(s)-1
# while i >= 0:
#     rev += s[i]
#     i -= 1
# if s == rev:
#     print("palindrome")
# else:
#     print("not a palindrome")

#===========sort using w/o sort method==============

# lst = [5, 2, 9, 1, 7]
# n = len(lst)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if lst[j] > lst[j+1]:
#             lst[j],lst[j+1]=lst[j+1],lst[j]
# print("sorted list: ",lst)

#=========merge two list w/o using concatination====

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
#
# merged = []
#
# for i in list1:
#     merged.append(i)
#
# for j in list2:
#     merged.append(j)
#
# print(merged)

#---------sum of digits----------------

# num = int(input("Enter number: "))
# sum = 0
# while num > 0:
#     rem = num % 10
#     num = num // 10
#     sum = rem + sum
# print(sum)


#***********find third maximum***********

# nums = list(map(int, input("Enter numbers: ").split()))
# distinct = list(set(nums))
# distinct.sort(reverse=True)
# if len(distinct) < 3:
#     print("Third maximum does not exist. Output:", distinct[0])
# else:
#     print("Third maximum is:", distinct[2])

#*******************************************


# class sample:
#     def __init__(self, no1, no2):
#         self.a = no1
#         self.b = no2
#     def display(self):
#             print(f'a.....{self.a}\nb.....{self.b}')
# obj1 = sample(30, 40)
# obj2 = sample(300, 400)
# obj1.display()
# print("="*20)
# obj2.display()


#**********************************************

# str1 = "silent"
# str2 = "listen"
#
# if len(str1) == len(str2):
#     if sorted(str1) == sorted(str2):
#         print("anagram")
#     else:
#         print("not an anagram")
# else:
#     print("enter valid length")

#***********************************************

# lst = [1,1,2,3,1,4,3]
# seen = {}
#                                         # for num in lst:
#                                         #     if num in seen:
#                                         #         seen[num] += 1
#                                         #     else:
#                                         #         seen[num] = 1
# for num in lst:
#     seen[num] = seen.get(num, 0) + 1
# for key, value in seen.items():
#     print(f"{key} : {value}")

#****************************************************

# str1 = "banana"
# seen ={}
# for value in str1:
#     if value in seen:
#         seen[value] += 1
#     else:
#         seen[value] = 1
# for key,value in seen.items():
#     print(f"{key}:{value}")
# print(f"total number of character : {len(str1)}")

#******************************************************

#Write a function that returns the sum of all elements in a list.

# def sum_of_list(numbers):
#     return sum(numbers)
# mylist = [1,2,3,4,5,6]
# print(sum_of_list(mylist))

#********************************************************


#Rotate right by k positions

# def rotate_list(lst, k):
#     n = len(lst)
#     k = k % n
#     return lst[-k:] + lst[:-k]
# lst = [1,2,3,4,5,6]
# print(rotate_list(lst, 3))

#*******************************************************

#Write a function that returns the common elements between two lists?

# def common_element(lst1, lst2):
#     result = []
#     for items in lst1:
#         if items in lst2 and items not in result:
#             result.append(items)
#     return result
# print(common_element([1,2,3,4,5], [3,4,5,6,7,8]))

#*******************************************************

#Write a function to find the GCD of two numbers?

# def gcd(a, b):
#     while b!=0:
#         a, b = b, a % b
#     return a
# print(gcd(48, 18))

#**********using in-built function************************

# import math
#
# def gcd(a, b):
#     return math.gcd(a, b)
# print(gcd(48,18))

#*********************************************************

#Write a function to flatten a nested list?

# def flatten(lst):
#     result = []
#     for item in lst:
#         if isinstance(item, list):
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#     return result
#
# nested = [1, [2, 3], [4, [5, 6]], 7]
# print(flatten(nested))


#*************************************************************

#Build a password strength checker?

# import string
#
# def check_password_strength(password):
#     if len(password) < 8:
#         return "Weak (Too short)"
#
#     has_upper = any(c.isupper() for c in password)
#     has_lower = any(c.islower() for c in password)
#     has_digit = any(c.isdigit() for c in password)
#     has_special = any(c in string.punctuation for c in password)
#
#     score = sum([has_upper, has_lower, has_digit, has_special])
#
#     if score == 4:
#         return "Strong"
#     elif score == 3:
#         return "Medium"
#     else:
#         return "Weak"
# print(check_password_strength("Suriya@2003"))

#***************************************************************
# n = 5
# num = 1
# for i in range(1, n+1):
#     print()
#     for j in range(1, n+1):
#         print(f"{num: 02d}", end=" ") #num:3d
#         num += 1

#****************************************************************

# nums = [500012368, 2316766232, 61234254252, 815211123682, 7]
#
# first = second = third = None
#
# for n in nums:
#     # skip duplicates
#     if n == first or n == second or n == third:
#         continue
#
#     if first is None or n > first:
#         third = second
#         second = first
#         first = n
#     elif second is None or n > second:
#         third = second
#         second = n
#     elif third is None or n > third:
#         third = n
#
# if third is None:
#     print("Less than 3 unique numbers")
# else:
#     print("Third max:", third)

#*****************************

# num = str(input())
# print(int(num,17))

#*****************************

# day = input("Enter a day: ").lower()
# no_of_days = int(input("Enter number of days: "))
# week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
# start_index = week.index(day)
# count = 0
# for i in range(no_of_days):
#     current_day = week[(start_index + i) % 7]
#     if current_day == "sun":
#         count += 1
# print("Number of Sundays:", count)

#*****************************************************

# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# arr.sort()
# for num in arr:
#     print(num, end=" ")


#*****************************************************


# def longestUniqueSubstringLength(s):
#     char_set = set()
#     left = 0
#     max_length = 0
#
#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#
#         char_set.add(s[right])
#         max_length = max(max_length, right - left + 1)
#
#     return max_length
# print(longestUniqueSubstringLength("abcabcbb"))

#***************************************************

# n = int(input("Enter the number: "))
# if n > 1:
#     for i in range(2,n):
#         if n % 2 == 0:
#             print("not prime")
#             break
#         else:
#             print("prime")
#             break
# else:
#     print("not a prime")

#****************************************************

# def subArrayRemoval(nums):
#     seen = set()
#     l = 0
#     max_len = 0
#     for r in range(len(nums)):
#         while nums[r] in seen:
#             seen.remove(nums[l])
#             l += 1
#         seen.add(nums[r])
#         max_len = max(max_len, r - l + 1)
#     return len(nums) - max_len
# print(subArrayRemoval([1,2,1,2,3]))

#*****************************************************

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"{i}-->fizz buzz")
#     elif i % 3 ==0:
#         print(f"{i}-->fizz")
#     elif i % 5 ==0:
#         print(f"{i}-->buzz")

#**************************************************

# s = "hehllo"
# dic = {}
# for i in s:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1
# print(dic)

#***************************************************



while True:
    str1 = input("enter first string: ")
    str2 = input("Enter second string: ")

    val = set()
    if len(str1) == len(str2):
        for ch in str1:
            val.add(ch)
        for i in str2:
            if i not in val:
                print("-1")
                break
        else:
            print("1")
    else:
        print("-1")
    choice = input("Enter yes to continue or no to stop: ")
    if choice.lower() == "no":
        print("stopped")
        break














