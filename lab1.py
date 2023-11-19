from PIL import Image
def print_image(image_path) :
    img = Image.open(image_path)
    img.show()
    print('Image Format : ', img.format)
    print('Image Mode : ', img.mode)
    print('Image Size : ', img.size)
    print('\n\n')


image_path = ["flower.jpeg", "flower2.jpeg", "flower3.jpeg", "flower4.jpeg", "flower5.jpeg"]
for i in image_path :
    print_image(i)    