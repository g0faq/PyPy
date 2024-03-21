from PIL import Image, ImageDraw


def gradient(color):
    sp_color_r = []
    sp_color_g = []
    sp_color_b = []
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for i in range(0, 512, 2):
        if color.lower() == 'r':
            sp_color_r.append((i // 2, 0, 0))
        elif color.lower() == 'g':
            sp_color_b.append((0, i // 2, 0))
        elif color.lower() == 'b':
            sp_color_b.append((0, 0, i // 2))
    new_image.save('res.png')