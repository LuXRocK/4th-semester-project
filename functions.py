# import pygame

def selectUser(data_file_path, username_input):
    data_file = open(data_file_path, 'r+')
    users = data_file.readlines()
    for user in users:
        if user.split(' ')[0] == username_input:
            username = username_input
            user_score = user.split(' ')[1]
            return username, user_score
    data_file.write('\n')
    data_file.write(username_input)
    data_file.write(' ')
    data_file.write('0')



