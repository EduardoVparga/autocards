import cv2

def formatting_name(name):
    name_split = name.title().split()
    if len(name_split) >= 3:
        name = ' '.join([name_split[0], f"{name_split[-2][0]}.", name_split[-1]])
    else:
        name = ' '.join(name_split)
    return name

def get_position(text, count, length, x, y, x_position = 165, y_position = 50):
    x_position = int(x_position*(len(text)/length))
    print(x_position, "position x")
    return x - x_position, int(count*y_position) + y

def write_name(img, fname, x, y, length = 21):
    
    if len(fname) > length:
        for i, text in enumerate(fname.split(" ", 1), 1):
            img = cv2.putText(
                img,
                text,
                get_position(text, i, length, x, y),
                cv2.FONT_HERSHEY_DUPLEX,
                1.5,
                (0, 0, 0),
                3
            )
    else:
        img = cv2.putText(
                img,
                fname,
                get_position(fname, 1.5, length, x, y),
                cv2.FONT_HERSHEY_DUPLEX,
                1.5,
                (0, 0, 0),
                3
            )
    
    return img


# img = cv2.imread("female.png")
img = cv2.imread("male.png")

qr = cv2.imread("basic_qrcode.png")
row, col, chan = qr.shape

y = 240
x = 593
img[y:row+y, x:col+x] = qr

text = "fernando eduardo valenzuela valenzuela"
text = formatting_name(text)
write_name(img, text, x, row+y)

cv2.imshow("image", img)
# cv2.imshow("qr", qr)
cv2.waitKey(0)
cv2.destroyAllWindows()