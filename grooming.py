# s = 'sunday monday tuesday'
# res = ""
# word = ""
# for ch in s[::-1]:
#     if ch != " ":
#         word = ch + word
#     else:
#         res += word + " "
#         word = ""
# res += word
# print(res)

#_______________________________________________________

# s = 'sunday!monday!tuesday'
# print("".join(s[::-1].split("!")))

#-------------------------------------------------------

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} * {j} = {i*j}')
#     print("-----------")

#********************************************************

# def sum_of_factors(n):
#     total = 0
#     for i in range(1, n//2+1):
#         if n % i == 0:
#             total += i
#     return total
# number=12
# if sum_of_factors(number) > number:
#     print("it is abundant number")
# else:
#     print("it is not")



#++++++++++++++++++++++++++++++++++++++++++++++++

# def sum_of_divisors(n):
#     total = 0
#     for i in range(1, n):
#         if n % i == 0:
#             total += i
#     return total
#
# n1, n2 = 6, 28
#
# if sum_of_divisors(n1) / n1 == sum_of_divisors(n2) / n2:
#     print("Friendly pair")
# else:
#     print("Not a Friendly Pair")

#******************************************************

# no = int(input("enter a number: "))
# mul = no * no
# for i in range(1):
#     digit = mul % 10
#     if digit == no:
#         print("it is automorphic number")
#     else:
#         print("not")

#*******************************************************

# no = int(input("enter a number:"))
# temp = no
# sum = 0
# while no > 0:
#     rem = no % 10
#     sum = sum + rem
#     no = no // 10
# if temp % sum == 0:
#     print("it is harshad number")
# else:
#     print("not")

#********************************************************

# no = 28
# temp = no
# sum = 0
# i = 1
# while i < no:
#     if no % i == 0:
#         sum = sum+i
#         i+=1
#     else:
#         pass
# if temp == sum:
#     print("perfect number")
# else:
#     print("not")

