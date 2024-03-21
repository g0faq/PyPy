from PIL import Image, ImageDraw


def gradient(color):
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for i in range(0, 512, 2):
        if color.lower() == 'r':
            draw.line((i, 0, i, 199), fill=(i // 2, 0, 0), width=2)
        elif color.lower() == 'g':
            draw.line((i, 0, i, 199), fill=(0, i // 2, 0), width=2)
        elif color.lower() == 'b':
            draw.line((i, 0, i, 199), fill=(0, 0, i // 2), width=2)
    new_image.save('res.png')


gradient('G')