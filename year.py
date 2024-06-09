def is_year_leap(n):
    if n % 4 == 0:
        return True
    else:
        return False

m = int(input('Введите год: '))

print(is_year_leap(m))