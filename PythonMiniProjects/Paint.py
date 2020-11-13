from tkinter import *
from tkinter.ttk import Scale

class Paint():
    def __init__(self,root):
        self.root=root
        self.root.title("Paint")
        self.root.geometry("800x520")
        self.root.config(background='purple')
        self.root.resizable(0,0)

        self.pen_color="black"

        #adding frame
        self.color_frame=LabelFrame(self.root,text="Color",font=('arial',15),bd=5,relief=RIDGE,bg='white')
        self.color_frame.place(x=0,y=0,width=70,height=205)

        colors=['#000000','#FFFFFF','#FF0000','#00FF00','#0000FF','#FFFF00','#00FFFF','#FF00FF','#F1510B','#CD9C10','#513D53','#4A7570']
        i=j=0

        for color in colors:
            Button(self.color_frame,bg=color,bd=2,relief=RIDGE,width=3,command=None).grid(row=i,column=j)
            i+=1
            if i==6:
                i=0
                j+=1


        self.eraser_button=Button(self.root,text="ERASER",bd=4,bg='white',command=None,width=8,relief=RIDGE)
        self.eraser_button.place(x=0,y=205)

        self.eraser_button = Button(self.root, text="Clear", bd=4, bg='white', command=None, width=8, relief=RIDGE)
        self.eraser_button.place(x=0, y=235)

        self.eraser_button = Button(self.root, text="Save", bd=4, bg='white', command=None, width=8, relief=RIDGE)
        self.eraser_button.place(x=0, y=265)

        self.eraser_button = Button(self.root, text="Canvas", bd=4, bg='white', command=None, width=8, relief=RIDGE)
        self.eraser_button.place(x=0, y=295)

        self.pen_size_scale_frame = LabelFrame(self.root, text="Size", bd=5, bg='white', font=('arial', 15,'bold'), relief=RIDGE)
        self.pen_size_scale_frame.place(x=0, y=325, width=70, height=195)

        self.pen_size=Scale(self.pen_size_scale_frame,orient=VERTICAL,from_=50,to=0,length=150)
        self.pen_size.set(1)
        self.pen_size.grid(row=0,column=1,padx=15)


        self.canvas=Canvas(self.root,bg='white',bd=5,relief=GROOVE,height=505,width=715)
        self.canvas.place(x=70,y=0)


        self.canvas.bind("<B1-Motion>",self.paint)


    def paint(self,event):
        x1,y1=(event.x-2),(event.y-2)
        x2,y2=(event.x+2),(event.y+2)


        self.canvas.create_oval(x1,y1,x2,y2,fill=self.pen_color,outline=self.pen_color,width=self.pen_size.get())

if __name__=="__main__":
    root=Tk()
    p=Paint(root)
    root.mainloop()

