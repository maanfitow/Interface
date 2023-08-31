import cv2 as cv
import depthai as dai
import pandas as pd
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import random as rd
from time import sleep
import sys

# Key to control the camera
continue_camera = True

# Create the camera
pipeline = dai.Pipeline()

camRgb = pipeline.createColorCamera()
camRgb.setPreviewSize(640, 480)
camRgb.setInterleaved(False)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setBoardSocket(dai.CameraBoardSocket.CAM_A)

# Set autofocus mode
camRgb.initialControl.setAutoFocusMode(dai.RawCameraControl.AutoFocusMode.AUTO)

# Set output xlinks
xoutRgb = pipeline.createXLinkOut()
xoutRgb.setStreamName("rgb")

# Linking
camRgb.preview.link(xoutRgb.input)

def get_number():
    """Get the number of the last image saved in the csv file"""
    df = pd.read_csv('Interface/dataset.csv')
    df.dropna()
    # Try to get the number from the last name in the "Name" column (like "capture_01" will give "1")
    # If there is an error, try with the second to last name
    while True:
        try:
            number = int(df['Name'].iloc[-1][-2:])
        except Exception as e:
            number = int(df['Name'].iloc[-2][-2:])
            print(f"Error: {e}")
        break
    return number

def save_capture(number):
    """Save the image name in the csv file"""
    df = pd.read_csv('Interface/dataset.csv')
    df.dropna()
    
    # Save the image name in the csv file
    # Random values for the height, width, and volume
    df.loc[number] = ['capture_' + str(number).zfill(2), rd.randint(10, 100), rd.randint(10, 100), rd.randint(10, 100), rd.choice([True, False])]
    df.to_csv('Interface/dataset.csv', index=False)

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('Interface/ui/first_w.ui', self)
        self.bt_capture.clicked.connect(self.capture)
        self.bt_clear.clicked.connect(self.clear)
        # Turn on the camera when the button is checked
        self.chkOAK.clicked.connect(self.action)
        # Save the data when the button is clicked
        self.bt_save.clicked.connect(self.save_data)
    
    # This function saves the OAK-D camera's output to a file
    def capture(self):
        # Deactivate the camera
        self.cancel()
        sleep(2)
        try:
            with dai.Device(pipeline) as device:
                # Get output queues
                qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
                
                for _ in range(20):  # capture 10 frames
                    rgbFrame = qRgb.get().getCvFrame()
                
                # Get the number with the function
                number = get_number() + 1
                cv.imwrite(f"capture_{str(number).zfill(2)}.jpg", rgbFrame)
                
                # Save the image name in the csv file
                save_capture(number)                
                # Enable the camera again
                self.start_video()
        except Exception as e:
            print(f"Error: {e}")
            self.start_video()
            
    def action(self):
        global continue_camera
        if self.chkOAK.isChecked() and continue_camera:
            self.start_video()
            # Change the text of the button
            self.chkOAK.setText('Disable Camera')
            self.chkOAK.setStyleSheet("""color: rgb(255, 255, 255);
                                      background-color: rgb(0, 178, 148);
                                      border-radius: 10px""")
            continue_camera = False
        else:
            self.cancel()
            # Clear the image
            self.img_oak.clear()
            # Change the text of the button
            self.chkOAK.setText('Enable Camera')
            # Change the color of the text
            self.chkOAK.setStyleSheet("""color: rgb(255, 255, 255);
                                      background-color: rgb(255, 37, 80);
                                      border-radius: 10px""")
            continue_camera = True
    
    def start_video(self):
        self.Work = Work()
        self.Work.start()
        self.Work.Imageupd.connect(self.update_slot)
        
    def update_slot(self, Image):
        self.img_oak.setPixmap(QPixmap.fromImage(Image))
        
    def cancel(self):
        self.img_oak.clear()
        self.Work.stop()
        
    def exit_program(self):
        sys.exit()
    
    # Clear all the data of height, width, and volume (set them to 0)
    # They are QspinBox objects that only accept numbers
    def clear(self):
        self.sp_height.setValue(0)
        self.sp_width.setValue(0)
        self.sp_volume.setValue(0)
    
    # This function saves the data to a new row in the csv file
    # The format is as follows: Name, Height, Width, Volume, Water
    # capture_01, 10, 20, 30, True
    def save_data(self):
        global number
        global df
        df = pd.read_csv('Interface/dataset.csv')
        df.dropna()
        # Get the data from the QSpinBox objects
        height = self.sp_height.value()
        width = self.sp_width.value()
        volume = self.sp_volume.value()
        # Get the data from the rb_yes object for the water column as a boolean
        water = self.rb_yes.isChecked()
        # Write the data to the csv file
        df = pd.read_csv('Interface/dataset.csv')
        
        number = int(df['Name'].iloc[-1][-2:])
        df.loc[number] = ['capture_' + str(number + 1).zfill(2), height, width, volume, water]
        df.to_csv('Interface/dataset.csv', index=False)
        # Increase the number by 1
        number += 1
        self.capture()
        # Clear all the data
        self.clear()
        # Show the number in the label
        self.lb_number.setText('capture_' + str(number).zfill(2))

class Work(QThread):
    Imageupd = pyqtSignal(QImage)
    
    def run(self):
        self.net_running = True
        
        with dai.Device(pipeline) as device:
            # Get output queues
            qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
            
            while self.net_running:
                rgbFrame = qRgb.get().getCvFrame()
                rgbFrame = cv.cvtColor(rgbFrame, cv.COLOR_BGR2RGB)
                
                h, w, ch = rgbFrame.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbFrame.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(350, 350, Qt.KeepAspectRatio)
                self.Imageupd.emit(p)
    
    def stop(self):
        self.net_running = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()