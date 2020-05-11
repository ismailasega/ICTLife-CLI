import sys
def main():

    login=input('Please enter your Access ID: ')
    for Access_ID in open('D:\ICTLife_credentials.txt', 'r').readlines():
        Access_info = Access_ID.split()
        if login == Access_info[0]:
            print('correct credentials')


if __name__ == '__main__':
    main()
