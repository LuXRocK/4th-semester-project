import pygame
import os
import re 

#Writing users to file
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


#Scoreboard
def scoreboard(data_file_path):
    scoreboard = {}
    with open('users.txt', 'r') as data_file:
        for line in data_file:
            scoreboard.update({line.split()[0] : line.split()[1]})
    data_file.close()
    scoreboard = sorted(scoreboard.items(), key=lambda x:x[1], reverse=True)
    scoreboard_list = []
    for item in scoreboard:
        scoreboard_list.append(item[0] + " " + item[1])
    return scoreboard_list

#Drawing text
def drawText(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x - textobj.get_width()/2, y - textobj.get_height()/2)
    surface.blit(textobj, textrect)