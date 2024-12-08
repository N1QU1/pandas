import time

#wrapper function
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + "took " +  str((end-start)) + " sec")
        return result
    return wrapper

#@time_it
def calc_square(numbers):
    #start = time.time()
    result = []
    for number in numbers:
        time.sleep(0.2)
        result.append(number * number)
        print(result)
    #end = time.time()
    #print("calc_square took " + str((end - start)*1000) + " mil sec")
    return result

#@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        time.sleep(0.2)
        result.append(number * number * number)
        print(result)
    return result

print(calc_square([1, 2, 3, 4]))
print(calc_cube([1, 2, 3, 4]))