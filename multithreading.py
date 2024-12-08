import threading

from PIL.ImImagePlugin import number

from decorators import calc_cube, calc_square, time_it


@time_it
def parallel_calculations(numbers):

    t1 = threading.Thread(target=calc_cube, args=(numbers,))
    t2 = threading.Thread(target=calc_square, args=(numbers,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

numbers = [2,3,8,9]

parallel_calculations(numbers)
