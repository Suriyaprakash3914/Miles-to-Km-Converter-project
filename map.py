# syntax : map(function, iterable)

# def sq(no):
#     return no **2
# lst=[1,2,3,4,5]
# res = map(sq,lst)
# print(res)

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

# n = 28
# i = 1
# perfect = 0
# while i < n:
#     if n % i == 0:
#         perfect += i
#     i = i + 1
# if perfect == n:
#     print("perfect")
# else:
#     print("not perfect")

# n = 28
# perfect = 0
# for i in range(1,n):
#     if n % i/2 == 0:
#         perfect += i
# if perfect == n:
#     print("perfect")
# else:
#     print("not perfect")

# Get matrix size
# n = int(input("Enter matrix size (e.g. 3): "))
#
# print("Enter cards as number,suit (example: 5,H)")
#
# # Read matrix
# matrix = []
# for i in range(n):
#     row = input(f"Row {i+1}: ").split()
#     temp = []
#     for card in row:
#         num, suit = card.split(',')
#         temp.append((int(num), suit))
#     matrix.append(temp)
#
# def steps_to_same(nums):
#     return len(nums) - max(nums.count(x) for x in nums)
#
# max_score = 0
#
# # Check rows
# for row in matrix:
#     nums = [card[0] for card in row]
#     if len(set(nums)) == 1:
#         score = nums[0]
#     else:
#         score = 0
#     max_score = max(max_score, score)
#
# # Check columns
# for c in range(n):
#     nums = [matrix[r][c][0] for r in range(n)]
#     if len(set(nums)) == 1:
#         score = nums[0]
#     else:
#         score = 0
#     max_score = max(max_score, score)
#
# # Check main diagonal
# nums = [matrix[i][i][0] for i in range(n)]
# if len(set(nums)) == 1:
#     max_score = max(max_score, 25)
#
# # Check anti-diagonal
# nums = [matrix[i][n-1-i][0] for i in range(n)]
# if len(set(nums)) == 1:
#     max_score = max(max_score, 25)
#
# print("\nMaximum Score:", max_score)


# no = 5
# fact = 1
# while no > 1:
#     fact = fact*no
#     no = no - 1
# print(fact)

#
# x = 6
# y = x
# x = x+4
# y = y*2
# print(x+y)


# a = 256
# b = 256
# c = 257
# d = 257
# print(a is b)
# print(c is d)





