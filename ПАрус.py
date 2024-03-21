from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#87CEEB', ocean_color='#017B92',
            boat_color='#874535', sail_color='#FFFFFF', sun_color='#FFCF40'):
    new_picture = Image.new('RGB', (width, height), sky_color)
    draw = ImageDraw.Draw(new_picture)
    draw.ellipse(((int(0.8 * width), -int(0.2 * height)),
                 (int(1.2 * width), int(0.2 * height))), sun_color)
    draw.rectangle(((0, int(0.8 * height)),
                    (width - 1), (height - 1)), ocean_color)
    draw.polygon(((int(0.25 * width), int(0.65 * height)),
                  (int(0.3 * width), int(0.85 * height)),
                  (int(0.65 * width), int(0.85 * height)),
                  (int(0.7 * width), int(0.65 * height))), boat_color)
    draw.rectangle((int(0.49 * width), int(0.3 * height),
                   (int(0.51 * width), int(0.65 * height))), boat_color)
    draw.polygon(((int(0.51 * width), int(0.3 * height)),
                  (int(0.66 * width), int(0.45 * height)),
                  (int(0.51 * width), int(0.6 * height))), sail_color)
    new_picture.save(file_name)


# picture('test.bmp', 1000, 800)
