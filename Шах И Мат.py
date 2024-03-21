from PIL import Image, ImageDraw


def board(num, size):
    np = Image.new('RGB', (size * num, size * num), (255, 255, 255))
    draw = ImageDraw.Draw(np)
    for j in range(0, size * num, size * 2):
        for i in range(0, size * num, size * 2):
            draw.rectangle(((i, j), (i + size - 1, j + size - 1)), (0, 0, 0))
    for j in range(size, size * num, size * 2):
        for i in range(size, size * num, size * 2):
            draw.rectangle(((i, j), (i + size - 1, j + size - 1)), (0, 0, 0))
    np.save('res.png')