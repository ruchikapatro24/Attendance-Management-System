from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from pillow_avif import AvifImagePlugin


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1537x768+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1537,height=45)

        img_top=Image.open(r"C:\Users\ruchi\OneDrive\Desktop\Face Recognition System\images\How-Many-Web-Developers-in-the-World-1.avif")
        img_top=img_top.resize((1537,800),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1537,height=800)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=30,width=500,height=250)

        img_top1=Image.open(r"C:\Users\ruchi\OneDrive\Desktop\Face Recognition System\images\me.jpg")
        img_top1=img_top1.resize((200,180),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=32,width=180,height=200)

        #developer info
        dev_label = Label(main_frame, text="Hello my name is Ruchika Patro!", font=("times new roman", 20, "bold"), bg="white")
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame, text="I am full stack developer.", font=("times new roman", 20, "bold"), bg="white")
        dev_label.place(x=0,y=40)

        # img2=Image.open(r"C:\Users\ruchi\OneDrive\Desktop\Face Recognition System\images\studpg3.jpeg")
        # img2=img2.resize((500,390),Image.LANCZOS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # f_lbl=Label(main_frame,image=self.photoimg2)
        # f_lbl.place(x=0,y=210,width=500,height=390)



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()