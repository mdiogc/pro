# ******************
# FIBONACCI ITERABLE
# ******************

class Fibonacci:
    def __init__(self, n):
        self.number = n
        self.previous, self.current = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.number:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return 0
        if self.count == 1:
            self.count += 1
            return 1
        self.previous, self.current = self.current, self.previous + self.current
        self.count += 1
        return self.current

def run(n):
    return list(Fibonacci(n))

