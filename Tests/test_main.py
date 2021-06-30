# def flip(d, a):
#     if d == 'R':
#         a.sort()
#     elif d == 'L':
#         a.sort(reverse=True)
#     return a

# print(flip('R', [3, 2, 1, 2]))

# def remove_exclamation_marks(s):
#     newStr=""
#     for i in range(0, len(s)):
#         if s[i] != "!":
#             newStr += s[i]
#         else:
#             break
#     return newStr
#
# print(remove_exclamation_marks("Hello World!"))


# def first_non_consecutive(arr):
#     dif = arr[1] - arr[0]
#     if len(arr) > 3:
#
#         if dif != (arr[2] - arr[1]) and (arr[2] - arr[1]) == (arr[3] - arr[2]):
#             dif = (arr[2] - arr[1])
#
#     print(dif)
#     for i in range(0, len(arr) - 1):
#
#         if dif != (arr[i + 1] - arr[i]):
#             return arr[i + 1]
#
# arr=[4,6,7,8,9,11]
# print(arr[:])
# print(first_non_consecutive([4,6,7,8,9,11]))
import math

# def array_madness(a,b):
#     sumSqu = 0
#     sumCub = 0
#
#     for i in a:
#         sumSqu += pow(i, 2)
#     for j in b:
#         sumCub += pow(j, 3)
#
#     print(sumSqu, sumCub)
#     return sumSqu > sumCub
#
# print(array_madness( [1,2,3], [8, 1, 13, 15, 4, 10, 21, 27, 26, 7, 9]))
# # a = [4, 5, 6]
# # print(math.pow(a[0],2))


# lst = [1, 2, 1, 1, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 8, 1, 2, 6, 98, 1, 5, 6, 4]
#
#
# def freqElement(lst):
#     element = 0
#     elCount = 0
#     for i in set(lst):
#
#         if elCount < lst.count(i):
#             element = i
#             elCount = lst.count(i)
#
#     return element
#
# print(freqElement(lst))
# # print("element: ", element)


