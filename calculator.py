
def number():
    while True:
        try:
            x = float(input("enter the number"))
            return x
        except ValueError:
            print("only number")
# number()
#
#
def choice():
    ch = ('+', '-', '/', '*')
    while True:
        try:
            c = input('+, -, /, *' )
            if c not in ch:
                raise Exception
        except Exception:
            print('grir miayn nshvac nshannery')
        else:
            return c
# choice()
#
def result():
    x = number()
    c = choice()
    y = number()
    if c == '+':
        res = x +y
        return f'{x} + {y} = {res}'
    elif c == '-':
        res = x - y
        return f'{x} - {y} = {res}'
    elif c == '*':
        res = x * y
        return f'{x} * {y} = {res}'
    elif c == '/':
        while True:
            try:
                res = x / y
                return f'{x} / {y} = {res}'
            except ZeroDivisionError:
                print('not division')
                y = number()
print(result())






try:
    text = "barev"
    tiv = int("777")
    result = text + tiv
except TypeError:
    print("strign u inetegery chen gumarvum qani vor mi type i chen patkanum")


try:
    print(barev)
except NameError:
    print("barev anuny chi gtnvum")


try:
    x = int("vanik")
except Exception:
    print('integer greluc heto string chi grvum')


try:
    my_dict = {'x': 9, 'y': 7}
    x = my_dict['a']
except KeyError:
    print('dictonary um tenc key chka')


try:
    number1 = 7
    number2 = 0
    result = number1 / number2
except ZeroDivisionError:
    print("tivy chi bajanvum 0i")

