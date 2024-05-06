#пример использования синхронного выполнения кода
import time
def count_down(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)

count_down(5)
