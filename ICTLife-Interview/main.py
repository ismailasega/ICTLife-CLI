import sys
from .classmodule import ICTlife
from .funcmodule import ICTlife_function
def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    ICTlife_function('hello world')
    my_object = ICTlife('Thomas')
    my_object.say_name()
if __name__ == '__main__':
    main()
