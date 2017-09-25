# -*- coding: utf-8 -*-
"""
Example




"""
from time import sleep as slp
import pyautogui as pgui
import cv2
import numpy as np

pgui.FAILSAFE = True
pgui.PAUSE = 1.2

btn_2bb = (257, 707)
btn_fold = (143, 829)
btn_call = (403, 829)
width = 541

x1 = 3

Nx = 4


def call(xn):
    """
    call action
    """
    pos_x = btn_call[0] + xn * width
    pos_y = btn_call[1]
    pgui.click(x=pos_x, y=pos_y)
    print('call ', xn)


def fold(xn):
    pos_x = btn_fold[0] + xn * width
    pos_y = btn_fold[1]
    pgui.click(x=pos_x, y=pos_y)
    print('fold ', xn)


def rs_poker(xn):
    pos_x = btn_2bb[0] + xn * width
    pos_y = btn_2bb[1]
    pgui.click(x=pos_x, y=pos_y)
    print('raise ', xn)


def process(xn):
    for i in range(Nx - 1):
        x = (xn + i) % Nx
        call(x)
        fold(x)
        # xn += 1
        # xn = xn % Nx

    # call(xn)
    # fold(xn)
    # xn += 1
    # xn = xn % Nx
    # call(xn)
    # fold(xn)
    # xn += 1
    # xn = xn % Nx
    # call(xn)
    # fold(xn)
    # xn += 1
    # xn = xn % Nx
    rs_poker((xn - 1 + Nx) % Nx)


def find_utg():
    # img = cv2.imread('screen.png', 0)
    img1 = cv2.imread('utg.png', 0)
    img2 = pgui.screenshot(region=(0, 650, 2160, 150))
    # img0 = cv2.imread('gui_save.png', 0)
    # img2.save('gui_save.png')
    img3 = np.array(img2)
    img4 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)
    # img3 = img2[:, :, ::, -1].copy()
    res = cv2.matchTemplate(img4, img1, cv2.TM_CCOEFF_NORMED)
    # print('res: ', res)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print('max_val:  , max_loc: ', max_val, max_loc)
    if max_val < 0.7:
        return -1

    top_left = min_loc
    # print(top_left[0]
    x_pos = top_left[0]
    x_pos_n = x_pos // width
    # print(x_pos_n)
    return x_pos_n


def main():
    xi = x1
    slp(5)
    while True:
        xi = find_utg()
        if xi < 0:
            slp(1)
            continue
        else:
            print('utg is under: ', xi)
            # slp(1)
            process(xi)
            # xi += 1
            # xi = xi % Nx
            slp(5)


if __name__ == "__main__":
    main()
