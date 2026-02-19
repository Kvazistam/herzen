import random
import math

def calculate_sa(n):
    return sum(math.sin(1 / (i * 5)) for i in range(1, n + 1))

def calculate_sb(n):
    return sum(1 / (i ** 2) for i in range(1, n + 1))

def generate_tests(num_tests, n_min, n_max):
    tests = []
    for _ in range(num_tests):
        n = random.randint(n_min, n_max)
        sa = calculate_sa(n)
        sb = calculate_sb(n)
        
        winner = "Алиса" if sa > sb else "Боб"
        tests.append((str(n), winner, winner))
    print(tests)

# Генерируем 10 тестов с N от 2 до 10^6
generate_tests(10, 2, 10**6)
