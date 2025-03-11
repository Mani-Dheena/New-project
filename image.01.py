
#Here is an example of how to use the Image.merge() method to merge the red, green and blue bands of an image to create a new RGB image


from PIL import Image
image = Image.open("Images/butterfly.jpg")
r, g, b = image.split()
image = Image.merge("RGB", (b, g, r))