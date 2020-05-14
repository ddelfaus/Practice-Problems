#plan 
# create a seat and go through string if its not in the set add it and record count
# if it is stop store the count and reset it
#then keep going
#return the max

def lengthOfLongestSubstring( s):

    str_list = []
    max_length = 0

    for x in s:
        if x in str_list:
            str_list = str_list[str_list.index(x)+1:]
           

        str_list.append(x)    
        print(str_list)
        max_length = max(max_length, len(str_list))

    return max_length
    



print(lengthOfLongestSubstring("aabfewaf"))




















#     lengths = []
#     string_set = set()
#     count = 0
#     for character in s:
#         if character not in string_set:
#             string_set.add(character)
#             count += 1
            
#         else: 
#             lengths.append(count)
#             print(lengths)
#             string_set.clear()
#             print(string_set)
#             count = 0
            
            
#     return max(lengths)



# print(lengthOfLongestSubstring(s))



        
#         queue = []
#         lengths = []
#         for character in s:
#             if character not in queue:

#                 queue.append(character)
                    
#             else:
                
#                 lengths.append(len(queue))
#                 queue = []
#                 queue.append(character)
#         lengths.append(len(queue))
#         print(lengths)
        
#         if lengths == []:
#             return len(queue)
#         return max(lengths)
        
#         lengths = []
#         string_set = set()
#         count = 0
#         for character in s:
          
#             if character not in string_set:
                
#                 string_set.add(character)
#                 count += 1
#                 print(count)
#             else: 
#                 lengths.append(count)
#                 string_set.clear()
#                 string_set.add(character)
                
#                 count = 1
                
        
        
#         if lengths:        
#             return max(lengths)
#         if len(string_set) == 1:
#             return 1
#         else:
#             print('test')
#             return 0
                    