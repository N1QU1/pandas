import multiprocessing

#result = []
#no puedo usar funciones complejas con un array de multiprocesos.

def calc_square(numbers,queue):
    #global result
    for n  in numbers:
        queue.put(n**2)

    print('inside process ' + str(queue))

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=calc_square, args=(numbers,queue))
    p.start()
    p.join()

    while queue.empty() is False:
        print(queue.get())