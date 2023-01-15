import datetime
import time
import random


class Delay:

    _delay = 60
    _fib = 1
    _delay_factor = 1
    _fib_array = [0, 1]

    def __init__(self, initial_delay: int):
        if type(initial_delay) is not int:
            raise ValueError('Invalid constructor argument. Requires int')
        self._delay = initial_delay

    def set_delay(self, seconds: int):
        self._delay = int(seconds)

    def set_initial_fib(self, fib):
        self._fib = fib

    def set_delay_factor(self, factor: int):
        self._delay_factor = factor

    def get_delay_factor(self) -> int:
        return self._delay_factor

    def get_fib(self) -> int:
        return self._fib

    def get_delay(self) -> int:
        rtn = self._delay * self._fib * self._delay_factor
        #print(f'Fib is {self._fib}')
        #print(f'Delay is {rtn}')
        return rtn

    def increase_delay(self):
        self._fib += 1
        #print(f'Increasing delay to {self._fib}')

    def decrease_delay(self):
        self._fib -= 1
        if self._fib <= 0:
            self._fib = 1
        #print(f'Decreasing delay to {self._fib}')

    def reset_delay(self):
        self._fib = 1

    def _fibonacci(self, n):
        try:
            n = int(n)
        except Exception as err:
            raise ValueError('Input has to be an integer')

        if n < 0:
            raise ValueError('Input has to be an integer greater than 0')

        elif n < len(self._fib_array):
            return self._fib_array[n]
        else:
            self._fib_array.append(self._fibonacci(n - 1) + self._fibonacci(n - 2))
            return self._fib_array[n]

    def __str__(self):
        return f'{self._fib=} {self._delay_factor=} {self._delay=}'

if __name__ == '__main__':

    a = Delay(5)
    a.delay_factor = 2
    x = 0
    kount = 0
    while kount < 10000:
        x = random.randint(0, 100)
        if x > 50:
            a.increase_delay()
        elif x <= 50:
            a.decrease_delay()
        if x <= 10:
            a.reset_delay()
            print('\nResetting Delay')
        print(f'X factor is {a}. delaying for {a.get_delay()} seconds')
        #time.sleep(3) # Ignoring a.get_delay() in favor of just sleeping 3 seconds for testing
        kount += 1
