import numpy as np

# 1. Створюємо масив з 200 випадкових чисел від -100 до 100
arr = np.random.randint(-100, 101, 200)

print("Початковий масив:")
print(arr)

# 2. Маска для додатніх чисел
positive_mask = arr > 0
positive_numbers = arr[positive_mask]

print("\nДодатні числа:")
print(positive_numbers)
