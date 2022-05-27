# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_for():
    array = []
    for i in range(20):
        if i % 2 == 1:
            array.append(i)

    print(array)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = 3
    m = 4
    array = [[0] * m for _ in range(n)]
    print(array)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
