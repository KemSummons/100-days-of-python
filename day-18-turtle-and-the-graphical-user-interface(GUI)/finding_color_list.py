import colorgram

colors = colorgram.extract('image.jpg', 30)
color_list = []

for color in colors:
    rgb = color.rgb
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    full_color = red, green, blue
    color_list.append(full_color)
print(color_list)
