# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def HW_task1():
    num = []
    g = 1
    n = int(input("Enter number: "))
    for i in range(1, n + 1):
        num.append(g)
        g *= i + 1
    print(f"{n} -> {num}")


# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
def HW_task3():
    string1 = input("Enter string1: ")
    string2 = input("Enter string2: ")
    length_string1 = len(string1)
    length_string2 = len(string2)
    count = 0
    for i in range(length_string1):
        for j in range(length_string2):
            if string1[i] == string2[j]:
                count += 1
        print(f"{string1[i]} - {count}", end=" ")
        count = 0


# HW_task3()


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы
# списка на 2 позиции вправо. 3 -> [2, 3, -3, -2, -1, 0, 1]
def HW_task4():
    list = []
    new_list = []
    n = int(input("Enter number N: "))
    step = int(input("Enter step: "))
    for i in range(-n, n + 1):
        list.append(i)
    print(f"list -> {list}")
    for j in range(len(list)):
        n = list[j] + step
        new_list.append(n)
    print(f"\nnew list -> {new_list}")


# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
def HW_task_2():
    print(f"x | y |¬ X V Y")
    for x in range(0, 2):
        for y in range(0, 2):
            print(f"{x} | {y} | {int(not x or y)}")