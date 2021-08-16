
class Counter(object):

    def __init__(self):
        self.current = 0
        self.stop = 10

    def __iter__(self):
        self.__init__()
        return self

    def __next__(self):
        if self.current < self.stop:
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
        self.__init__()
        return self

    def __next__(self):
        if self.current != self.stop:
            self.current += self.step
        else:
            raise StopIteration

        return self.current


class FibCounter(object):

    def __init__(self, stop: int = 200):
        self.counter = 0
        self.current = 1
        self.stop = stop
        self.current_minus_1 = 1
        self.current_minus_2 = 1

    def __iter__(self):
        self.__init__()
        return self

    def __next__(self):
        start_seq_value = {0: 0,
                           1: 1,
                           2: 1
                           }.get(self.counter)

        if start_seq_value is not None:
            self.counter += 1
            return start_seq_value

        self.current_minus_2 = self.current_minus_1
        self.current_minus_1 = self.current
        self.current = self.current_minus_2 + self.current_minus_1
        self.counter += 1

        if self.current <= self.stop:
            return self.current

        raise StopIteration


if __name__ == '__main__':
    c = Counter()

    for number in c:
        print(number)

    cr = CounterRange(start=10, stop=0, step=-1)

    for number in cr:
        print(number)

    f = FibCounter()

    for number in f:
        print(number)
