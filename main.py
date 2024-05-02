from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import uic
import os
import sys
import pygame
import pygame.mixer
import eyed3
from tkinter import messagebox as msgbox
import random
pygame.mixer.init()
pygame.init()
from BlurWindow.blurWindow import blur

class Ui(QMainWindow):
    
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("ui/ui.ui", self)
        self.listmusic.setSpacing(5)
        self.btnplay.setPixmap(QPixmap("play.png"))
        self.mouseDoubleClickEvent = lambda e: self.seting()
        ## Adding The music to the listwidget
        self.widthb = 1348
        self.xb = 1150
        
        self.randx = 520
        self.prex = 570
        self.playx = 620
        self.nexx = 700
        self.repx = 750
        
        self.playing = None
        
        self.adding()
        self.rand_bool = False
        # Signals
        self.listmusic.itemDoubleClicked.connect(self.playing_music)
        self.btnplay.mousePressEvent = lambda e: self.pausing()
        self.nextplay.mousePressEvent = lambda e: self.Next()
        self.previusplay.mousePressEvent = lambda e: self.Previus()
        self.repeatplay.mousePressEvent = lambda e: self.Repeat()
        #self.seconds.mouseReleaseEvent = lambda e: self.timer2.start(1)
        self.rand.mousePressEvent = lambda e: self.random()
        
        self.pos = self.seconds.value()
        
        self.seconds.sliderMoved[int].connect(self.seekPosition)
        #QSlider.dragEnterEvent(self, a0)
        
        #pygame.mixer.music.set
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.seeing)
        self.timer.start(1)
        self.repeating = None
        self.full = False
        
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.set_pos)
        self.timer2.start(1000)
        
        self.timer3 = QTimer(self)
        self.timer3.timeout.connect(self.set_window)
        self.timer3.start(1)
        
        self.position = 0
        
        
    def set_window(self):
        #print (self.width(), self.widthb)
        
        result_w = 1000  - ((self.widthb - 57) - self.width())
        print (result_w)
        self.seconds.setFixedWidth(result_w)
        
        result_x = self.xb - ((self.widthb - 57) - self.width())
        self.lbltime_2.setGeometry(QRect(result_x, self.lbltime_2.y(), self.lbltime_2.width(), self.lbltime_2.height()))
        print (result_x)
        
        if self.isFullScreen() or self.isMaximized():
            #print (1)
            result_x = self.randx - ((self.widthb - 57) - self.width())
            self.rand.setGeometry(QRect(result_x, self.rand.y(), self.rand.width(), self.rand.height()))
            #print (result_x)
            
            result_x = self.playx - ((self.widthb - 57) - self.width())
            self.btnplay.setGeometry(QRect(result_x, self.btnplay.y(), self.btnplay.width(), self.btnplay.height()))
            #print (result_x)
            
            result_x = self.nexx - ((self.widthb - 57) - self.width())
            self.nextplay.setGeometry(QRect(result_x, self.nextplay.y(), self.nextplay.width(), self.nextplay.height()))
            #print (result_x)
            
            result_x = self.repx - ((self.widthb - 57) - self.width())
            self.repeatplay.setGeometry(QRect(result_x, self.repeatplay.y(), self.repeatplay.width(), self.repeatplay.height()))
            #print (result_x)
            
            result_x = (self.prex - ((self.widthb - 57) - self.width()))
            self.previusplay.setGeometry(QRect(result_x, self.previusplay.y(), self.previusplay.width(), self.previusplay.height()))
            #print (result_x)
        elif self.width() + 57 < 1000:
            print (2)
            result_x =   440 + self.randx - ((self.widthb - 57) - self.width())
            self.rand.setGeometry(QRect(result_x, self.rand.y(), self.rand.width(), self.rand.height()))
            #print (result_x)
            
            result_x = 440 +self.playx - ((self.widthb - 57) - self.width())
            self.btnplay.setGeometry(QRect(result_x, self.btnplay.y(), self.btnplay.width(), self.btnplay.height()))
            #print (result_x)
            
            result_x = 440 +self.nexx - ((self.widthb - 57) - self.width())
            self.nextplay.setGeometry(QRect(result_x, self.nextplay.y(), self.nextplay.width(), self.nextplay.height()))
            #print (result_x)
            
            result_x = 440 +self.repx - ((self.widthb - 57) - self.width())
            self.repeatplay.setGeometry(QRect(result_x, self.repeatplay.y(), self.repeatplay.width(), self.repeatplay.height()))
            #print (result_x)
            
            result_x = (440 +self.prex - ((self.widthb - 57) - self.width()))
            self.previusplay.setGeometry(QRect(result_x, self.previusplay.y(), self.previusplay.width(), self.previusplay.height()))
            #print (result_x)
        else:
            print (3)
            print (self.width() + 57)
            result_x =   200 + self.randx - ((self.widthb - 57) - self.width())
            self.rand.setGeometry(QRect(result_x, self.rand.y(), self.rand.width(), self.rand.height()))
            #print (result_x)
            
            result_x = 200 +self.playx - ((self.widthb - 57) - self.width())
            self.btnplay.setGeometry(QRect(result_x, self.btnplay.y(), self.btnplay.width(), self.btnplay.height()))
            #print (result_x)
            
            result_x = 200 +self.nexx - ((self.widthb - 57) - self.width())
            self.nextplay.setGeometry(QRect(result_x, self.nextplay.y(), self.nextplay.width(), self.nextplay.height()))
            #print (result_x)
            
            result_x = 200 +self.repx - ((self.widthb - 57) - self.width())
            self.repeatplay.setGeometry(QRect(result_x, self.repeatplay.y(), self.repeatplay.width(), self.repeatplay.height()))
            #print (result_x)
            
            result_x = (200 +self.prex - ((self.widthb - 57) - self.width()))
            self.previusplay.setGeometry(QRect(result_x, self.previusplay.y(), self.previusplay.width(), self.previusplay.height()))
            #print (result_x)
        
    def seekPosition(self, position):
        sender = self.sender()
        #print ()
        if isinstance(sender,QSlider):
            
                    self.position = position
                    pygame.mixer.music.set_pos(position)
                    
            
    def set_pos(self):
        if self.playing == True:
            self.position += 1
            
        elif self.playing == False:
            #self.position = 0
            pass
        else:
            self.position = 0
    def seting(self):
        
        if self.full == False:
            self.showFullScreen()
            self.full = True
        else:
            self.full = False
            self.showNormal()
    def Repeat(self):
        if self.repeating == None:
            self.repeating = True
            self.repeatplay.setPixmap(QPixmap("repeat-again.png"))
        elif self.repeating == True:
            self.repeating = False
            self.repeatplay.setPixmap(QPixmap("repeat-off.png"))
        else:
            self.repeating = None
            self.repeatplay.setPixmap(QPixmap("repeat.png"))
    def adding(self):
        self.type = ['.mp3', '.flac']
        self.listmusic.clear()
        directory = os.listdir(f"C:/Users/{os.getlogin()}/Music")
        
        directory.remove("desktop.ini")
        for i in directory:
            if os.path.splitext(i)[-1] in self.type:
                self.listmusic.addItem(os.path.splitext(i)[0])
          
    def Next(self):
        try:
            if self.rand_bool == True:
                self.position = 0
                files = os.listdir(f"C:/Users/{os.getlogin()}/Music")
                files.remove("desktop.ini")
                self.filename = random.choice(files)
                print (self.filename)
                pygame.mixer.music.unload()
                pygame.mixer.music.load(f"C:/Users/{os.getlogin()}/Music/{self.filename}")  
                pygame.mixer.music.play()
                self.data = eyed3.load(f"C:/Users/{os.getlogin()}/Music/{self.filename}")
                tag  = self.data.tag
                self.title.setText(self.data.tag.title if tag != None else "Unknown")
                try:
                    self.zir.setText(self.data.tag.artist+" "+self.data.tag.album)
                except:
                    self.zir.setText("Unknown")
                if tag != None:
                    for image in self.data.tag.images:
                        file = open("music.png", "wb")
                        file.write(image.image_data)
                        file.close()
                    for image in self.data.tag.images:
                        file = open("ui/music.png", "wb")
                        file.write(image.image_data)
                        file.close()
                    imageing = QPixmap("ui/music.png")
                    self.musicimg.setStyleSheet("QLabel{border-image:url(music.png);background-color:rgb(0,0,0,0);border-radius:8%;border:1px solid rgb(217,217,217;)}")
                    self.musicimg.setScaledContents(True)
                    self.musicimg.setMargin(20)
                else:
                    imageing = QPixmap("ui/unknown.png")
                    self.musicimg.setStyleSheet("QLabel{border-image:url(music.png);background-color:rgb(0,0,0,0);border-radius:8%}")
                    self.musicimg.setScaledContents(True)
                    self.musicimg.setMargin(20)
            else:
                files = os.listdir(f"C:/Users/{os.getlogin()}/Music")
                files.remove("desktop.ini")
                index = files.index(self.filename)+1
                self.filename = files[index]
            
                
            
            self.btnplay.setPixmap(QPixmap("pause.png"))
            self.btnplay.setEnabled(True)
            self.nextplay.setEnabled(True)
            self.previusplay.setEnabled(True)
            
            self.playing = True
            self.position = 0
            pygame.mixer.music.unload()
            pygame.mixer.music.load(f"C:/Users/{os.getlogin()}/Music/{self.filename}")  
            pygame.mixer.music.play()
            
            self.data = eyed3.load(f"C:/Users/{os.getlogin()}/Music/{self.filename}")
            tag = self.data.tag
            self.title.setText(self.data.tag.title if tag != None else "Unknown")
            try:
                self.zir.setText(self.data.tag.artist+" "+self.data.tag.album)
            except:
                self.zir.setText("Unknown")
            
            
                
            #file.close()
            if tag != None:
                for image in self.data.tag.images:
                    file = open("music.png", "wb")
                    file.write(image.image_data)
                    file.close()
                for image in self.data.tag.images:
                    file = open("ui/music.png", "wb")
                    file.write(image.image_data)
                    file.close()
                imageing = QPixmap("ui/music.png")
                self.musicimg.setStyleSheet("QLabel{border-image:url(music.png);background-color:rgb(0,0,0,0);border-radius:8%}")
                self.musicimg.setScaledContents(True)
                self.musicimg.setMargin(20)
            else:
                imageing = QPixmap("ui/unknown.png")
                self.musicimg.setStyleSheet("QLabel{border-image:url(music.png);background-color:rgb(0,0,0,0);border-radius:8%}")
                self.musicimg.setScaledContents(True)
                self.musicimg.setMargin(20)
        except Exception as e:
            error = msgbox.showerror("Error", e)
            #erorr.show()
    def random(self):
        if self.rand_bool == False:
            self.rand_bool = True
            self.rand.setPixmap(QPixmap("random.png"))
        else:
            self.rand_bool = False
            self.rand.setPixmap(QPixmap("random_off.png"))
        
    def Previus(self):
        print ("Hello")
        files = os.listdir(f"C:/Users/{os.getlogin()}/Music")
        files.remove("desktop.ini")
        index = files.index(self.filename)-1
        self.filename = files[index]
        
            
        
        self.btnplay.setPixmap(QPixmap("pause.png"))
        self.btnplay.setEnabled(True)
        self.nextplay.setEnabled(True)
        self.previusplay.setEnabled(True)
        self.position = 0
        self.playing = True
        pygame.mixer.music.unload()
        pygame.mixer.music.load(f"C:/Users/{os.getlogin()}/Music/{self.filename}")  
        pygame.mixer.music.play()
        self.data = eyed3.load(f"C:/Users/{os.getlogin()}/Music/{self.filename}")
        try:
            self.title.setText(self.data.tag.title)
        except:
            self.title.setText("Unknown")
        try:
            self.zir.setText(self.data.tag.artist+" "+self.data.tag.album)
        except:
            self.zir.setText("Unknown")
        
        
        tag = self.data.tag
        #file.close()
        if tag != None:
            for image in self.data.tag.images:
                file = open("music.png", "wb")
                file.write(image.image_data)
                file.close()
            for image in self.data.tag.images:
                file = open("ui/music.png", "wb")
                file.write(image.image_data)
                file.close()
            imageing = QPixmap("ui/music.png")
            self.musicimg.setStyleSheet("QLabel{border-image:url(music.png);background-color:rgb(0,0,0,0);border-radius:8%}")
            self.musicimg.setScaledContents(True)
            self.musicimg.setMargin(20)
        else:
            imageing = QPixmap("ui/unknown.png")
            self.musicimg.setStyleSheet("QLabel{border-image:url(music.png);background-color:rgb(0,0,0,0);border-radius:8%}")
            self.musicimg.setScaledContents(True)
            self.musicimg.setMargin(20)
         
    def playing_music(self):
            
            self.btnplay.setPixmap(QPixmap("pause.png"))
            self.btnplay.setEnabled(True)
            self.nextplay.setEnabled(True)
            self.previusplay.setEnabled(True)
            
            self.playing = True
            filename = self.listmusic.currentItem().text()
            files = os.listdir(f"C:/Users/{os.getlogin()}/Music")
            files.remove("desktop.ini")
            for file in files:
                print (os.path.split(file)[0])
                if os.path.splitext(file)[0] == filename:
                    self.filename = file
            self.position = 0
            pygame.mixer.music.unload()
            pygame.mixer.music.load(f"C:/Users/{os.getlogin()}/Music/{self.filename}")  
            pygame.mixer.music.play()
            self.data = eyed3.load(f"C:/Users/{os.getlogin()}/Music/{self.filename}")
            tag = self.data.tag
            self.title.setText(self.data.tag.title if tag != None else "Unknown")
            try:
                self.zir.setText(self.data.tag.artist+" "+self.data.tag.album)
            except:
                pass
            
            
            if tag != None:
                for image in self.data.tag.images:
                    file = open("music.png", "wb")
                    file.write(image.image_data)
                    file.close()
                for image in self.data.tag.images:
                    file = open("ui/music.png", "wb")
                    file.write(image.image_data)
                    file.close()
                imageing = QPixmap("ui/music.png")
                self.musicimg.setStyleSheet("QLabel{border-image:url(music.png);background-color:rgb(0,0,0,0);border-radius:8%}")
                self.musicimg.setScaledContents(True)
                self.musicimg.setMargin(20)
            else:
                imageing = QPixmap("ui/unknown.png")
                self.musicimg.setStyleSheet("QLabel{border-image:url(music.png);background-color:rgb(0,0,0,0);border-radius:8%}")
                self.musicimg.setScaledContents(True)
                self.musicimg.setMargin(20)
            #self.musicimg.setPixmap(QPixmap("music.png"))
            
            
        
    def pausing(self):
        if self.playing == False:
            self.btnplay.setPixmap(QPixmap("pause.png"))
            self.playing = True
            pygame.mixer.music.unpause()
            
        elif self.playing == None:
            self.btnplay.setPixmap(QPixmap("pause.png"))
            self.btnplay.setEnabled(True)
            self.nextplay.setEnabled(True)
            self.previusplay.setEnabled(True)
            
            self.playing = True
            filename = self.listmusic.currentItem().text()
            pygame.mixer.music.unload()
            pygame.mixer.music.load(f"C:/Users/{os.getlogin()}/Music/{filename}")  
            pygame.mixer.music.play()
        elif self.playing == True:
            self.playing = False
            self.btnplay.setPixmap(QPixmap("play.png"))
            pygame.mixer.music.pause()
            
    def seeing(self):
        #print (self.repeating)
        files = os.listdir(f"C:/Users/{os.getlogin()}/Music")
        files.remove("desktop.ini")
        try:
            index = files.index(self.filename)
        except:
            pass
        if self.playing == None:
            self.btnplay.setEnabled(False)
            self.nextplay.setEnabled(False)
            self.previusplay.setEnabled(False)
        try:
            if files[-1] == files[index] and self.rand_bool == False:
                self.nextplay.setEnabled(False)
            if files[-1] == files[index] and self.rand_bool == True:
                self.nextplay.setEnabled(True)
        except:
            pass
        try:
            if files[0] == files[index]:
                self.previusplay.setEnabled(False)
            
        except:
            pass
        
        try:
            #print (" "*1000)
            #print (int(pygame.mixer.music.get_pos()/1000),int(self.data.info.time_secs))
            if self.position == int(self.data.info.time_secs-1):
                if self.repeating == None and self.nextplay.isEnabled() == True:
                    
                    self.Next()
                if self.repeating == True:
                    print ("Hello World")
                    self.position = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play()
                    
                if self.repeating == False:
                    
                    pygame.mixer.music.stop()
                    self.btnplay.setPixmap(QPixmap("play.png"))
                    self.btnplay.setEnabled(False)
                    self.nextplay.setEnabled(False)
                    self.previusplay.setEnabled(False)
                    self.playing = None
                    self.position = 0
                if self.rand_bool == True and self.repeating in (False, None):
                    self.position = 0
                    files = os.listdir(f"C:/Users/{os.getlogin()}/Music")
                    files.remove("desktop.ini")
                    self.filename = random.choice(files)
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(f"C:/Users/{os.getlogin()}/Music/{self.filename}")  
                    pygame.mixer.music.play()
                    self.data = eyed3.load(f"C:/Users/{os.getlogin()}/Music/{self.filename}")
                    tag = self.data.tag
                    self.title.setText(self.data.tag.title if tag != None else "Unkown")
                    try:
                        self.zir.setText(self.data.tag.artist+" "+self.data.tag.album)
                    except:
                        pass
                    
                    
                    if tag != None:
                        for image in self.data.tag.images:
                            file = open("music.png", "wb")
                            file.write(image.image_data)
                            file.close()
                        for image in self.data.tag.images:
                            file = open("ui/music.png", "wb")
                            file.write(image.image_data)
                            file.close()
                        imageing = QPixmap("ui/music.png")
                        self.musicimg.setStyleSheet("QLabel{border-image:url(music.png);background-color:rgb(0,0,0,0);border-radius:8%}")
                        self.musicimg.setScaledContents(True)
                        self.musicimg.setMargin(20)
                    else:
                        imageing = QPixmap("ui/unknown.png")
                        self.musicimg.setStyleSheet("QLabel{border-image:url(music.png);background-color:rgb(0,0,0,0);border-radius:8%}")
                        self.musicimg.setScaledContents(True)
                        self.musicimg.setMargin(20)
                
                
        except Exception as e:
            #print (e)
            #print (self.repeating)
            pass
            
        ### seconds
        self.sec = self.position
        self.seconds.setValue(self.sec)
        self.sec = self.sec % (24 * 3600)
        self.hour = self.sec // 3600
        self.sec %= 3600
        self.min = self.sec // 60
        self.sec %= 60
        self.result = "%02d:%02d:%02d" %(self.hour , self.min, self.sec)
        self.lbltime.setText(self.result)
        
        try:
            self.sec2 = int(self.data.info.time_secs)
            self.seconds.setMaximum(self.sec2)
            self.sec2 = self.sec2 % (24 * 3600)
            self.hour2 = self.sec2 // 3600
            self.sec2 %= 3600
            self.min2 = self.sec2 // 60
            self.sec2 %= 60
            self.result2 = "%02d:%02d:%02d" %(self.hour2 , self.min2, self.sec2)
            
            self.lbltime_2.setText(self.result2)
        except Exception as e:
            #print (e)
            self.lbltime_2.setText("00:00:00")
            
            
        ## titling
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui()
    blur(window.winId())
    window.show()
    app.exec_()