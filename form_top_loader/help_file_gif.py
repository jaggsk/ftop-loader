from tkinter import *
import time
import os

def play_help_gif():
    root_help = Tk()
    root_help.title("OK BOOMER!")
    root_help.iconphoto(False, PhotoImage(file=os.path.join(os.path.dirname(__file__),'Config', 'doge_icon.PNG'),master = root_help))
    
    #root = Toplevel()

    #frames = [PhotoImage(file='H:\\Python\iepg\\Formation Top Loader\\ok_boomer.gif',format = 'gif -index %i' %(i), master = root_help) for i in range(10)]
    frames = [PhotoImage(file=os.path.join(os.path.dirname(__file__),'Config', 'ok_boomer.gif'),format = 'gif -index %i' %(i), master = root_help) for i in range(10)]
    def update(ind):
        frame = frames[ind]
        ind += 1
        #print(ind)
        if ind>9: #With this condition it will play gif infinitely
            ind = 0
        label.configure(image=frame)
        root_help.after(100, update, ind)

    label = Label(root_help)
    label.pack()
    root_help.after(0, update, 0)
    root_help.mainloop()

#play_help_gif()