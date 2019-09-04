from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import os
from PIL import ImageTk, Image
import cv2
import numpy as np
import tensorflow as tf
import sys
def cardetect():
    def clickme():
        def clickme1():
            sys.path.append("..")
            from utils import label_map_util
            from utils import visualization_utils as vis_util
            MODEL_NAME = 'inference_graph'
            IMAGE_NAME = file
            CWD_PATH = os.getcwd()
            PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')
            PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')
            PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)
            NUM_CLASSES = 4
            label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
            categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
            category_index = label_map_util.create_category_index(categories)
            detection_graph = tf.Graph()
            with detection_graph.as_default():
                od_graph_def = tf.GraphDef()
                with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                    serialized_graph = fid.read()
                    od_graph_def.ParseFromString(serialized_graph)
                    tf.import_graph_def(od_graph_def, name='')
                sess = tf.Session(graph=detection_graph)
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            image = cv2.imread(PATH_TO_IMAGE)
            image_expanded = np.expand_dims(image, axis=0)
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: image_expanded})
            vis_util.visualize_boxes_and_labels_on_image_array(
                image,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8,
                min_score_thresh=0.60)
            cv2.imshow('Object detector', image)
            cv2.waitKey(0)
            
            cv2.destroyAllWindows()
            
        file=filedialog.askopenfilename(initialdir="/",title="select file",filetypes=[("jpeg files",".jpeg"),("jpg files",".jpg"),("png files",".png"),("all files",".*")])
    
        root=Tk()
        button=Button(root,height = 2, width = 11,bg="SpringGreen3",bd=10,text="Detect image!",font = "Helvetica 16 bold italic",command=clickme1)
        button.pack()
        w = Label(root, width=25,text="Click to recognize image!",bg="SpringGreen3",font = "Helvetica 16 bold italic").pack()
        text1="It’s easy enough to make a computer recognize a specific image, like a QR code, but they suck at recognizing things in states they don’t expect — enter image recognition.The way image recognition works, typically, involves the creation of a neural network that processes the individual pixels of an image. Researchers feed these networks as many pre-labelled images as they can, in order to “teach” them how to recognize similar images."
        description=Message(root,text=text1,bg="SpringGreen",font = "Helvetica 20 bold italic",aspect=1000).place(x=0,y=250)
        root.configure(bg="SpringGreen3")
        app1=FullScreenApp(root)
        root.mainloop()
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
    root1.geometry("170x200+30+30")

    background=PhotoImage(file='D:/tensorflow1 - Copy (3)/models/research/object_detection/33.png')
    background_label=Label(root1,image=background)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    tmp = PhotoImage(file='D:/tensorflow1 - Copy (3)/models/research/object_detection/88.png')
    tm = tmp.subsample(2, 2)
    button1=Button(root1,height = 100, width = 100,bg="red",command=clickme,image=tm,bd=10)
    button1.place(x=150,y=50)
    w = Label(root1, width=18,text="Select the cars image!",bg="SpringGreen3",font = "Helvetica 16 bold italic")
    w.place(x=110,y=180)
    exitbtn=Button(root1,text="EXIT",height = 1, width = 4,bg="red",font = "Helvetica 16 bold italic",bd=10,command=root1.destroy)
    exitbtn.place(x=1380,y=0)
    app=FullScreenApp(root1)
    root1.mainloop()

cardetect()
