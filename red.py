from PIL import Image

im = Image.open('image.jpg')
# im = Image.open('image.jpg')
pixels = im.load()  # список с пикселями
x, y = im.size  # ширина (x) и высота (y) изображения

count = 0
red = 0
green = 0
blue = 0
for i in range(x):
    for j in range(y):
        count += 1
        r, g, b = pixels[i, j]
        red += r
        green += g
        blue += b
print(red // count, green // count, blue // count)

# im.save("image.jpg")
