import abc


class ComponentI:

    @abc.abstractmethod
    def count(self):
        pass


class Component(ComponentI):

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.components = []

    def count(self):
        count = self.price
        for component in self.components:
            count += component.count()
        return count


    def addComponent(self, component):
        self.components.append(component)


def main():
    personal_computer = Component("PC", 0)
    personal_computer.addComponent(Component("karta graficzna", 1200))
    personal_computer.addComponent(Component("karta dźwiękowa", 100))
    personal_computer.addComponent(Component("zasilacz", 250))
    personal_computer.addComponent(Component("stacja DVD", 250))

    main_board = Component("płyta główna", 350)
    main_board.addComponent(Component("procesor", 900))
    main_board.addComponent(Component("RAM", 300))
    main_board.addComponent(Component("pasta termoprzewodząca", 9))

    personal_computer.addComponent(main_board)

    print(personal_computer.count())
    print(main_board.count())


if __name__ == '__main__':
    main()
