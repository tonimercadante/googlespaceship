# def solution(data, n):
#     uniqueData = set(data)
#     for i in uniqueData:
#         if data.count(i) > n:
#             data = [t for t in data if t != i]
#     return data

# solution([5, 10, 15, 10, 7], 1)
# ################################################################################################################################################



# def solution(xs):
#     if len(xs) == 1:
#         return str(xs[0])

#     def calc_product(l):
#         p = 1
#         for x in l:
#             p = p * x
#         return p

#     subset = []
#     negatives = []
#     positives = []
#     removedNum = False

#     if 0 in xs:
#         removedNum = True


#     for x in xs:
#         if x < 0:
#             negatives.append(x)
#         else:
#             if x != 0:
#                 positives.append(x)

#     if len(positives) == 0:
#         return str(0)

#     if len(negatives) % 2 != 0:
#         negatives.remove(max(negatives))

#     product_negatives = calc_product(negatives)
#     product_positives = calc_product(positives)
#     result = str(product_negatives * product_positives)
#     return result

# print(solution([2, -3, 1, 0, -5]))
# print(solution([-2, -3, 4, -5]))
# print(solution([2, 0, 2, 2, 0]))
# print(solution([2, 2, 2, 2]))
# print(solution([0,0,0,0,0]))
