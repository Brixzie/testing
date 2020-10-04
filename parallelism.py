import multiprocessing
import time


list = []



for x in range(1000):
    list.append(1000-x)

def selection_sort(input_list):
    #print('Pre-sorted: ', input_list)
    #start = time.perf_counter()
    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
# Swap the minimum value with the compared value

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
    
    #finish = time.perf_counter()
    #final = finish - start
    #print('Sorted: ', input_list, '\nTime:', final)


start = time.perf_counter()

if __name__ == '__main__': 
    p1 = multiprocessing.Process(target=selection_sort,args=[list])
    p2 = multiprocessing.Process(target=selection_sort,args=[list])
    p3 = multiprocessing.Process(target=selection_sort,args=[list])
    p4 = multiprocessing.Process(target=selection_sort,args=[list])

    start = time.perf_counter()

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    finish = time.perf_counter()
    final = finish - start
    print('\n\nTotal Time:', final)