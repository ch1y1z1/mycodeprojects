import pyautogui
import time
import pyscreenshot as ImageGrab

pyautogui.PAUSE = 0.002

time.sleep(2)

x = 555*2
y = 167*2
x2 = 897*2
y2 = 826*2
xx = 583*2
yy = 763*2
x11 = xx-x
y11 = yy-y
dxx = (80)*2
dyy = (80)*2


def zidong():

    # png = pyautogui.screenshot(region=(x, y, x2-x, y2-y))
    # png = ImageGrab.grab(bbox=(x, y, x2, y2))
    png = ImageGrab.grab(bbox=(x/2, y/2, x2/2, y2/2))
    # pix_4 = png.getpixel((1920-880, 1250-1220))
    # pix_3 = png.getpixel((1600-880, 1250-1220))
    # pix_2 = png.getpixel((1280-880, 1250-1220))
    # pix_1 = png.getpixel((960-880, 1250-1220))
    for i in range(8):
        pix_4 = png.getpixel((x11+dxx*3, y11-i*dyy))
        pix_3 = png.getpixel((x11+dxx*2, y11-i*dyy))
        pix_2 = png.getpixel((x11+dxx, y11-i*dyy))
        pix_1 = png.getpixel((x11, y11-i*dyy))
        print(pix_1, pix_2, pix_3, pix_4)

        if (pix_1[0] < 250):
            pyautogui.press('d')
        elif (pix_2[0] < 250):
            pyautogui.press('f')
        elif (pix_3[0] < 250):
            pyautogui.press('j')
        elif (pix_4[0] < 250):
            pyautogui.press('k')

        # time.sleep(0.02)


def kaishi():
    a = time.time()
    b = time.time()
    while (b-a < 20):
        zidong()
        # time.sleep(0.05)
        b = time.time()


kaishi()


# png = ImageGrab.grab(bbox=(x/2, y/2, x2/2, y2/2))
# png.save('./ppp.png')
