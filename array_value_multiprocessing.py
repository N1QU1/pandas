import multiprocessing

#result = []
#no puedo usar funciones complejas con un array de multiprocesos.
def calc_square(numbers, result, v):
    v.value = 2.2
    for idx,n  in enumerate(numbers):
        result[idx] = (n**2)
    print(v.value)
    print('inside process ' + str(result[:]))

if __name__ == '__main__':
    numbers = [2,3,4]
    result = multiprocessing.Array('i', 3)
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calc_square, args=(numbers,result,v))

    p.start()
    p.join()
    print('outside process ' + str(result[:]))
    print('outside process ' + str(v.value))