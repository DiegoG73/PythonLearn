import time

class FiboIter():
    def __init__(self, max=100):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        self.max
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            if not self.max:
                return self.aux
            if self.max:
                if self.aux > self.max:
                    raise StopIteration
                else:
                    return self.aux

if __name__ == '__main__':
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.5)