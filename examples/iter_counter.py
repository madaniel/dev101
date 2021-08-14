
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


if __name__ == '__main__':
    c = Counter()

    for number in c:
        print(number)
