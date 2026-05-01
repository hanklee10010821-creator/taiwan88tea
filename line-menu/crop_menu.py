from PIL import Image
img = Image.open('/Users/chen/.openclaw/media/inbound/file_27---5a677a23-fd96-413d-97d3-2cfaf038081b.jpg')

# Bottom text bar: let's guess it's 80px high. 1280 - 80 = 1200.
# Rich menu height: approx 418.
# top = 1200 - 418 = 782
menu = img.crop((0, 782, 619, 1200))
menu_resized = menu.resize((2500, 1686), Image.Resampling.LANCZOS)
menu_resized.save('/Users/chen/.openclaw/workspace/taiwan88tea/line-menu/cropped_menu.jpg', quality=95)
print("Saved")
