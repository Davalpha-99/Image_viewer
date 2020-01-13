from tkinter import *
from PIL import ImageTk,Image

root=Tk()
#root.geometry("458x430")
root.title("image viewer")
root.resizable(0,0)

#adding icon to the viewer.


#assessing the images that i want to display.
image_1=ImageTk.PhotoImage(Image.open('images\\abs_1.png'))
image_2=ImageTk.PhotoImage(Image.open('images\\abs_2.png'))
image_3=ImageTk.PhotoImage(Image.open('images\\abs_3.png'))
image_4=ImageTk.PhotoImage(Image.open('images\\abs_4.png'))
#image_5=ImageTk.PhotoImage(Image.open('images\\abs_5.png'))
#image_6=ImageTk.PhotoImage(Image.open('images\\abs_6.png'))
image_7=ImageTk.PhotoImage(Image.open('images\\abs_7.png'))
image_8=ImageTk.PhotoImage(Image.open('images\\abs_8.png'))
image_9=ImageTk.PhotoImage(Image.open('images\\abs_9.png'))
image_10=ImageTk.PhotoImage(Image.open('images\\abs_10.png'))


#image_list is a normal python list that consist of all the images in a list.
image_list=[image_1,image_2,image_3,image_4,image_7,image_8,image_9,image_10]

#label is a token variable used to put an image on screen initially.
label=Label(root,image=image_list[0])
label.grid(row=0,column=1)

#Function defining the work of forward button.
#remember the use of label.grid_forget() is compulsory, before adding a new image onto the label.
#because,if not done so,the images will overlap,and that's not what we want.
#we want that, the one image must come in while the other goes away(from the screen).
def forward(image_number):
	global label
	global forward_b
	global back_b
	label.grid_forget()
	label=Label(root,image=image_list[image_number-1])
	
	#defining the function of the forward button if in between images.
	#give note to the use of global variables with the label,forward_b and the back_b.
	#we used a global variable,because we want an access to these variables from outside the funtion,and alter their funtionality inside the function too,according to our requirements.
	forward_b=Button(root,text=">>",pady=20,command=lambda:forward(image_number+1))
	#defines what a back_b will do if called when currently the pointer is in forward() funtion.
	back_b=Button(root,text="<<",pady=20,command=lambda:back(image_number-1))
	
	#if we reach the last image of the list,we need to disable the forward button.
	if(image_number==len(image_list)):
		forward_b=Button(root,text=">>",pady=20,state=DISABLED)

	forward_b.grid(row=0,column=2)
	back_b.grid(row=0,column=0)
	label.grid(row=0,column=1)

#funtion that defines the functionality of the back key.
def back(image_number):
	global label
	global forward_b
	global back_b
	label.grid_forget()
	label=Label(root,image=image_list[image_number-1])
	
	#similar to the description given in the forward function,both working of forward_b and back_b is manipulated in back() function too.
	forward_b=Button(root,text=">>",pady=20,command=lambda:forward(image_number+1))
	back_b=Button(root,text="<<",pady=20,command=lambda:back(image_number-1))

	#if we reach the very first image,so;we want the backward button to be disabled.
	if(image_number==1):
		back_b=Button(root,text="<<",pady=20,state=DISABLED)
	forward_b.grid(row=0,column=2)
	back_b.grid(row=0,column=0)
	label.grid(row=0,column=1)



#initial definition of the keys on the screen.
forward_b=Button(root,text=">>",pady=20,command=lambda:forward(2))
back_b=Button(root,text="<<",pady=20,state=DISABLED,command=lambda:back())

exit_b=Button(root,text="EXIT",padx=30,command=root.quit)

#gridding or configuring the position of the buttons on the screen.
forward_b.grid(row=0,column=2)
back_b.grid(row=0,column=0)
exit_b.grid(row=1,column=1)

#put a mainloop over the tk() window created named as root.
root.mainloop()