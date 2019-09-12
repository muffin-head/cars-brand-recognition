from tkinter import *
import requests
import os
import urllib.request
import cv2
from PIL import ImageTk, Image
import numpy as np
import tensorflow as tf
import sys
import tkinter as tk
def cardetect():  
# This is needed since the notebook is stored in the object_detection folder.
    sys.path.append("..")

    # Import utilites
    from utils import label_map_util
    from utils import visualization_utils as vis_util

    # Name of the directory containing the object detection module we're using
    MODEL_NAME = 'inference_graph'

    # Grab path to current working directory
    CWD_PATH = os.getcwd()

    # Path to frozen detection graph .pb file, which contains the model that is used
    # for object detection.
    PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

    # Path to label map file
    PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')

    # Number of classes the object detector can identify
    NUM_CLASSES = 4

    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    # Load the Tensorflow model into memory.
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess = tf.Session(graph=detection_graph)


    # Define input and output tensors (i.e. data) for the object detection classifier

    # Input tensor is the image
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

    # Output tensors are the detection boxes, scores, and classes
    # Each box represents a part of the image where a particular object was detected
    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

    # Each score represents level of confidence for each of the objects.
    # The score is shown on the result image, together with the class label.
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

    # Number of objects detected
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')
    link=(e1.get())
    video = cv2.VideoCapture("http://"+link+":4747/video")
    #video=cv2.VideoCapture("http://"+link+":8080/video")for using ipwebcam
    ret = video.set(3,1280)
    ret = video.set(4,720)

    while(True):

        # Acquire frame and expand frame dimensions to have shape: [1, None, None, 3]
        # i.e. a single-column array, where each item in the column has the pixel RGB value
        ret, frame = video.read()
        frame_expanded = np.expand_dims(frame, axis=0)

        # Perform the actual detection by running the model with the image as input
        (boxes, scores, classes, num) = sess.run(
            [detection_boxes, detection_scores, detection_classes, num_detections],
            feed_dict={image_tensor: frame_expanded})
        # Draw the results of the detection (aka 'visulaize the results')
        vis_util.visualize_boxes_and_labels_on_image_array(
            frame,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=8,
            min_score_thresh=0.60)
        cv2.imshow('Object detector', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
    # Clean up
    video.release()
    cv2.destroyAllWindows()
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
master = tk.Tk()
background=tk.PhotoImage(file='D:/tensorflow1 - Copy (3)/models/research/object_detection/33.png')
background_label=Label(master,image=background)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
label1=tk.Label(master, text="Enter droidcam wifi ip",bg="SpringGreen3",height=1,bd=10,width=18,font = "Helvetica 16 bold italic")
label1.place(x=150,y=50)
e1 = tk.Entry(master,font = "Helvetica 16 bold italic",bd=10)
e1.place(x=400,y=50)

tk.Button(master,text="EXIT",height = 1, width = 4,bg="red",font = "Helvetica 16 bold italic",bd=10,command=master.destroy).place(x=1380,y=0)
tk.Button(master, text='Start',height = 1, width = 4, command=cardetect,bg="SpringGreen3",font = "Helvetica 16 bold italic",bd=10).place(x=450,y=100)
text1="To check cars detection working using portable webcam or camera of handset,make sure Droid application is installed in webcam and your main system and handset are connected to the same network.If you desire to use USB cable,make sure you run the batch file of droid_usb and use the generated ip link to get conected to the droid services.FYI no internet connectivity required"
description=Message(master,text=text1,bg="SpringGreen",font = "Helvetica 14 bold italic",aspect=80).place(x=1160,y=430)
app=FullScreenApp(master)
tk.mainloop()
