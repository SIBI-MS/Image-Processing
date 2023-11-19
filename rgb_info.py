from PIL import Image

def print_image_info(image_path) :
    img = Image.open(image_path)
    #img.show()
    print('Image Format : ', img.format)
    print('Image Mode : ', img.mode)
    print('Image Size : ', img.size)
    r_channel, g_channel, b_channel = img.split()
    #print('r_channel : ', r_channel)
    #print('g_channel : ', g_channel)
    #print('b_channel : ', b_channel)
    pixel_data = list(img.getdata())
    print('No.of Pixels : ', len(pixel_data))
    pixel_color = pixel_data[50507]
    print('Color of first pixel : ', pixel_color)

image_path = 'flower.jpeg'
print_image_info(image_path)    

