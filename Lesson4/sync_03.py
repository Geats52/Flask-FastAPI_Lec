import random
import time

def long_running_task():
    for i in range(5):
        print(f"Выполнение задачи {i}")
        time.sleep(random.randint(1, 3))

def main():
    print("Начало программы")
    long_running_task()
    print("Конец программы")

main()
