import tkinter as tk
from tkinter import filedialog
import threading
from tkinter import messagebox
from random import randint
import datetime 
import time
import os
import math
from PIL import Image, ImageTk

input_file_path = ''

class GUI(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Nhận diện biển số xe")
		self.geometry('1250x650')
		self['bg'] = '#FFFFCC'

## ***************** THONG TIN - GIỚI THIỆU ******************
		self.GVHD = tk.Label(self,text = 'GVHD: Name',font = ('Times New Roman', 14), bg= '#FFFFCC',fg = '#222222')
		self.GVHD.place(x = 840,y=520)

		self.sv1 = tk.Label(self,text = 'Nguyễn Hương Giang - B17DCPT058',font = ('Times New Roman', 12), bg= '#FFFFCC',fg = '#222222')
		self.sv1.place(x = 902,y=545)

		self.sv2 = tk.Label(self,text = 'Lê Minh Hiếu - B17DCPT078',font = ('Times New Roman', 12), bg= '#FFFFCC',fg = '#222222')
		self.sv2.place(x = 902,y=565)

		self.sv2 = tk.Label(self,text = 'Phùng Thị Phương Thanh - B17DCPT170',font = ('Times New Roman', 12), bg= '#FFFFCC',fg = '#222222')
		self.sv2.place(x = 902,y=585)

# *****************************************************************
		self.input_file_path = ''
		self.input = ''
		self.output = ''
		self.flag = 0

# anh trang
		self.while_ = Image.open("while_image.PNG")
		self.while__ = self.while_.resize((600, 450),Image.ANTIALIAS)
		self.while_img = ImageTk.PhotoImage(self.while__)
# tieu de
		self.title = tk.Label(self,text = 'Nhận diện biển số xe',font = ('arial', 20), bg= '#FFFFCC',fg = '#000000')
		self.title.place(x = 500,y=1)

# image input and output
		self.input_img = tk.Label(self,image = self.while_img)
		# self.input_img.image = self.ip_img
		self.input_img.place(x = 10,y=50)

		self.output_img = tk.Label(self,image = self.while_img)
		self.output_img.place(x = 640,y=50)

# *******************************************************************************
# btn nhan dien anh
		self.start = tk.Button(self,text='Xử lý',width=6,height=2, command =lambda: self.handles.start_main())
		self.start.place(x=600,y=550)
# btn chon anh input
		self.ip_btn = tk.Button(self,text='Input',width=7,height=2, command =lambda: self.handles.browseFiles())
		self.ip_btn.place(x=280,y=510)

# label thong bao
		self.thong_bao = tk.Label(self,text = '',font = ('arial', 12), bg= '#FFFFCC',fg = '#000000')
		self.thong_bao.place(x = 580,y=510)

		self.handles = handles(self)

	def notification(self, title, msg):
		messagebox.showinfo(str(title), str(msg))

class handles():
	def __init__(self,gui):
		super().__init__()
		self.gui =gui

	def start_main(self):
		t1 = threading.Thread(target=self.start_main_())
		t1.start()

	def start_main_(self):
		if self.gui.flag ==0:
			self.gui.notification("Chú ý!", "Chọn ảnh xử lý")
		else:
			
			time.sleep(1)
			script = 'python main.py --image_path='+self.gui.input_file_path
			os.system(script)
			self.gui.thong_bao.configure(text = 'Đã xử lý xong')
			self.gui.output = Image.open('output.jpg')
			self.gui.output_ = self.gui.output.resize((600, 450),Image.ANTIALIAS)
			self.gui.output_label = ImageTk.PhotoImage(self.gui.output_)
			self.gui.output_img.configure(image=self.gui.output_label)
			os.system('rm -rf output.jpg')


	def browseFiles(self):
		self.gui.thong_bao.configure(text = '')
		filename = filedialog.askopenfilename(initialdir = "./samples/",
											title = "Chọn ảnh nhận diện",
											filetypes = (("Text files",
															"*.jpg*"),
														("all files",
															"*.*")))
	
		self.gui.input_file_path = filename
		self.gui.flag = 1
		self.gui.input = Image.open(self.gui.input_file_path)
		self.gui.input_ = self.gui.input.resize((600, 450),Image.ANTIALIAS)
		self.gui.input_label = ImageTk.PhotoImage(self.gui.input_)
		self.gui.input_img.configure(image=self.gui.input_label)
		self.gui.thong_bao.configure(text = '')
		self.gui.output_img.configure(image=self.gui.while_img)

		print(input_file_path)

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()