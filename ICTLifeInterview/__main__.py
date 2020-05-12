import sys
def access_allowed(): #Validating IAM user using the assigned AWS_ACCESS_KEY_ID
    AWS_ACCESS_KEY_ID = input('Please enter your AWS_ACCESS_KEY_ID: ')
    for access_id in open('D:\ICTLife_credentials.txt', 'r'):
            access_id = access_id.split()
            if AWS_ACCESS_KEY_ID == access_id[2]:
                return True
    return False

if access_allowed():
    print('\n' '******your IAM credentials******\n', open('D:\ICTLife_credentials.txt', 'r').read(), '\n' '******Keep them safe******', '\n')
    print('Access Granted' '\n' 'press any key to continue')
else:
    print('Invalid IAM user')
    sys.exit()
#*******************************end of IAM User credentials Validation*******************************
def main():
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

if __name__ == '__main__':
    main()
