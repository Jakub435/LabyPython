import abc

class Clean:

    @abc.abstractmethod
    def wash(self):
        pass


class CleanFrontCarBody(Clean):

    def wash(self):
        print("CleanFrontCarBody")


class CleanBackCarBody(Clean):

    def wash(self):
        print("CleanBackCarBody")


class CleanFrontWheels(Clean):

    def wash(self):
        print("CleanFrontWheels")


class CleanBackWheels(Clean):

    def wash(self):
        print("CleanBackWheels")


class CarWash(Clean):

    def wash(self, typeOfWash):
        typeOfWash.wash()


def main():
    car_wash = CarWash()
    message = "1-umycie przodu karoseri\n2-umycie tyłu karoserii\n" \
              "3-czyszczenie przednich kół\n4-czyszczenie tylnich kół\n5-koniec\n"
    while True:
        option = input(message)
        if option == "1":
            car_wash.wash(CleanFrontCarBody())
        elif option == "2":
            car_wash.wash(CleanBackCarBody())
        elif option == "3":
            car_wash.wash(CleanFrontWheels())
        elif option == "4":
            car_wash.wash(CleanBackWheels())
        elif option == "5":
            break
        else:
            print("Brak opcji")


if __name__ == '__main__':
    main()
