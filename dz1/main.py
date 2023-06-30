def palindrom_check(x):
    if x == x[::-1]:
        print(True)
    else:
        print(False)

while 1 == 1:
    palindrom_check(input("Введите слово для проверки на палиндром:"))