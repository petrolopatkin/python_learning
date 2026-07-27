from PIL import Image
image1 = Image.open('GOT wallaper.jpg')
image1.rotate(90).save('GOT wallaper_modiefied.jpg')
image1.convert(mode= 'L').save('GOT wallaper_modiefied_2.jpg')