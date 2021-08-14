
class Counter(object):

    def __init__(self):
        self.current = 0
        self.limit = 10

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
        else:
            raise StopIteration

        return self.current


class CounterRange(object):

    def __init__(self, start: int = 0, stop: int = 10, step: int = 1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current != self.stop:
            self.current += self.step
        else:
            raise StopIteration

        return self.current


if __name__ == '__main__':
    c = Counter()

    for number in c:
        print(number)

    cr = CounterRange(start=10, stop=0, step=-1)

    for number in cr:
        print(number)
