import math
import numpy as np
import time
import os
import cv2 as cv


def savej(png):

    b = png[:, :, 0].copy()
    g = png[:, :, 1].copy()
    r = png[:, :, 2].copy()

    out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    # out = out.astype(np.uint8)

    lx, ly = 32, 16

    outt = np.zeros((int(len(out)/lx), int(len(out[0])/ly)))

    for i in range(int(len(out)/lx)):
        for j in range(int(len(out[0])/ly)):
            outt[i][j] = out[lx*i][ly*j]
            outt[i][j] = outt[i][j]*1.5 if outt[i][j]*1.5 <= 255 else 255

    txt = ''

    for i in range(len(outt)):
        for j in range(len(outt[0])):
            txt = txt.join(
                ['@BMQ&AwhIfvL<i*r!;^:-_,\'. '[int(math.pow(outt[i][j], 1/2)/16*26)], ''])
        txt = txt.join(['\n', ''])

    txt = txt[::-1]
    print(txt)

    # print(tat)
    # tat = tat[::-1]


mp4 = cv.VideoCapture('./videos/xinbaodao.mp4')

# print(mp4)
# print(int(mp4.get(cv.CAP_PROP_FPS)))


ret, frame = mp4.read()
i = 0
start = time.time()
for i in range(30*117):
    ret, frame = mp4.read()
    if ret == False:
        break
    if i/30 >= (time.time() - start):
        os.system('clear')
        savej(frame)
        time.sleep(0.035)


mp4.release()
