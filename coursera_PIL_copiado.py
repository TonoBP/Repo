import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import Image, ImageDraw, ImageFont

image = Image.open("readonly/msi_recruitment.gif")
image = image.convert('RGB')

#font
fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 30)

#settings for loop
factors = [0.1, 0.5, 0.9]
images = []

for i in factors:
    r, g, b= image.split()
    r = r.point(lambda x: x*i)
    new_img = Image.merge('RGB', (r, g, b))
    ft_bg = Image.new('RGB', (new_img, 40), color = (0, 0, 0))
    d = ImageDraw.Draw(ft_bg)
    d.text((10, 10), 'channel 0 intensity {}'.format(i), font = fnt, fill = new_img.getpixel((0, 50)))
    sheet = PIL.Image.new(mew_img.mode, (new_img.width, new_img.height + ft_bg.height))
    sheet.paste(ft_bg, (0, new_img.height))
    sheet.paste(new_img, (0, 0))
    images.append(sheet)

for i in factors:
    r, g, b= image.split()
    g = g.point(lambda x: x*i)
    new_img = Image.merge('RGB', (r, g, b))
    ft_bg = Image.new('RGB', (new_img, 40), color = (0, 0, 0))
    d = ImageDraw.Draw(ft_bg)
    d.text((10, 10), 'channel 0 intensity {}'.format(i), font = fnt, fill = new_img.getpixel((0, 50)))
    sheet = PIL.Image.new(mew_img.mode, (new_img.width, new_img.height + ft_bg.height))
    sheet.paste(ft_bg, (0, new_img.height))
    sheet.paste(new_img, (0, 0))
    images.append(sheet)

for i in factors:
    r, g, b= image.split()
    b = b.point(lambda x: x*i)
    new_img = Image.merge('RGB', (r, g, b))
    ft_bg = Image.new('RGB', (new_img, 40), color = (0, 0, 0))
    d = ImageDraw.Draw(ft_bg)
    d.text((10, 10), 'channel 0 intensity {}'.format(i), font = fnt, fill = new_img.getpixel((0, 50)))
    sheet = PIL.Image.new(mew_img.mode, (new_img.width, new_img.height + ft_bg.height))
    sheet.paste(ft_bg, (0, new_img.height))
    sheet.paste(new_img, (0, 0))
    images.append(sheet)
