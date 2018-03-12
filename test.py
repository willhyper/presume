from presume import presume, then
import time

n = [0]  # mutable


@presume(KeyboardInterrupt, action=print, args=('use pickle.load to restore status',))
@presume(KeyboardInterrupt, action=then.save, args=('temp', n))
def main():
    global n
    while True:

        time.sleep(1)
        n[0] += 1
        print(n)

main()