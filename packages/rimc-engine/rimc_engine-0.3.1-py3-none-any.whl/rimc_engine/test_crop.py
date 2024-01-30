from effects import centered_crop
from convert import open_apply_save
from tools import suffixname
from PIL import Image

img_p = 'bike.jpg'
out_path = '../../out/'
orig_path = '../../orig/'

orig = Image.open(orig_path+img_p)

out = centered_crop(orig)

o = out_path+suffixname(img_p, "crop")
print("Saving crop: ", o)
out.save(o)

