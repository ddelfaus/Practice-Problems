#Plan
# there are 3  acctions to take
# if 1 append x to collection
#if 2 delete y from the collection
#if 3 check the occurance of z from  the collection
#first pass solution too slow need to take out the coutner and required frequency with a different dictnary



def frequencyQueries(queries):
    # collection = []
    # output = []
    # for task in queries:
    #     if task[0] == 1:
    #         collection.append(task[1])
    #     elif task[0] == 2:
    #         if task[1] in collection:
    #             collection.remove(task[1])
    #     elif task[0] == 3:
    #         counted_dict= dict(Counter(collection))

    #         if task[1] in counted_dict.values():
    #             output.append(1)
    #         else:
    #             output.append(0)
    # return output

     count = dict()
    result = list()
    for q in queries: 
        if q[0] == 1:
            try:
                count[q[1]] += 1
            except:
                count[q[1]] = 1

        elif q[0] == 2:
            try:
                count[q[1]] -= 1
                if count[q[1]] == 0:
                    del count[q[1]]
            except:
                continue
        
        else:
            if q[1] in set(count.values()):
                result.append('1')
            else:
                result.append('0')
    return result



    print(collection)
    print(queries)