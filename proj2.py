import subprocess
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.ttk import Combobox
def image():
    subprocess.call(['python','proj.py'])
def webcam():
    subprocess.call(['python','Object_detection_webcam.py'])
def droidcam():
    subprocess.call(['python','proj1.py'])
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
root1=Tk()
background=PhotoImage(file='D:/tensorflow1 - Copy (3)/models/research/object_detection/33.png')
a=PhotoImage(file='D:/tensorflow1 - Copy (3)/models/research/object_detection/53.png')
tm = a.subsample(5, 5)
background_label=Label(root1,image=background)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
button1=Button(root1,text="Image",height = 100, width = 100,image=tm,command=image,bd=10)
button1.place(x=130,y=52)
label1= Label(root1, width=8,text="Image File",bg="SpringGreen3",font = "Helvetica 16 bold italic")
label1.place(x=130,y=175)
b=PhotoImage(file='D:/tensorflow1 - Copy (3)/models/research/object_detection/56.png')
tm1 = b.subsample(5, 5)
button2=Button(root1,text="WebCam",height = 100, width = 100,image=tm1,command=webcam,bd=10)
button2.place(x=130,y=450)
label2= Label(root1, width=8,text="webcam",bg="SpringGreen3",font = "Helvetica 16 bold italic")
label2.place(x=130,y=575)
c=PhotoImage(file='D:/tensorflow1 - Copy (3)/models/research/object_detection/57.png')
tm2 = c.subsample(5, 5)
button3=Button(root1,text="Droidcam",height = 100, width = 100,image=tm2,command=droidcam,bd=10)
button3.place(x=130,y=250)
label3= Label(root1, width=8,text="Droid app",bg="SpringGreen3",font = "Helvetica 16 bold italic")
label3.place(x=130,y=375)
app=FullScreenApp(root1)
root1.mainloop()
