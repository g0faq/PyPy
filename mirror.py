from PIL import Image


def mirror():
    im = Image.open('image.jpg')
    w, h = im.size
    pixels = im.load()
    for x in range(w // 2):
        for y in range(h):
            pixels[x, y], pixels[w - x - 1, y] = pixels[w - x - 1, y], pixels[x, y]
    im.save('res.jpg')