# import pygame
import os
import re 

def selectUser(data_file_path, username_input):
    username_input = username_input.upper()
    if os.path.getsize(data_file_path) == 0:
        with open(data_file_path, 'a') as data_file:
            data_file.write(username_input)
            data_file.write(' ')
            data_file.write('0')
            data_file.write('\n')
            data_file.close()
    else:
        with open(data_file_path, 'r+') as data_file:
            for line in data_file:
                if re.search(username_input, line):
                    user = line.strip('\n') 
                    return user
            data_file.write(username_input)
            data_file.write(' ')
            data_file.write('0')
            data_file.write('\n')
            data_file.close()
    with open(data_file_path, 'r') as data_file:
        for line in data_file:
            if re.search(username_input, line):
                user = line.strip('\n')
                return line
        data_file.close()

# data_file_name = 'users.txt'
# username_input = 'Jan'
# user = selectUser(data_file_name, username_input)


# print(user)
# print(user.split(' ')[0], user.split(' ')[1])