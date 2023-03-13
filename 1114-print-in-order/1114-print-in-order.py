class Foo:
    def __init__(self):
        self.status = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.status = 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.status != 1:
            time.sleep(0.1)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.status = 2


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.status != 2:
            time.sleep(0.1)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.status = 3