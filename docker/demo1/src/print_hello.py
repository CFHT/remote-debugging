import threading
import time
import random


def run(value):
    if value == 11:
        print("success")
    else:
        print("fail")


class ThreadExample:
    count = 0
    go = True

    def increment_counter(self):
        def wait():
            time.sleep(random.uniform(0, 1))

        def increment():
            if (random.uniform(0, 1) < 0.5):
                wait()
            self.count += 1
            wait()

        while self.go:
            if self.should_increment():
                increment()

    def should_increment(self):
        return self.count < 100

    def run(self):
        threads = []
        for i in range(10):
            threads.append(threading.Thread(target=self.increment_counter))

        for thread in threads:
            thread.start()

        while self.count < 100:
            pass

        self.go = False
        for thread in threads:
            thread.join(1.0)

        print(self.count)

example = ThreadExample()

if __name__ == "__main__":
    run(11)
    example.run()
