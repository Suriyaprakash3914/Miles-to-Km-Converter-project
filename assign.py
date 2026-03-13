# s = 'MaNgO'
# d = {}
# for i in range(len(s)):
#     key = i
#     value = s[i].swapcase()
#     d[key] = value
# print(d)

#____________________or__________________________

# s = 'MaNgO'
# d = {}
# for i,j in enumerate(s):
#     key = i
#     value = j.swapcase()
#     d[key] = value
# print(d)

#===============================================

# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# s = []
# i = 0
# res = 0
# while i < len(lst):
#     if i % 2 == 0:
#         res = lst[i] + 1
#     else:
#         res = lst[i] + 3
#     s.append(res)
#     i = i+1
# print(s)

#______________________or_________________________

# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# res = []
# for i,j in enumerate(lst):
#     if i % 2 == 0:
#         res.append(j+1)
#     else:
#         res.append(j+3)
# print(res)




#===============================================

# lst = ['apple', 'orange', 'mango', 'grapes']
# d = {}
# for i, word in enumerate(lst):
#     first_half = word[:len(word) // 2]
#     second_half = word[len(word) // 2:]
#     if i % 2 == 0:
#         key = first_half[::-1]
#         value = second_half
#     else:
#         key = first_half
#         value = second_half[::-1]
#     d[key] = value
# print(d)

#===============================================

# s = 'python is a beautiful programming language'
# lst = []
# for i, n in enumerate(s):
#     if i % 3 == 0 and n != ' ':
#         lst.append(n)
# print(lst)

#===============================================

# lst = ['apple', 'orange', 'mango', 'grapes']
# d = {}
# for i, word in enumerate(lst):
#     key = i
#     rev = word[::-1]
#     value = (word, rev)
#     d[key] = value
# print(d)

#===============================================

# WAP TO CREATE A DICT WITH KEY FROM STRING AND VALUE FROM A LIST

# s = 'abcd'
# lst = ['apple', 'bat', 'cat', 'dog']
# d = {}
# for i in range(len(s)):
#     key = s[i]
#     value = lst[i]
#     d[key] = value
# print(d)

#=================================================

#WAP TO CREATE A NEW LIST WITH THE PRODUCT OF THE ELEMENT PRESENT IN SECOND LIST IN THE SAME Index

# lst1 = [1, 2, 3, 4]
# lst2 = [5, 6, 7, 8]
# lst3=[]
# for i, j in zip(lst1,lst2):
#     lst3.append(i*j)
# print(lst3)

#==================================================

#WAP TO CREATE 2 DICT FROM 3 LIST WITH KEY FROM 1ST LIST AND VALUES FROM REMAINING

# lst1 = ['a', 'b', 'c', 'd']
# lst2 = [1, 2, 3, 4]
# lst3 = ['apple', 'bat', 'cat', 'dog']
# d = {}
# d1 = {}
# for i, j, k in zip(lst1, lst2, lst3):
#     d[i] = j
#     d1[i] = k
# print(d)
# print(d1)

#=======================================================
