import cv2
import matplotlib.pyplot as plt

img = cv2.imread("pic.jpg")

crop = img[50:300, 50:300]
resize = cv2.resize(img, (300,300))
rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

titles = ["Original","Cropped","Resized","Rotated"]
images = [img,crop,resize,rotate]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis("off")

plt.show()

cv2.imwrite("crop.jpg",crop)
cv2.imwrite("resize.jpg",resize)
cv2.imwrite("rotate.jpg",rotate)
