# student_solution.py

# ---------- ЗАДАНИЕ 1 ----------
def task1(s):
    # s — строка вида "подстрока1,подстрока2"
    # вернуть кортеж: (len(sub1) > len(sub2), sub1==sub2, sub2 in sub1)
    ...

# ---------- ЗАДАНИЕ 2 ----------
def task2(s):
    # s — любая строка
    # вернуть кортеж:
    # (s.strip(), len(s), s.count('a'), s.replace('a','@'), s.istitle())
    ...
    s = input()
    result1 = s.strip()
    print(result1)
    result2 = len(s)
    print(result2)
    result3 = s.count('a')
    print(result3)
    result4 = s.replace('a', '@')
    print(result4)
    result5 = s.istitle()
    print(result5)

# ---------- ЗАДАНИЕ 3 ----------
def task3(s):
    # s — строка
    # вернуть кортеж: (без первого и последнего символа, каждый второй символ, строка.lower() в обратном порядке)
    ...
    s = input("")
    result1 = s[1:-1]
    result2 = s[::2]
    result3 = s[::-1].lower()
    print("без первого и последнего символа:", result1)
    print("каждый второй символ строки:", result2)
    print("в обратном порядке:", result3)

# ---------- ЗАДАНИЕ 4 ----------
def task4(nums):
    # nums — список чисел
    # вернуть кортеж: (отсортированный список, сумма, (min, max))
    ...
    
    numbers_str = input("Введите числа через пробел: ")
    numbers = list(map(int, numbers_str.split()))
    sorted_numbers = sorted(numbers)
    total_sum = sum(numbers)
    min_number = min(numbers)
    max_number = max(numbers)
    print("Отсортированный список:", sorted_numbers)
    print("Сумма всех элементов:", total_sum)
    print("Минимальное число:", min_number)
    print("Максимальное число:", max_number)

# ---------- ЗАДАНИЕ 5 ----------
def task6(s):
    # s — строка
    # вернуть True если палиндром (без учёта регистра) и нет пробелов, иначе False
    ...
    s = input().lower()
    result = s == s[::-1] and ' ' not in s
    print(result)

# ---------- ЗАДАНИЕ 6 ----------
def task7(n):
    # n — целое число
    # вернуть кортеж: (hex(n) без '0x', len(hex), True если 'a' есть в hex)
    ...

# ---------- ЗАДАНИЕ 7 ----------
def task8(month_num):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # вернуть название месяца по номеру (1-12)
    ...
    month_number = int(input())
    if 1 <= month_number <= 12:
        print(months[month_number - 1])
