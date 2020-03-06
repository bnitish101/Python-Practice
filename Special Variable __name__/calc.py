def add():
    print('Calc is calling: ', __name__)
    print('Add function.')


def sub():
    print('Sub function.')


def main():
   add()
   sub()

# main function is stand alone code


if __name__ == '__main__':
    main()