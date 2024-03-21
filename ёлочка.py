from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#75BBFD', snow_color='#FFFAFA',
            trunk_color='#A45A52', needls_color='#01796F', sun_color='#FFDB00'):
    new_picture = Image.new('RGB', (width, height), sky_color)
    draw = ImageDraw.Draw(new_picture)
    draw.ellipse(((int(0.8 * width), -int(0.2 * height)),
                  (int(1.2 * width), int(0.2 * height))), sun_color)
    draw.polygon(((int(0.5 * width), int(0.1 * height)),
                  (int(0.6 * width), int(0.3 * height)),
                  (int(0.55 * width), int(0.3 * height)),
                  (int(0.65 * width), int(0.5 * height)),
                  (int(0.6 * width), int(0.5 * height)),
                  (int(0.7 * width), int(0.7 * height)),
                  (int(0.3 * width), int(0.7 * height)),
                  (int(0.4 * width), int(0.5 * height)),
                  (int(0.35 * width), int(0.5 * height)),
                  (int(0.45 * width), int(0.3 * height)),
                  (int(0.4 * width), int(0.3 * height))), needls_color)
    draw.rectangle(((0, int(0.8 * height)),
                    (width - 1), (height - 1)), snow_color)
    draw.polygon(((int(0.45 * width), int(0.9 * height)),
                  (int(0.45 * width), int(0.7 * height)),
                  (int(0.55 * width), int(0.7 * height)),
                  (int(0.55 * width), int(0.9 * height))), trunk_color)
    new_picture.save(file_name)
