from partition import partition as partition
import time, random

def main():
    times = {}
    count = 10000
    for i in range(0, count+1, 50):
        t = []
        repeat = 20
        for _ in range(repeat):
            start = time.time()
            lst = [1]
            while sum(lst) % 2 == 1:
                lst = [random.randint(1, 10) for _ in range(i+1)]
            partition(lst)
            end = time.time()
            t.append(end - start)
        times[i] = sum(t) / repeat
        print(i, ",", times[i])

if __name__ == "__main__":
    main()