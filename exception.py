x = input("Give me a number: ")
try:
   plus3 = int(x) + 3
except Exception as e:
    print("Efectivamente eres tonto")
    plus3 = None
print(plus3)