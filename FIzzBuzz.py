def FizzBuzz(min, max):
    for i in range(min, max+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)

def FizzBuzz2(min, max):
    for i in range(1, 101):
        text = ""
        if i%3==0:
            text+="Fizz"
        if i%5==0:
            text+="Buzz"
        if text !="":
            print(i)
        else:
            print(text)
