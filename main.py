import colorgram


def rgb_from_pic(picture, num_of_colors):
    colors = colorgram.extract(picture, num_of_colors)
    color_list = []

    for color in colors:
        rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
        color_list.append(rgb)

    return color_list


rgb_colors = rgb_from_pic("image.jpg", 20)

print(rgb_colors)
