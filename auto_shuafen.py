import pyautogui as pgui
from time import sleep as slp

pgui.FAILSAFE = True
pgui.PAUSE = 1.5

btn_2bb = (257,707)
btn_fold = (143,829)
btn_call = (403,829)
width = 541

x1 = 1

Nx = 3

def call(xn):
    pos_x = btn_call[0]+xn*width
    pos_y = btn_call[1]
    pgui.click(x=pos_x, y=pos_y)
    print('call ', xn)

def fold(xn):
    pos_x = btn_fold[0]+xn*width
    pos_y = btn_fold[1]
    pgui.click(x=pos_x, y=pos_y)
    print('fold ', xn)

def rs_poker(xn):
    pos_x = btn_2bb[0]+xn*width
    pos_y = btn_2bb[1]
    pgui.click(x=pos_x, y=pos_y)
    print('raise ', xn)

def process(xn):
    for i in range(Nx-1):
        call(xn)
        fold(xn)
        xn += 1
        xn = xn % Nx

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
    rs_poker(xn)    


def main():
    xi = x1
    slp(5)
    while True:
        print('utg is under: ', xi)
        process(xi)
        xi += 1
        xi = xi % Nx
        slp(9)
    

if __name__ == "__main__":
    main()    