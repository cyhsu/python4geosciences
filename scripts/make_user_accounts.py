import os

fuug = open('users_undergrads.txt')
fug = open('users_grads.txt')
fpug = open('passwds_undergrads.txt')
fpg = open('passwds_grads.txt')

# undergrads
for user, passwd in zip(fuug.readlines(), fpug.readlines()):

    # remove new line at end
    user = user.split()[0]
    passwd = passwd.split()[0]

    # https://www.systutorials.com/39549/changing-linux-users-password-in-one-command-line/
    command = 'sudo useradd ' + user + '; echo -e "' + passwd + '\n' + passwd + '" | sudo passwd ' + user
    print(command)
    os.system(command)

# grads
for user, passwd in zip(fug.readlines(), fpg.readlines()):

    # remove new line at end
    user = user.split()[0]
    passwd = passwd.split()[0]

    command = 'sudo useradd ' + user + '; echo -e "' + passwd + '\n' + passwd + '" | sudo passwd ' + user
    print(command)
    os.system(command)
