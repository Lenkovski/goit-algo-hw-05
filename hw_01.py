def caching_fibonacci():
    cache = {}  # Словник для кешування обчислених значень

    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        # Якщо значення вже є в кеші - повертаємо його
        if n in cache:
            return cache[n]
        
        # Інакше обчислюємо рекурсивно, зберігаємо у кеш і повертаємо
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib(20))  # Виведе 6765