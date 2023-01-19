     ##Importing Modules##

from faulthandler import disable
from sys import byteorder
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import database as db
from Constants import *
from tkinter import messagebox


     ##Success Output##

def messageboxy(floor=None):
        messagebox.showinfo(title = "Acknowledgment", message="Room Status has been Updated!") 
        floorscreen(floor)

     ##Room Information GUI##
    
def init_info_widgets(room_num, floor, type, status):
    icon=booking_icon
    lblfloor1= Label(info_frame, text=f"Room Number: {room_num}             ", font="Helvetica 15 bold", bg=COLOUR_A, fg=COLOUR_B)
    lblfloor1.place(x=10, y=200)
    lblfloor2= Label(info_frame, text=f"Floor: {floor}             ", font="Helvetica 15 bold", bg=COLOUR_A, fg=COLOUR_B)
    lblfloor2.place(x=10, y=230)
    lblfloor3= Label(info_frame, text=f"Room Type: {type}             ", font="Helvetica 15 bold", bg=COLOUR_A, fg=COLOUR_B)
    lblfloor3.place(x=10, y=260)
    lblfloor4= Label(info_frame, text=f"Room Status: {status}             ", font="Helvetica 15 bold", bg=COLOUR_A, fg=COLOUR_B)
    lblfloor4.place(x=10, y=290)
    Btn=Button(info_frame, font=myFont2, image=icon, borderwidth=0, height=100, width=150, text="Update Room \nStatus", compound="center", bg=SIDEBAR_COLOUR, bd=0, relief=FLAT, activebackground="black",  command=lambda: [db.updatestatus(room_num), messageboxy(floor)]).place(x=75, y=400)

     ##Fetching Data from Database##
     
def get_room_data(btn_text):
    data = db.fetchdata(int(btn_text.strip()))[0]
    if db.check_occ(int(btn_text)):
        occ="Occupied"
    else:
        occ="Vacant"
    init_info_widgets(data[0], data[1], data[2], occ)
    
     ##Room Number Creator##

def place_room_icons(floor_no, row, col):
    i = 1
    for y in range(row):
        for x in range(col):
            btn_text = f"{floor_no+i}"
            if db.check_occ(int(btn_text)):
                icon=occupied_icon
            else:
                icon=vacant_icon
            Button(option_frame, font=myFont, image=icon, borderwidth=0, height=100, width=150, text=btn_text,  compound="center", bg=OPTION_FRAME_COLOUR, bd=0, relief=FLAT, activebackground="black",  command=lambda text=btn_text: get_room_data(text)).place(x=19+(x*170), y=50+(200*y))
            i+=1

     ##Main GUI Interface##

def floorscreen(floor):
    floor_no = floor*100
    row, col = 3, 4

    place_room_icons(floor_no, row, col)

    lblfloor1= Label(option_frame, text=f"Floor {floor}", font="Helvetica 14 bold", bg=MID_FRAME_COLOUR)
    lblfloor1.place(relx=0.46, y=630)
    mainlbl1= Label(option_frame, text=f"ROOMS ON FLOOR {floor}", font="Helvetica 14 bold", bg=MID_FRAME_COLOUR, fg=SIDEBAR_COLOUR)
    mainlbl1.place(x=50, y=10)

     ##Toggle for Floor Switching##

def arrowchecker():
    global floor
    arrowbtnright.place(relx= 0.7, y=625)
    arrowbtnleft.place(relx= 0.56, y=625)
    if floor==1:
        arrowbtnleft['state']= DISABLED
    elif floor==floors:
        arrowbtnright['state'] = DISABLED
    else:
        arrowbtnright['state'] = ACTIVE
        arrowbtnleft['state']= ACTIVE

     ##Initiation of FLoor Switching##

def floorup():
    global floor
    floor+=1
    floorscreen(floor)
    arrowchecker()

def floordown():
    global floor
    floor-=1
    floorscreen(floor)
    arrowchecker()

     ##Constants##

iconsize = (150, 120)
arrowsize= (40,35)
floor=1
floors=4

     ##GUI Initiation##

win= Tk()
win.geometry("1000x700+500+150")
win.title("Hotel Management 2.7")

     ##Font Constants##

myFont = font.Font(size=20, family="Adobe Heiti Std R", weight="bold")
myFont2 = font.Font(size=10, family="Adobe Heiti Std R", weight="bold")

     ##GUI Building using Tkinter##

info_frame= Frame(win, bg=SIDEBAR_COLOUR)
info_frame.place(x=0, y=0, relwidth=0.3, relheight=1)
option_frame= Frame(bg=OPTION_FRAME_COLOUR)
option_frame.place(relx=0.3, rely= 0, relheight=1, relwidth=0.7)
colorframe1= Frame(option_frame, bg=MID_FRAME_COLOUR)
colorframe1.place(height=50, relwidth=1)
colorframe2= Frame(option_frame, bg= MID_FRAME_COLOUR)
colorframe2.place(y= 155, height=95, relwidth=1)
colorframe3= Frame(option_frame, bg= MID_FRAME_COLOUR)
colorframe3.place(y= 355, height=95, relwidth=1)
colorframe4= Frame(option_frame, bg= MID_FRAME_COLOUR)
colorframe4.place(y= 555, height=200, relwidth=1)

     ##Importing of program ##

vacant_icon= PhotoImage(file= r"UI Elements\vacant_icon.png")
occupied_icon= PhotoImage(file= r'UI Elements\occupied_icon.png')
booking_icon= PhotoImage(file= r'UI Elements\booking.png')
right_icon=PhotoImage(file=r"UI Elements\right_arrow.png")
left_icon=PhotoImage(file=r"UI Elements\left_arrow.png")
display1=PhotoImage(file=r"UI Elements\Display1.png")

arrowbtnleft= Button(height= 30, width=50, image= left_icon, borderwidth=0, command= lambda: floordown(), bg=MID_FRAME_COLOUR)
arrowbtnright= Button(height= 30, width=50, image= right_icon, borderwidth=0, command= lambda: floorup(), bg= MID_FRAME_COLOUR)

floorscreen(1)
arrowchecker()

win.mainloop()

