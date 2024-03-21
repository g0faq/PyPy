from PIL import Image, ImageDraw

ni = Image.new('RGB', (200, 100), (0, 0, 0))
draw = ImageDraw.Draw(ni)

sp = [0] * 180
for i in range(45):
    sp[i] = (round(255 - (i * 2.55)), 0, 0)
for i in range(45):
    sp[i + 45] = (round(127.5 - (i * 2.55)), 0, round((i * 2.55)))
for i in range(45):
    sp[i + 90] = (0, round(i * 2.55), round(127.5 - (i * 2.55)))
for i in range(45):
    sp[i + 135] = (0, round(127.5 + (i * 2.55)), 0)
 
for elem in sp:
    print(elem)
for i in range(200):
    draw.line((i, 0, i, 199), fill=(sp[i]))
ni.save('my_gradient.png')
