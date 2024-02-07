import img2pdf
import os
import pathlib

# opening from filename
images=['test.jpg','test1.jpg','test2.jpg']
with open("final.pdf","wb") as f:
	f.write(img2pdf.convert(images))

# convert all files ending in .jpg inside a directory
# dirname = "/path/to/images"
# imgs = []
# for fname in os.listdir(dirname):
# 	if not fname.endswith(".jpg"):
# 		continue
# 	path = os.path.join(dirname, fname)
# 	if os.path.isdir(path):
# 		continue
# 	imgs.append(path)
# with open("name.pdf","wb") as f:
# 	f.write(img2pdf.convert(imgs))
