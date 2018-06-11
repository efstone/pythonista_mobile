import photos, PIL, os
 
pic_to_resize = photos.pick_asset()
img = pic_to_resize.get_image()
all_folders = photos.get_albums()
for album in all_folders:
    if album.title == 'medium-sized':
        meds = album
new_size = (int(pic_to_resize.pixel_width / 3), int(pic_to_resize.pixel_height / 3))
img_med = img.resize(new_size, PIL.Image.ANTIALIAS)
img_med.save('img_med.jpg')
new_med = photos.create_image_asset('img_med.jpg')
meds.add_assets([new_med])
try:
    os.remove('img_med.jpg')
except OSError:
    pass
