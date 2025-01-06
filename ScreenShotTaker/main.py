import pyscreenshot 
import datetime 

image = pyscreenshot.grab() 

image.show() 

filename = "screenshot" + str(datetime.datetime.now()) + ".png"

image.save(filename) 
