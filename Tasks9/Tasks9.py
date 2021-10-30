import threading
import time


class Philosopher(threading.Thread):
    running = True

    def __init__(self, index, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):

        while self.running:
            time.sleep(5)
            print('philosopher number %s is hungry.\n' % self.index)
            self.diner()

    def diner(self):
        fork1, fork2 = self.left_fork, self.right_fork
        while self.running:
            fork1.acquire()
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print('philosopher %s change this forks.' % self.index)
            fork1, fork2 = fork2, fork1
        else:
            return
        self.dining()

        fork2.release()
        fork1.release()

    def dining(self):
        print('philosopher number %s starts eating. ' % self.index)
        time.sleep(5)
        print('philosopher number %s finish.' % self.index)


def main():
    forks = [threading.Semaphore() for n in range(5)]
    philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5])
                    for i in range(5)]
    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(5)
    Philosopher.running = False
    print("Finish")


if __name__ == "__main__":
    main()