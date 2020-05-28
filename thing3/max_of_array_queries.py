






#plan
#create empty array for n
#going to add only the first value of the query  to it because were are going to sum it weirdly 
#if the end of the query, query[1] is not the end of it we have to create a gap.
#so the value will be decrement by query[2]

#to find the max add each value and compare it to the max.
#if the value > than the max replace it
#runtime should be O(n)

def maxArrayQueries(n, queries):

    arr = [0]*n
    for query in queries:
        arr[query[0] - 1] += query[2]

        if query[1] != len(arr):
            arr[query[1]] -= query[2]
    max_val = 0
    i = 0

    for q in arr:
        i += q
        if i > max_val:
            max_val = i
    return max_val


print(maxArrayQueries(10, [[1, 2, 100], [2, 3, 100],[3, 4, 100],[10, 10, 100],[10, 10, 100], [10, 10, 100]]))
    # Write your code here


# too slow

#     arr = [0] * n

#     for query in queries:
#         start = query[0] - 1
#         end = query[1]
#         k = query[2]

#         while start < end:
#             print(start)
#             arr[start] += k
#             start = start + 1

    

#     print(arr)


# 






# too slow
# print(queries)
# # arr = [0] * n
# # for query in queries:
# #     start = query[0] - 1
# #     end = query[1]
# #     k = query[2]
# #     while start < end:
# #         arr[start] += k
# #         start += 1
# # max_val = 0
# # for num in arr:
# #     if num > max_val:
# #         max_val = num
# # return max_val
# # for query in queries:
# #     for num in range(query[0], query[1] + 1):
# #         arr[num - 1] += query[2]
# # return max(arr)