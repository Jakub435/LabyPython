import progressbar
import time


class Observer:
    _observers = []

    def __init__(self):
        self._observers.append(self)
        self._observables = {}

    def observe(self, event_name, callback):
        self._observables[event_name] = callback


class Event:

    def __init__(self, name):
        self.name = name
        self.fire()

    def fire(self):
        for observer in Observer._observers:
            if self.name in observer._observables:
                observer._observables[self.name]()


class ProgressBar(Observer):

    def __init__(self, val):
        Observer.__init__(self)
        self.bar = progressbar.ProgressBar(max_value=val)
        self.barValue = 0
        self.maxVal = val

    def incr_progressbar(self):
        if self.barValue < self.maxVal:
            self.barValue += 1
        else:
            return
        self.bar.update(self.barValue)


def main():
    VAL = 1000
    pBar = ProgressBar(VAL)
    pBar.observe("incrProgressBar", pBar.incr_progressbar)

    for i in range(VAL):
        Event("incrProgressBar")
        time.sleep(0.01)


if __name__ == '__main__':
    main()
