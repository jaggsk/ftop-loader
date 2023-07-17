import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
from functools import partial

import pandas as pd
import numpy as np
#import re
import os
import traceback
#import math

#link to gui functions
import sns_formation_top_dictionary as sftd
import template_load as tl
from top_formats import *
import help_file_gif as hfg



class formtop_load_gui:
    
    '''
    list_filter_frame(): function to add labelframes, text box, label and list box to frame 2
    well_list(): import nsta sourced csv file containing all the uk well names and add to 
    listbox_check_input(event): Function to filter list box using a keyboard event bind from a textbox 
    '''

    def __init__(self):


        #main window parameters
        self.main_window_x = 800
        self.main_window_y = 800
        self.window_title = "Petrel Format Formation Top Loader"

        #frame dimensions
        self.frame_rbuttons_w = 300
        self.frame_rbuttons_h = 70

        self.frame_wells_w = 300
        self.frame_wells_h = 640

        self.frame_buttons_w = 300
        self.frame_buttons_h = 70

        self.frame_dataentry_w = 500
        self.frame_dataentry_h = 800

        self.well_csv_id = 'ndr_well_data_list.csv'

        #read predefined formation tops list from sns_formation_top_dictionary
        self.form_top_list = sftd.form_top_dict()
        self.form_top_dict = self.form_top_list.sns_create_dict() 
        self.form_top_dict_keys_list = list(self.form_top_dict.keys())

        #read predefined templates
        self.get_templates = tl.read_templates()
        print(self.get_templates )
        self.template_dict = self.get_templates.generate_templates("templates.txt")
        #print(self.template_dict)

        #Number of data entry boxes
        self.no_combo_boxes = 70

        #file address locations
        self.inpath = "H:\Documents"
        self.outpath = "H:\Documents"

        #get current user name
        self.user_string = os.getenv('username')

    def main_gui(self):
        '''
        Function to create main gui window
        All code related to root object should be placed here.
        '''

        #instantiate main window
        self.root = tk.Tk()
        self.root.title(self.window_title)
        
        #define window size and make it fixed
        self.root.resizable(False,False)
        self.root.geometry(str(self.main_window_x) + "x" + str(self.main_window_y))

        self.menu_gui()
        self.frames_gui()
        self.elevation_units_frame()
        self.list_filter_frame()
        self.button_frame()
        self.combobox_frame()

        self.well_list()

        #self.dummy_load()

        #self.root.iconphoto(False, tk.PhotoImage(file='H:\Python\iepg\Formation Top Loader\doge_icon.PNG'))
        #self.root.iconphoto(False, tk.PhotoImage(file='.\\Config\\doge_icon.PNG'))
        self.root.iconphoto(False, tk.PhotoImage(file=os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'Config', 'doge_icon.PNG')))
        

        self.root.mainloop()

    def menu_gui(self):
        '''
        Function to add menubar items to gui
        All code related to menubar items and binding should be placed here.
        '''

        #add menu bar
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        #add 'file' heading
        self.file_menu = tk.Menu(self.menubar, tearoff=False)

        #add file menu items and binding where required
        self.file_menu.add_command(
            label='Exit',
            command=self.root.destroy,
        )

        self.menubar.add_cascade(
            label="File",
            menu=self.file_menu,
            underline=1
        )
         
        #add template menu items - binding is through command 
        self.template_menu = tk.Menu(self.menubar, tearoff=False)
        self.template_menu.add_command(
            label='Cavendish',
            command =lambda: self.combobox_template_fill("'Cavendish Area'"),
        )
        self.template_menu.add_command(
            label='Breagh',
            command =lambda: self.combobox_template_fill("'Breagh Area'"),
        )        
        self.template_menu.add_command(
            label='Clipper',
            command =lambda: self.combobox_template_fill("'Clipper Area'"),
        )    
        #self.template_menu.add_command(
        #    label='Clipper Reservoir',
        #    command =lambda: self.combobox_template_fill("'Clipper Reservoir'"),
        #)  
        #self.template_menu.add_command(
        #    label='Breagh Reservoir',
            #command =lambda: self.combobox_template_fill("'Breagh Reservoir'"),
        #)
        self.template_menu.add_separator()      
        #option to clear the current user inputs
        self.template_menu.add_command(
            label='Clear',
            command =lambda: self.combobox_template_clear(),
        )

        self.menubar.add_cascade(
            label="Templates",
            menu=self.template_menu,
            underline=4
        )

        #add help menu items and binding where equired
        self.help_menu = tk.Menu(self.menubar, tearoff=False)
        self.help_menu.add_command(
            label='Help',
            #lambda: self.combobox_template_fill("'Cavendish Area'")
            command = lambda: hfg.play_help_gif()
            #command = self.root.bind('<<MenuSelect>>', openNewWindow)
            #command=root.bind(),
        )
 
        self.menubar.add_cascade(
            label="Help",
            menu=self.help_menu,
            #underline=0
        )

    


    def frames_gui(self):
        '''
        Function to create four main frames
        All code related to these objects should be placed here.
        '''
        self.frame1 = tk.Frame(self.root, width = self.frame_rbuttons_w, height = self.frame_rbuttons_h)
        #self.frame1 = tk.Frame(self.root, width = self.frame_rbuttons_w, height = self.frame_rbuttons_h, bg = 'blue')
        self.frame2 = tk.Frame(self.root, width = self.frame_wells_w, height = self.frame_wells_h)
        #self.frame2 = tk.Frame(self.root, width = self.frame_wells_w, height = self.frame_wells_h, bg= 'red')
        self.frame3 = tk.Frame(self.root, width = self.frame_buttons_w, height = self.frame_buttons_h)
        #self.frame3 = tk.Frame(self.root, width = self.frame_buttons_w, height = self.frame_buttons_h, bg = 'pink')
        self.frame4= tk.Frame(self.root, width = self.frame_dataentry_w, height = self.frame_dataentry_h)
        #self.frame4= tk.Frame(self.root, width = self.frame_dataentry_w, height = self.frame_dataentry_h, bg = 'green')

        self.frame1.grid(row =0, column = 0, padx = 5, pady = 5, sticky='nsew', columnspan = 2)
        self.frame2.grid(row =1, column = 0, sticky='nsew', columnspan = 2)
        self.frame3.grid(row =2, column = 0, sticky='nsew', columnspan = 2)
        self.frame4.grid(row =0, column = 2, sticky='nsew', rowspan = 3)


    def elevation_units_frame(self):
        '''
        Radio buttons to determine input and outp units in either feet or metres 
        '''
        self.buttonframe1_label = tk.LabelFrame(self.frame1, text='Select input units')
        self.buttonframe1_label.grid(column=0, row=0, ipadx=72, ipady=38)
        self.buttonframe2_label = tk.LabelFrame(self.frame1, text='Select output units')

        self.buttonframe2_label.grid(column=1, row=0,  ipadx=72, ipady=38)
   
        self.radio_in = tk.IntVar()
        self.radio_out = tk.IntVar()

        # Define radiobutton for input options
        self.r1 = tk.Radiobutton(self.buttonframe1_label, text="Feet", variable=self.radio_in, value=1, command=self.rselection)
        self.r1.place(x=5, y=5,width=60, height=20)
        self.r1.select()

        self.r2 = tk.Radiobutton(self.buttonframe1_label, text="Metres", variable=self.radio_in, value=2, command=self.rselection)
        self.r2.place(x=12, y=30,width=60, height=20)   

        # Define radiobutton for output options
        self.r3 = tk.Radiobutton(self.buttonframe2_label, text="Feet", variable=self.radio_out, value=1, command=self.rselection)
        self.r3.place(x=5, y=5,width=60, height=20)
        self.r3.select()
 
        self.r4 = tk.Radiobutton(self.buttonframe2_label, text="Metres", variable=self.radio_out, value=2, command=self.rselection)
        self.r4.place(x=12, y=30,width=60, height=20)  
    

    def list_filter_frame(self):
        '''
        function to add labelframes, text box, label and list box to frame 2
        List box is populated by well list exported from NDR database
        Text box is used to filter this list
        '''

        self.frame2.columnconfigure(0, weight = 1)
        self.frame2.rowconfigure(1, weight = 1)

        self.frame2_label = tk.LabelFrame(self.frame2, text='Select associated Well ID')
        #self.frame2_label.pack(fill="both", expand="yes")
        #self.frame2_label.pack(fill="both")
        self.frame2_label.grid(column=0, row=1, ipadx=144, ipady=317,columnspan = 2)

        self.filt_label = tk.Label(self.frame2_label, text='Filter well list')
        self.filt_label.place(x = 10, y= 5)

        # Create text widget and specify size.
        self.T = tk.Text(self.frame2_label)
        self.T.place(x = 10, y = 30, height = 25, width = 260)
        self.T.bind('<KeyRelease>', self.listbox_check_input)

        self.well_listbox = tk.Listbox(self.frame2_label)
        self.well_listbox.place(x = 10, y = 70,width=260, height=530)

        # Creating a Scrollbar and 
        # attaching it to root window
        self.scrollbar = tk.Scrollbar(self.well_listbox, orient="vertical")
        self.scrollbar.config(command=self.well_listbox.yview)
        # Adding Scrollbar to the right
        # side of root window
        self.scrollbar.pack(side = tk.RIGHT, fill=tk.BOTH)
        self.well_listbox.config(yscrollcommand=self.scrollbar.set)
   

    def button_frame(self):
        '''
        function to add Buttons to frame 3
        1 Button to generate tops text files
        1 Button to import text file - to do
        '''
        #self.frame3.columnconfigure(0, weight = 1)
        #self.frame3.rowconfigure(1, weight = 1)
        self.btn_ok = tk.Button(self.frame3, text = 'Generate Formation Tops')
        self.btn_ok.place(x = 5, y = 10, height = 50, width = 145)
        self.btn_ok.bind("<Button-1>", lambda:  self.create_form_tops_file("test"))
        self.btn_ok.bind("<Button-1>", self.create_form_tops_file)

        self.btn_load = tk.Button(self.frame3, text = 'Load Formation Tops')
        self.btn_load.place(x = 152, y = 10, height = 50, width = 145)
        self.btn_load.bind("<Button-1>", self.load_form_tops_file)

    def combobox_frame(self):
        '''
        Frame to hold multiple comboboxes and list boxes
        Conmboboxes populated by the predefined list of tops
        Each box bound to and event which filters the list of tops for each new character added.
        '''
        #self.frame4_label = tk.LabelFrame(self.frame4, text='Enter formation top ID and depths')
        #self.frame4_label.place(x=10, y=50, height = 740, width = 480)

        self.frame5 = tk.Frame(self.frame4)
        self.frame5.place(x=10, y=50, height = 740, width = 480)

        self.canvas_frame = tk.Canvas(self.frame5)
        self.scrollbar_combo = tk.Scrollbar(self.frame5, orient="vertical", command = self.canvas_frame.yview)
        self.canvas_frame_scrollable = tk.Frame(self.canvas_frame)

        self.canvas_frame_scrollable.bind(
            "<Configure>",
            lambda e: self.canvas_frame.configure(
            scrollregion=self.canvas_frame.bbox("all")
            )
        )

        self.canvas_frame.create_window((0,0), window=self.canvas_frame_scrollable, anchor='nw')
        self.canvas_frame.configure(yscrollcommand =  self.scrollbar_combo.set)
        self.scrollbar_combo.place(x = 0, y =0, relheight=1.0)
        self.canvas_frame.place(x = 0, y =0, relheight=1.0, relwidth=1.0)

        #self.canvas_frame_int = tk.Frame(self.canvas_frame)
        
        #self.bind_class("mytag", "<KeyRelease>", self.combobox_check_input)

        self.box_dict = {}
        self.text_dict = {}
        
        for i in range(self.no_combo_boxes):

            #self.box = ttk.Combobox(self.frame5)
            self.box = ttk.Combobox(self.canvas_frame_scrollable)
            
            self.box_dict[i] = self.box
            #new_tag = self.box_dict[i].bindtags()+()
            self.box_dict[i].unbind_class("TCombobox", "<MouseWheel>")
            self.box_dict[i].bind('<KeyRelease>', self.combobox_check_input)
            self.box.grid(column=1, row=i+1, sticky=tk.W, ipadx = 50, padx=25, pady=5)

            #self.Tbox = tk.Entry(self.frame5, width = 15, textvariable =i)
            self.Tbox = tk.Entry(self.canvas_frame_scrollable, width = 20, textvariable =i)
            self.text_dict[i] = self.Tbox
            self.Tbox.grid(column=2, row=i+1, sticky=tk.W, padx=5, pady=5)

        for k in range(len(self.box_dict)):
            self.box_dict[k]['values'] = self.form_top_dict_keys_list
    
    
    def combobox_check_input(self,event):
        '''
        Bind event to filter the dropdown menu of comboboxes
        '''

        value = event.widget.get()
        #print(value, i)
        
        #print(event.widget['values'])

        if value == '':
            #self.box_dict[i]['values'] = self.form_top_dict_keys_list
            event.widget['values'] = self.form_top_dict_keys_list
        else:
            #print(value)
            data = []
            for item in self.form_top_dict_keys_list:
                if value.lower() in item.lower():
                    data.append(item)
                    event.widget['values'] = data

    def combobox_template_clear(self):
        '''
        function to clear rows of comboboxes and associated text boxes
        '''
        for cnt_combobox_clear in range(self.no_combo_boxes):
            self.box_dict[cnt_combobox_clear].set('')
            self.text_dict[cnt_combobox_clear].delete(0,"end")


    def combobox_template_fill(self, template_key):
        '''
        function to fill rows of comboboxes with a pre defined template
        '''
        self.combobox_template_clear()
        #print(self.template_dict.keys())

        for i in range(len(self.template_dict[template_key])):
        #    #print(i)
            #print(self.template_dict[template_key][i].strip('\''))
            #print(re.findall(r"'(.*?)'", self.template_dict[template_key][i], re.DOTALL))
            self.box_dict[i].set(self.template_dict[template_key][i].strip('\''))   

    def rselection(self):
        '''
        Placeholder for future functionality required with depth units radiobuttons
        '''
        #print("hello")
        pass


    def well_list(self):
        '''
        Function to retrieve the well list from a csv file, generated from NSTA list, and add it to the listbox in panel #2
        https://ndr.nstauthority.co.uk/
        Project type - wellbore
        Sort on well ID , Export all to csv - keep header names
        H:\Python\iepg\Formation Top Loader\ndr_well_data_list.csv
        '''
        
        #csv file deined as 
        #csv_well_path = os.path.join(os.path.dirname(__file__), self.well_csv_id)
        #csv_well_path = '.\\Config\\ndr_well_data_list.csv'
        csv_well_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'Config', 'ndr_well_data_list.csv')
        #read csv to pandas and export 'Well ID' column to list
        df = pd.read_csv(csv_well_path)
        self.well_list_all = df['Well ID'].tolist()

        #iterate through list and add values to listbox
        for values in range(len(self.well_list_all)):
            well_string_temp = self.well_list_all[values]
            well_string_temp = well_string_temp.strip()
            self.well_listbox.insert(tk.END, well_string_temp)


    def listbox_check_input(self,event):
        '''
        Function to filter list box using a keyboard event bind from a textbox 
        '''
        
        #get string from textbox every timer a character is added or deleted. Remove newline characters
        value = self.T.get("1.0",tk.END)
        value = value.replace('\n','')

        #if return is empty repopulate with original well list file
        if value == '':
            self.well_listbox.delete('0',tk.END)
            for values in range(len(self.well_list_all)):
                self.well_listbox.insert(tk.END, self.well_list_all[values])
        #else filter well list file is pattern match is observed
        else:
            data = []
            self.well_listbox.delete('0',tk.END)
            for item in self.well_list_all:
                #print(item)
                if value.lower() in item.lower():
                    data.append(item)
                    self.well_listbox.insert(tk.END, item )

    def dummy_load(self):
        '''
        Fills in all combo boxes plus text boxes for quick function tests
        '''
        #print(self.form_top_dict_keys_list)
        ref_depth =1000
        for cnt_combobox_add in range(self.no_combo_boxes):
            self.box_dict[cnt_combobox_add].set(self.form_top_dict_keys_list[cnt_combobox_add])
            self.text_dict[cnt_combobox_add].insert(tk.END, ref_depth)
            #.set(self.form_top_dict_keys_list[cnt_combobox_add])
            ref_depth += 200
    
    
    def create_form_tops_file(self, event):
        '''
        Function to create output text file
        Read the combo boxes and text boxes and output contents to pandas dataframe

        '''

        #clear the terminal window
        #clear = lambda : os.system('tput reset')
        #clear()

        #obtain the selected well id
        #error raised if not selected
        try:
            self.well_id = self.well_listbox.get(self.well_listbox.curselection())
            #print(self.well_listbox.get(self.well_listbox.curselection()))
        except tk.TclError:
            tk.messagebox.showerror("Input Error", "No well selected!")
        
        print("Selected well ID = ", self.well_id) 

        #remove unwanted characters from well id string to create a valid output file name
        self.clean_well_id()
        


        #create output path file names for all top variations
        #
        self.outpath_all = os.path.join(self.outpath, "Tops All")
        self.check_directory(self.outpath_all)
        self.outfile_tops_all = os.path.join(self.outpath_all, str(self.well_id_clean) + '_' + "Tops_All" + '.txt')
        
        self.outpath_epoch = os.path.join(self.outpath, "Tops Epoch")
        self.check_directory(self.outpath_epoch)
        self.outfile_tops_epoch = os.path.join(self.outpath_epoch, str(self.well_id_clean) + '_' + "Tops_Epoch" + '.txt')
        
        self.outpath_period = os.path.join(self.outpath, "Tops Period")
        self.check_directory(self.outpath_period)
        self.outfile_tops_period = os.path.join(self.outpath_period, str(self.well_id_clean) + '_' + "Tops_Period" + '.txt')
        
        self.outpath_series = os.path.join(self.outpath, "Tops Series")
        self.check_directory(self.outpath_series)
        self.outfile_tops_series = os.path.join(self.outpath_series, str(self.well_id_clean) + '_' + "Tops_Series" + '.txt')
        
        self.outpath_group = os.path.join(self.outpath, "Tops Groups")
        self.check_directory(self.outpath_group)
        self.outfile_tops_group = os.path.join(self.outpath_group, str(self.well_id_clean) + '_' + "Tops_Group" + '.txt')
        
        self.outpath_formation = os.path.join(self.outpath, "Tops Formations")
        self.check_directory(self.outpath_formation)
        self.outfile_tops_formation = os.path.join(self.outpath_formation, str(self.well_id_clean) + '_' + "Tops_Formation" + '.txt')

        self.outpath_member = os.path.join(self.outpath, "Tops Members")
        self.check_directory(self.outpath_member)
        self.outfile_tops_member = os.path.join(self.outpath_member, str(self.well_id_clean) + '_' + "Tops_Member" + '.txt')
        
        self.outpath_discontinuity = os.path.join(self.outpath, "Tops Discontinuity")
        self.check_directory(self.outpath_discontinuity)
        self.outfile_tops_discontinuity = os.path.join(self.outpath_discontinuity, str(self.well_id_clean) + '_' + "Tops_Discontinuity" + '.txt')
       
        #determine input and output units
        if self.radio_in.get() == 1:
            self.input_units_ft = True
            print("Selected input units = ft")
        else:
            self.input_units_ft = False
            print("Selected input units = m")

        if self.radio_out.get() == 1:
            self.output_units_ft = True
            print("Selected output units = ft")
        else:
            self.output_units_ft = False
            print("Selected output units = m")        

        #instantiate lists - populated by iterating through all the combo and text boxes
        #results will be added to new dataframe
        top_main_id = []
        top_period_id = []
        top_epoch_id = []
        top_series_id = []
        top_group_id = []
        top_formation_id = []
        top_member_id = []
        top_depth = []

        #iterate through every combo and list box - populate lists instantiated above
        for cnt_combobox_df in range(self.no_combo_boxes):
            if self.box_dict[cnt_combobox_df].get() != '':
                #print(self.form_top_dict[self.box_dict[cnt_combobox_df].get()][0],self.form_top_dict[self.box_dict[cnt_combobox_df].get()][5])
                top_main_id.append(self.box_dict[cnt_combobox_df].get())
                top_period_id.append(self.form_top_dict[self.box_dict[cnt_combobox_df].get()][0])
                top_epoch_id.append(self.form_top_dict[self.box_dict[cnt_combobox_df].get()][1])
                top_series_id.append(self.form_top_dict[self.box_dict[cnt_combobox_df].get()][2])
                top_group_id.append(self.form_top_dict[self.box_dict[cnt_combobox_df].get()][3])
                top_formation_id.append(self.form_top_dict[self.box_dict[cnt_combobox_df].get()][4])
                top_member_id.append(self.form_top_dict[self.box_dict[cnt_combobox_df].get()][5])
                top_depth.append(self.text_dict[cnt_combobox_df].get())

        #create new pandas dataframe and populate with lists 
        self.df_tops=pd.DataFrame({'Main':top_main_id,'Depth':top_depth,'Period':top_period_id,'Epoch':top_epoch_id,'Series':top_series_id,'Group':top_group_id,'Formation':top_formation_id,'Member':top_member_id})
        self.df_tops['Depth'].replace('', np.nan, inplace=True)
        self.df_tops.dropna(subset=['Depth'], inplace=True)
        #print(self.df_tops)
        #remove rows without depth data
        #self.df_tops =  self.df_tops[pd.to_numeric(self.df_tops['Depth'], errors='coerce').notnull()]
        self.df_tops['Depth'] = self.df_tops['Depth'].astype(float)
        #print(self.df_tops.info())
        self.df_tops = self.df_tops.sort_values(by = 'Depth', ascending = True)
        self.df_tops = self.df_tops.reset_index(drop = True) 
        #print(self.df_tops) 

        #change in string value is used to denote higher timeframe top surfaces e.g. Top Jurassic, Top Cretaceous etc.
        #e.g. change in epoch is marked by 1, 0 for columns with no change
        self.df_tops['Period Change'] = self.df_tops['Period'].ne(self.df_tops['Period'].shift().bfill()).astype(int)
        self.df_tops['Epoch Change'] = self.df_tops['Epoch'].ne(self.df_tops['Epoch'].shift().bfill()).astype(int)
        self.df_tops['Group Change'] = self.df_tops['Group'].ne(self.df_tops['Group'].shift().bfill()).astype(int)
        self.df_tops['Formation Change'] = self.df_tops['Formation'].ne(self.df_tops['Formation'].shift().bfill()).astype(int)
        #print(self.df_tops)

        #shift the period top - used to identify discontinuity
        #empty cell to host discontinuity ID
        self.df_tops['Period Discontinuity'] = self.df_tops['Period'].shift()
        self.df_tops['Discontinuity'] = ""

        #empty list for 
        create_message = []

        #create tops file for all user input tops

        self.df_all = self.df_tops.copy()
        #print("All", self.df_all.shape)
        if self.df_all.shape[0] > 0:
            self.write_tops_file(outpath = self.outfile_tops_all,df_out = self.df_all, tops_col = 'Main',depth_col = 'Depth')
            create_message.append(self.outfile_tops_all +"\n")

        
        #create tops file for period only user input tops
        self.df_period = self.df_tops.copy()
        if self.df_period.shape[0] > 0:
            self.df_period =  self.df_period[self.df_period['Period Change'] > 0]
            self.df_period = self.df_period.reset_index(drop = True) 
            self.write_tops_file(outpath = self.outfile_tops_period,df_out = self.df_period, tops_col = 'Period',depth_col = 'Depth')
            create_message.append(self.outfile_tops_period +"\n")

        #create tops file for epoch only user input tops
        self.df_epoch = self.df_tops.copy()
        if self.df_epoch.shape[0] > 0:
            self.df_epoch =  self.df_epoch[self.df_epoch['Epoch Change'] > 0]
            self.df_epoch = self.df_epoch.reset_index(drop = True) 
            self.write_tops_file(outpath = self.outfile_tops_epoch,df_out = self.df_epoch, tops_col = 'Epoch',depth_col = 'Depth')
            create_message.append(self.outfile_tops_epoch +"\n")

        #create tops file for series only user input tops
        self.df_series = self.df_tops.copy()
        if self.df_series.shape[0] > 0:
            self.df_series =  self.df_series[self.df_series['Epoch Change'] > 0]
            self.df_series = self.df_series.reset_index(drop = True) 
            self.write_tops_file(outpath = self.outfile_tops_series,df_out = self.df_series, tops_col = 'Series',depth_col = 'Depth')
            create_message.append(self.outfile_tops_series +"\n")


        #create tops file for group only user input tops
        self.df_group = self.df_tops.copy()
        self.df_group =  self.df_group[self.df_group['Group Change'] > 0]
        self.df_group = self.df_group.reset_index(drop = True) 
        
        if self.df_group.shape[0] > 0:
            self.write_tops_file(outpath = self.outfile_tops_group,df_out = self.df_group, tops_col = 'Group',depth_col = 'Depth')
            create_message.append(self.outfile_tops_group +"\n")

        #create tops file for formatrion only user input tops
        self.df_formation = self.df_tops.copy()
        self.df_formation =  self.df_formation[self.df_formation['Formation Change'] > 0]
        self.df_formation = self.df_formation.reset_index(drop = True)
        
        if self.df_formation.shape[0] > 0:
            self.write_tops_file(outpath = self.outfile_tops_formation,df_out = self.df_formation, tops_col = 'Formation',depth_col = 'Depth')
            create_message.append(self.outfile_tops_formation +"\n")

        #create tops file for formatrion only user input tops
        self.df_member = self.df_tops.copy()
        self.df_member =  self.df_member[self.df_member['Member'] != '']
        self.df_member = self.df_member.reset_index(drop = True) 
        if self.df_member.shape[0] > 0:
            self.write_tops_file(outpath = self.outfile_tops_member,df_out = self.df_member, tops_col = 'Member',depth_col = 'Depth')
            create_message.append(self.outfile_tops_member +"\n")
            create_message.append("\nSuccessfully Created!")
        
        #rslt_df = dataframe.loc[~dataframe['Stream'].isin(options)]
        self.df_tops.loc[(self.df_tops['Period Discontinuity'] == 'Permian') & (self.df_tops['Period'] == 'Carboniferous'), 'Discontinuity'] = "BPU"
        self.df_tops.loc[(self.df_tops['Period Discontinuity'] == 'Cretaceous') & (self.df_tops['Period'].isin(['Jurassic', 'Triassic'])), 'Discontinuity'] = "BCU"
        self.df_tops.loc[(self.df_tops['Period Discontinuity'] == 'Permian') & (self.df_tops['Period'].isin(['Cretaceous','Jurassic', 'Triassic'])), 'Discontinuity'] = "Salt"

        #create tops file for formatrion only user input tops
        self.df_discontinuity = self.df_tops.copy()
        self.df_discontinuity =  self.df_discontinuity[self.df_discontinuity['Discontinuity'] != ""]
        self.df_discontinuity = self.df_discontinuity.reset_index(drop = True) 
        
        if self.df_discontinuity.shape[0] > 0:
            self.write_tops_file(outpath = self.outfile_tops_discontinuity,df_out = self.df_discontinuity, tops_col = 'Discontinuity',depth_col = 'Depth')
            create_message.append(self.outfile_tops_discontinuity +"\n")
            create_message.append("\nSuccessfully Created!")

        

        #print(self.df_tops[['Period','Period Discontinuity', 'Discontinuity']])
        #issue messagebox to user showing the output locations
        
        if len(create_message) > 0:
            tk.messagebox.showinfo("Files Created",create_message)
        else:
            tk.messagebox.showinfo("Files Created","No files generated")

        #return break releases the button once the function is finished
        #without this - button remains pressed.
        return "break"

    def load_form_tops_file(self, event):

        print("load data")
        return "break"

    def clean_well_id(self):
        '''
        remove unwatnted characters from well id for putposes of creating an output file name
        example \ is replaced with _
        '''
        #remove unwanted characters
        self.well_id_clean = self.well_id

        #replace all spaces
        self.well_id_clean = self.well_id_clean.replace(' ','')
        
        #remove rogue characters and replace with underscore for final file name
        chars = "/\`*_{}[]()>#+-.!$"                   
        for ch in chars:
            #print(ch,self.well_id_clean[0])
            if ch in  self.well_id_clean:     
                self.well_id_clean = self.well_id_clean.replace(ch,'_')


    def write_tops_file(self, outpath = '', df_out = '', tops_col = '', depth_col = ''):
        '''
        (string)(pandas dataframe)(string)(string)
        outpath = directory/file path name for output file
        df_out = pandas dataframe containing tops and depth
        tops_col = dataframe column name for required tops
        depth_col = dataframe column name for required depth

        function to write the tops file
        currently defaults to Petrel format header
        depth converted between units if required
        PRECONDITION input database has been filtered to required untis only.
        '''
        #obtain correct text header from tops_header_file subroutine
        #boolean operator indicates if output is in feet or metres
        self.text_header = petrel_tops_header_file(feet = self.output_units_ft)

        file_writer = open(outpath,"w") 

        #iterate trhough header file - stored as a list - line by line and write to the open writer
        for i in range(len(self.text_header)):
            #write current header line to text file
            file_writer.write(str(self.text_header[i]) + "\n") 

        #iterate through all the active rows in the spreadsheet
        for j in range(df_out.shape[0]):
            #find only instances where values are not nan i.e. left blank by user
            #if math.isnan(df_out.loc[j][depth_col]) == False :

            #extract top id and depth for qc (if require) and conversion purposes
            top_temp = df_out.loc[j][tops_col]
            #print(top_temp)
            depth_temp = float(df_out.loc[j][depth_col])

            #convert depth if input = feet and output = metres
            if self.input_units_ft == True and self.output_units_ft == False:
                depth_temp = round(depth_temp/3.2808399,2)
                #print(depth_temp)

            #convert depth if input = metres and output = feet
            if self.input_units_ft == False and self.output_units_ft == True:
                depth_temp = round(depth_temp * 3.2808399,2)
                #print(depth_temp)

            #write file output for md top author and well id - attach double quotes to strings for consistency    
            if top_temp != "":
                print(top_temp)           
                file_writer.writelines([str(depth_temp), " ", self.double_quote(top_temp) , " " , self.double_quote(self.well_id.lstrip(' ')) ," ", self.double_quote(self.user_string) ,"\n"] )



    def double_quote(self, word):
        '''
        Adds double quotes to a string to avoid triggering an error at run time whilst writing text to files.
        '''
        return '"%s"' % word  

    
    def show_error(self, *args):
        '''
        Error catching text box - to ve further developed.
        '''
        err = traceback.format_exception(*args)
        tk.tkMessageBox.showerror('Exception',err)

    def check_directory(self, out_check):
        '''
        Check if the requested directory exists, if nto create it
        '''
        if os.path.isdir(out_check) == True:
            #print("Directpry Exists")
            pass
        else:
            #print("Creating Directpry")
            os.mkdir(out_check)

flg = formtop_load_gui()
flg.main_gui()


