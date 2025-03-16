# def date_nb_days(a0, a, p) -> str:
#     days = 0
#     while a0 < a:
#         a0 += a0 * p / 36000
#         days += 1
#     start_date = '2016.01.01'
#     start_date = list(map(int, start_date.split('.')))
#
#     while days > 0:
#         if start_date[1] == 12 and start_date[2] == 31:
#             start_date[0] += 1
#             start_date[1] = 1
#             start_date[2] = 1
#         elif start_date[2] == days_in_month(start_date[0], start_date[1]):
#             start_date[1] += 1
#             start_date[2] = 1
#         else:
#             start_date[2] += 1
#         days -= 1
#     return f'{start_date[0]:04d}-{start_date[1]:02d}-{start_date[2]:02d}'
#
#
# def days_in_month(year, month):
#     if month == 2:
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             return 29
#         else:
#             return 28
#     return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
#
#
# print(date_nb_days(100, 150, 2.00))  # --> "2035-12-26" (7299 days)
#
# # a0 -> amount of money
# # a -> money wanted
# # p -> intereset rate % / 360 per day -> p / 36000) -> 0.98% -> 0.0098
# # first day: 1st of January 2016 -> 2016-01-01
#
#
# # print(date_nb_days(100, 101, 0.98))   # --> "2017-01-01" (366 days)
#
# print(date_nb_days(100, 150, 2.00))  # --> "2035-12-26" (7299 days)
from math import floor

#
# def gps(s, x):
#     if len(x) <= 1:
#         return 0
#     # return max([3600.0 * (x[i] - x[i - 1]) / s for i in range(1, len(x))])
#     a = max(x[i] - x[i - 1] for i in range(1, len(x)))
#     return a * 3600.0 / s
#
#
# x = [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]
# s = 15
#
# print(gps(s, x))
# 0.0-0.19, 0.19-0.5, 0.5-0.75, 0.75-1.0, 1.0-1.25, 1.25-1.50, 1.5-1.75, 1.75-2.0, 2.0-2.25

# [45.6, 74.4, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0]


# def partlist(arr):
#     # x = []
#     # for i in range(len(arr)):
#     #     x.append((', '.join(arr[:i+1]))), x.append((', '.join(arr[i+1:])))
#
#     return [(' '.join(arr[:i+1]), ' '.join(arr[i+1:])) for i in range(1, len(arr))]
#
#
#
#

#
# from functools import reduce
# from operator import mul
#
#
# def find_middle(st):
#     if not isinstance(st, str) or not any(c.isdigit() for c in st):
#         return -1
#
#     digits = [int(i) for i in st if i.isnumeric()]
#     if not digits:
#         return -1
#
#     prod = str(reduce(mul, digits))
#     i = (len(prod) - 1) // 2
#     return int(prod[i:-i or len(prod)])

# if len(digits) % 2 == 0:
#     mid_index = len(digits) // 2
#     return reduce(lambda x, y: x * y, digits[mid_index - 1: mid_index + 1])
#     if digits[mid_index - 1] > 0:
#         if str()
#     else:
#         return digits[mid_index]
# else:
#     return reduce(lambda x, y: x * y, digits)


# print(find_middle('101')) # -> 5*6-30
# print(find_middle('{@}x@xy6q39^8@e!8!yl_+@q~>wo$g')) # -> 5*6-30
# print(find_middle('64k_8d3mlxs9z[7-{_{~]x^_np`4`9')) # -> 5*6-30

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

print(solution(15))
