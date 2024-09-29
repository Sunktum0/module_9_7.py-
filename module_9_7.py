def is_prime(func):
    def it_is_prime(*args):
        result = func(*args)

        # Проверка на простое число
        if result <= 1:
            print('Составное число')
            return result

        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                print('Составное число')
                return result

        print('Простое число')
        return result

    return it_is_prime


@is_prime
def sum_three(*args):
    result = sum(args)  # Можно использовать встроенную функцию sum
    return result


result = sum_three(2, 3, 6)
print(result)  # Результат: 11, и выведется "Простое число"