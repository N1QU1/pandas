even = []
numbers = [1,2,3,4,5,6]
"""for ele in numbers:
    if ele % 2 == 0:
        even.append(ele)
"""
even = [i for i in numbers if i%2==0]
print(even)