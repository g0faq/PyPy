from PIL import Image


def mirror():
    im = Image.open('image.jpg')
    w, h = im.size
    pixels = im.load()
    for y in range(h):
        for x in range(w - y):
            pixels[x, y], pixels[h - y - 1, w - x - 1] = pixels[h - y - 1, w - x - 1], pixels[x, y]
    im.save('res.jpg')