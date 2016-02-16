# -*- coding: utf-8 -*-

import pyautogui as p

position = p.locateOnScreen('vow.png')
phrase = 'I certify this submission as my own original work completed in accordance with the Coursera Honor Code'

x = position[0] + position[2] / 2
y = position[1] + position[3] / 2
p.moveTo(x, y, 0.25)
p.click()
p.typewrite(phrase, 0.05)
