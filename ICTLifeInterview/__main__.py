import sys
import keyboard #using this module to assign keyboard keys to run program accountingly
import pandas as resources #using this module to create a DataFrame showing the list of resourses
def access_allowed(): #Validating IAM user access using the assigned AWS_ACCESS_KEY_ID
    AWS_ACCESS_KEY_ID = input('Please enter your AWS_ACCESS_KEY_ID: ')#input tag for user to input an AWS_ACCESS_KEY_ID to be validated
    for access_id in open('D:\ICTLife_credentials.txt', 'r'):#location of AWS_ACCESS_KEY_ID on local machine
            access_id = access_id.split()
            if AWS_ACCESS_KEY_ID == access_id[2]:#line location of the AWS_ACCESS_KEY_ID
                return True
            pass #if AWS_ACCESS_KEY_ID correct i am passing to procced and run program
    return False


def main():
    if access_allowed(): #if access granted display IAM_Users credentials
        print('\n' '******your IAM credentials******\n', open('D:\ICTLife_credentials.txt', 'r').read(), '\n' '******Keep them safe******', '\n')
        print('Access Granted\n')
    else:
        print('Invalid IAM user')
        sys.exit(0) #if entered AWS_ACCESS_KEY_ID Invalid program exits

    ResourceName = ['IAM_Users', 'EC2_Instatnces', 'RDS_Instances', 'S3 buckets', 'ECR_Repos', 'ECS_Clusters' ]#list of resources by name
    Allocation = [2, 6, 5, 1, 7, 15] #list of resources by allocations
    AvilableResouces = resources.DataFrame(ResourceName, columns = ['ResourceName'])# A DataFrame for only the resources by name
    NumberofResources = resources.DataFrame(list(zip(ResourceName, Allocation)),#using zipping two lists
                    columns = ['ResourceName' , 'Allocation'])#assigning column names for resources DataFrame

    print('''Help Menu:
    1.To list ResourceName press F1
    2.To list all resources and allocations press F2
    3.To Exit/Quit press Esc\n''')#Help Menu to ease application usage

    while True: #Assigning keyboard keys to use help menu options after login
        try:
            if keyboard.is_pressed('F1'):
                print('Below is a list of resourse names\n')#diplays the resources names only
                print(AvilableResouces.to_string(index=False),'\n') #prints out a DataFrame of the resources names
                break
            if keyboard.is_pressed('F2'):#diplays the resources
                print('Below is a list of all resourses and allocations\n')
                print(NumberofResources.to_string(index=False),'\n') #prints out a DataFrame of the resources and allocations
                break
            if keyboard.is_pressed('Esc'): #exits program
                print('\nExiting...')
                sys.exit(0)
        except:
            break

if __name__ == '__main__':
    main()
