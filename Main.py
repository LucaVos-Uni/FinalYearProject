# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:01:38 2021

@author: -
"""

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
import cv2
import logging as logs
import datetime as dt
from time import sleep

class mainApp(App):
    def build(self, **kwargs):
        return mainLayout()

class mainLayout(GridLayout):
    def __init__(self,**kwargs):
        super(mainLayout, self).__init__(**kwargs)
        Window.size = (650,750)
        self.cols = 1
        self.row_default_height = 64
        self.row_force_default = True
        self.titleLayout = GridLayout(cols = 2, row_force_default = True, row_default_height = 64)
        self.layout = GridLayout(cols = 3, row_force_default = True, row_default_height = 128, padding = 20)
        self.titleLabel = Label(text = 'Title')
        self.close = Button(text='EXIT', on_press=self.pressed)

        self.titleLayout.add_widget(self.titleLabel)
        self.titleLayout.add_widget(self.close)

        self.layout.add_widget(Image(source='C:/Users/lucav/OneDrive/Documents/Uni/Final Year Project/Images/Hats/hat1.png'))
        self.layout.add_widget(Label(text = 'VD Hat'))
        self.layout.add_widget(Button(text='Add to List'))
        self.layout.add_widget(Image(source='C:/Users/lucav/OneDrive/Documents/Uni/Final Year Project/Images/Hats/hat2.png'))
        self.layout.add_widget(Label(text = 'Y-3 Hat'))
        self.layout.add_widget(Button(text='Add to List'))
        self.layout.add_widget(Image(source='C:/Users/lucav/OneDrive/Documents/Uni/Final Year Project/Images/Hats/hat3.png'))
        self.layout.add_widget(Label(text = 'Plain White Hat'))
        self.layout.add_widget(Button(text='Add to List'))
        self.layout.add_widget(Image(source='C:/Users/lucav/OneDrive/Documents/Uni/Final Year Project/Images/Hats/hat4.png'))
        self.layout.add_widget(Label(text = 'Plain Blue Hat'))
        self.layout.add_widget(Button(text='Add to List'))
        self.layout.add_widget(Label(text=''))
        self.cam = Button(text='Try on!', font_size=40, on_press=Camera.run)

        self.layout.add_widget(self.cam)
        self.add_widget(self.titleLayout)
        self.add_widget(self.layout)

    def pressed(self,instance):
        App.get_running_app().stop()


class Camera:
    def run(self):
        hcPath = "haarcascade_frontalface_default.xml"
        setCascade = cv2.CascadeClassifier(hcPath)
        logs.basicConfig(filename='webcam.log', level=logs.INFO)
        videoCap = cv2.VideoCapture(0)
        totFace = 0

        while True:
            if not videoCap.isOpened():
                print('Camera cannot be loaded')
                sleep(5)
                pass
            ret, frame = videoCap.read()
            faces = setCascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=7, minSize=(30, 30))
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if totFace != len(faces):
                totFace = len(faces)
                logs.info("num of faces: " + str(totFace) + ""
                                    " at " + str(dt.datetime.now()))
            frame = cv2.flip(frame, 1)
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        videoCap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    mainApp().run()