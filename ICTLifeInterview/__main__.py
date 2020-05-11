import sys
def main():

    AWS_ACCESS_KEY_ID=input('Please enter your AWS_ACCESS_KEY_ID: ')
    for Access_ID in open('D:\ICTLife_credentials.txt', 'r').readlines():
        Access_info = Access_ID.split()
        if AWS_ACCESS_KEY_ID == Access_info[0]:
            print('correct credentials')
            return True
        print("Incorrect credentials.")
        return False

if __name__ == '__main__':
    main()
