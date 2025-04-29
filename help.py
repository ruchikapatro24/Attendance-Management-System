from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from pillow_avif import AvifImagePlugin


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1537x768+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1537,height=45)

        img_top=Image.open(r"C:\Users\ruchi\OneDrive\Desktop\Face Recognition System\images\istockphoto-1327214585-612x612.jpg")
        img_top=img_top.resize((1537,800),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1537,height=800)

        dev_label = Label(f_lbl, text="Email: ruchikapatro2004@gmail.com", font=("times new roman", 18, "bold"), bg="white")
        dev_label.place(x=550,y=540)


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()