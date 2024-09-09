import threading
import time

def task1():
    for i in range(5):
        print(f"Task 1 - {i}")
        time.sleep(1)

def task2():
    for i in range(5):
        print(f"Task 2 - {i}")
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
