
import re
# import regex
# from collections import defaultdict
d = {}
ONLINE = True
prompt = True
pop_up1 = True
Index = 0
class login_information:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def Pcheck(self):
        global d
        global prompt
        global Index
        pattern = re.compile('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!?.])\S+')
        if re.findall(pattern, str(self.password)):
            print(' Good job! for meeting the criteria for the password')
            print('\___________________________________________________/')
            d[Index] = str(self.password)
            d[Index + 1] = str(self.username)
            Index = Index + 2
            prompt = False

        else:
            print(' You need to meet the password criteria, Try again')
            print('\_________________________________________________/')

def Sign_Up_Prompt_function():
    if prompt == True:
        UN = input("Username: ")
        PSW = input("Password: ")
        L1 = login_information(UN, PSW)
        login_information.Pcheck(L1)
        # print(d)
def Login_Prompt_function():
    if prompt == False:
        global ONLINE
        global d
        print('                    LOGIN PAGE                        ')
        print('Give us ur username and password or else you getting wacked')
        un = input('Login username: ')
        for i in range(Index):
            if d[i] == un:
                print('Great! now give us the password')
                ps = input('Login Password: ')
                for j in range(Index):
                    if d[j] == ps:
                        print('Access Granted')
                        ONLINE = False
        if ONLINE == True:
            print("Wrong Bruv")
def pop_up():
    global pop_up1
    if pop_up1 == True:
        print('|\_____________________________________________________/| Grub' + str(chr(169)))
        print('| Welcome to the sign in page!                          |')
        print('| Make sure that your Password has at least 1 of these: |')
        print('| A character from a-z lowercase                        |')
        print('| A character from A-Z Uppercase                        |')
        print('| A Number from 0-9                                     |')
        print('| And a symbol listed: either ! . or ?                  |')
        print(' \_____________________________________________________/ ')
        pop_up1 = False
while ONLINE == True:
    pop_up()
    Sign_Up_Prompt_function()
    Login_Prompt_function()

# UN = input("Username: ")
# PSW = input("Password: ")
# L1 = login_information(UN, PSW)
# print(login_information.Pcheck(L1))
# print(d)
# pattern = re.compile('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!?.])\S+')
# print(re.search(pattern,'a#3232!abbb32..'))
# Make the login page storage
# Make the logic for that ^^^
# Make it able to get a wrong input()
# launch that bih
# Also make sure that the password is strong in the first place
# Then we can launch the thingy
