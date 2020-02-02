import cv2
import math


class Check:

    @staticmethod
    def run(image):
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)
        opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15)))
        contours, _ = cv2.findContours(opened, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        cnt_id = 0
        cnt_biggest_area = 0
        cnt_biggest_prm = 0
        i = 0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            prim = cv2.arcLength(cnt, True)
            if cnt_biggest_area < area:
                cnt_biggest_area = area
                cnt_biggest_prm = prim
                cnt_id = i
            i += 1

        cnt = contours[cnt_id]
        moment = cv2.moments(cnt)

        radius = int(cnt_biggest_prm / (math.pi * 2) - 10)
        x = int(moment['m10'] / moment['m00'])
        y = int(moment['m01'] / moment['m00'])

        # cv2.circle(img, (x,y), radius, (0,255,0),2)

        s1 = 0
        for c in cnt:
            pxl = image[c[0][1]][c[0][0]]
            s1 += (int(pxl[0]) + int(pxl[1]) + int(pxl[2])) / 3
        s1 = s1 / len(cnt)

        s2 = 0
        m = 0
        for i in range(y + radius - 10, image.shape[0]):
            for j in range(x + radius - 10, image.shape[1]):
                pxl = image[i][j]
                s2 += (int(pxl[0]) + int(pxl[1]) + int(pxl[2])) / 3
                m += 1

        for i in range(0, y - radius + 10):
            for j in range(0, x - radius + 10):
                pxl = image[i][j]
                s2 += (int(pxl[0]) + int(pxl[1]) + int(pxl[2])) / 3
                m += 1

        for i in range(y + radius - 10, image.shape[0]):
            for j in range(0, x - radius + 10):
                pxl = image[i][j]
                s2 += (int(pxl[0]) + int(pxl[1]) + int(pxl[2])) / 3
                m += 1

        for i in range(0, y - radius + 10):
            for j in range(x + radius - 10, image.shape[1]):
                pxl = image[i][j]
                s2 += (int(pxl[0]) + int(pxl[1]) + int(pxl[2])) / 3
                m += 1
        if m != 0:
            s2 = s2 / m
        else:
            s2 = 0

        if s2 == 0:
            return False, (0, 0), 0
        if s1 > 12 and s2 < 5:
            return True, (x, y), radius
        return False, (0, 0), 0
