from tkinter import *
from tkinter import filedialog
from tkinter import font
import docx
import PyPDF2





root=Tk()
root.title('Word Clone')
# root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.iconbitmap('c:/Users/DEVANSH/Downloads/word.ico')

global open_status_name
open_status_name= False

global selected
selected=False

#Create New File Function
def new_file():

    my_text.delete("1.0",END)   #delete previous text
    root.title('New File')      
    status_bar.config(text="New File        ")    #updates status bar
    global open_status_name
    open_status_name= False


#Open Files
def open_file(e):
    my_text.delete("1.0",END)   #delete previous text
    #Grab File
    text_file=filedialog.askopenfilename(initialdir="C:/Users/DEVANSH/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Word File", "*.docx"),("All Files", "*.*")))
    
    #Check to see if there is file name
    if text_file:
        #Make file name global so we can access it later
        global open_status_name
        open_status_name= text_file

    #Update Status Bars
    name=text_file
    status_bar.config(text=f'{name}    ')
    name = name.replace("C:/Users/DEVANSH/", " ")
    root.title(f'{name}')

    #Open the file
    text_file=open(text_file, 'r')
    content=text_file.read()
    #Add file to Textbox
    my_text.insert(1.0,content)
    #Close the opened file
    text_file.close()

    

    
    

#Save As File
def save_as_file():
    text_file=filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Users/DEVANSH/", title="Save File", filetypes=(("Text Files", "*.txt"),("HTML Files", "*.html"), ("Word File", "*.docx"), ("All Files", "*.*")))
    if text_file:
        name=text_file
        status_bar.config(text=f'Saved : {name}    ')
        name = name.replace("C:/Users/DEVANSH/", " ")
        root.title(f'{name}')

    #Save the file
    text_file=open(text_file, 'w')
    text_file.write(my_text.get("1.0",END))
    text_file.close()

#Save File
def save_file(e):
    global open_status_name
    if open_status_name:
        #Save the file
        text_file=open(open_status_name, 'w')
        text_file.write(my_text.get("1.0",END))
        text_file.close()

        status_bar.config(text=f'Saved : {open_status_name}    ')
    else:
        save_as_file()

#Cut Text
def cut_text(e):
    global selected
    #check to see if we used keyboard shortcut
    if e:
        selected=root.clipboard_get()
    if my_text.selection_get():
        #Grab Selected text from text box
        selected=my_text.selection_get()
        #Delete selected text from textbox
        my_text.delete("sel.first","sel.last")
        #clear the clipboard and then append
        root.clipboard_clear()
        root.clipboard_append(selected)

#Copy Text
def copy_text(e):
    global selected
    #check to see if we used keyboard shortcut
    if e:
        selected=root.clipboard_get()
    else:
        if my_text.selection_get():
            #Grab Selected text from text box
            selected=my_text.selection_get()
            #clear the clipboard and then append
            root.clipboard_clear()
            root.clipboard_append(selected)


#Paste Text
def paste_text(e):
    global selected
    #check to see if we used keyboard shortcut
    if e:
        selected=root.clipboard_get()
    else:
         if selected:
            position=my_text.index(INSERT)
            my_text.insert(position,selected)

#Bold Text
def bold_it():
    #Create our font
    bold_font=font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    italic_bold_font=font.Font(my_text, my_text.cget("font"))
    italic_bold_font.configure(slant="italic", weight="bold")

    bold_underline_font=font.Font(my_text, my_text.cget("font"))
    bold_underline_font.configure(weight="bold", underline=True)

    italic_bold_underline_font=font.Font(my_text, my_text.cget("font"))
    italic_bold_underline_font.configure(underline=True, slant="italic" , weight="bold")

    italic_underline_font=font.Font(my_text, my_text.cget("font"))
    italic_underline_font.configure(slant="italic", underline=True)


    #Configure a tag
    my_text.tag_configure("bold", font=bold_font)
    #Define Current tags
    current_tags=my_text.tag_names("sel.first")

    #If statement to see if tag has been set 
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    elif "italic" in current_tags:
        my_text.tag_configure("bold italic", font=italic_bold_font)
        my_text.tag_add("bold italic", "sel.first", "sel.last")
    elif "underline" in current_tags:
        my_text.tag_configure("underline bold", font=bold_underline_font)
        my_text.tag_add("underline bold", "sel.first", "sel.last")
    elif "underline italic" in current_tags:
        my_text.tag_configure("underline italic bold", font=italic_bold_underline_font)
        my_text.tag_add("underline italic bold", "sel.first", "sel.last")
    elif "italic underline" in current_tags:
        my_text.tag_configure("italic underline bold", font=italic_bold_underline_font)
        my_text.tag_add("italic underline bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")

    
#Italic Text
def italic_it():
    #Create our font
    italic_font=font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant="italic")

    italic_bold_font=font.Font(my_text, my_text.cget("font"))
    italic_bold_font.configure(slant="italic", weight="bold")

    italic_underline_font=font.Font(my_text, my_text.cget("font"))
    italic_underline_font.configure(slant="italic", underline=True)

    italic_bold_underline_font=font.Font(my_text, my_text.cget("font"))
    italic_bold_underline_font.configure(slant="italic", underline=True, weight="bold")

    bold_underline_font=font.Font(my_text, my_text.cget("font"))
    bold_underline_font.configure(underline=True, weight="bold")

    #Configure a tag
    my_text.tag_configure("italic", font=italic_font)
    my_text.tag_configure("bold italic", font=italic_bold_font)
    my_text.tag_configure("underline italic", font=italic_bold_font)
    #Define Current tags
    current_tags=my_text.tag_names("sel.first")
    

    #If statement to see if tag has been set 
    if "italic" in current_tags:
       my_text.tag_remove("italic", "sel.first", "sel.last")
    elif "bold" in current_tags:
        my_text.tag_configure("bold italic", font=italic_bold_font)
        my_text.tag_add("bold italic", "sel.first", "sel.last")
    elif "underline" in current_tags:
        my_text.tag_configure("italic underline", font=italic_underline_font)
        my_text.tag_add("italic underline", "sel.first", "sel.last")
    elif "bold underline" in current_tags:
        my_text.tag_configure("underline italic bold", font=italic_bold_underline_font)
        my_text.tag_add("underline italic bold", "sel.first", "sel.last")
    elif "underline bold" in current_tags:
        my_text.tag_configure("underline italic bold", font=italic_bold_underline_font)
        my_text.tag_add("underline italic bold", "sel.first", "sel.last")

    else:
        my_text.tag_add("italic", "sel.first", "sel.last")

    
    
#Underline text
def underline_it():
    #Create Our Font
    underline_font=font.Font(my_text, my_text.cget("font"))
    underline_font.configure(underline=True)

    bold_underline_font=font.Font(my_text, my_text.cget("font"))
    bold_underline_font.configure(weight="bold", underline=True)

    italic_underline_font=font.Font(my_text, my_text.cget("font"))
    italic_underline_font.configure(slant="italic", underline=True)

    italic_bold_underline_font=font.Font(my_text, my_text.cget("font"))
    italic_bold_underline_font.configure(slant="italic", underline=True, weight="bold")

    italic_bold_font=font.Font(my_text, my_text.cget("font"))
    italic_bold_font.configure(slant="italic", weight="bold")


    #Configure a tag
    my_text.tag_configure("underline", font=underline_font)
    #Define Current Tags
    current_tags=my_text.tag_names("sel.first")


    #If statement to see if tag has been set 
    if "underline" in current_tags:
        my_text.tag_remove("underline", "sel.first", "sel.last")
    elif "bold" in current_tags:
        my_text.tag_configure("underline bold", font=bold_underline_font)
        my_text.tag_add("underline bold", "sel.first", "sel.last")
    elif "italic" in current_tags:
        my_text.tag_configure("underline italic", font=italic_underline_font)
        my_text.tag_add("underline italic", "sel.first", "sel.last")
    elif "bold italic" in current_tags:
        my_text.tag_configure("italic bold underline", font=italic_bold_underline_font)
        my_text.tag_add("italic bold underline", "sel.first", "sel.last")
    elif "italic bold" in current_tags:
        my_text.tag_configure("underline italic bold", font=italic_bold_underline_font)
        my_text.tag_add("underline italic bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("underline", "sel.first", "sel.last")




def font_chooser(e):
    our_font.config(family=font_listbox.get(font_listbox.curselection()))
    my_text.config(font=our_font)


def size_chooser(e):
    our_font.config(size=size_listbox.get(size_listbox.curselection()))
    my_text.config(font=our_font)

def font_window():
    global our_font
    global font_listbox
    global size_listbox
    top=Toplevel()
    top.title('Change Font')
    top.iconbitmap('c:/Users/DEVANSH/Downloads/font-size.ico')
    #top.geometry("800x800")
    our_font=font.Font(family="Helvetica", size=32)
    font_frame=Frame(top, width=480, height=275)
    font_frame.pack(pady=10)
    font_frame.grid_propagate(False)
    #font_frame.columnconfigure(0,weight=10)
    font_textbox=Label(font_frame, font=our_font, text="This is Your Text")
    font_textbox.grid(row=0, column=0)
    # font_textbox.grid_rowconfigure(0,weight=1)
    # font_textbox.grid_columnconfigure(0,weight=1)

    

    #bottom frame 
    bottom_frame=Frame(top)
    bottom_frame.pack()

    #Add Label
    font_label=Label(bottom_frame, text="Choose font")
    font_label.grid(row=0,column=0)

    size_label=Label(bottom_frame, text="Font size")
    size_label.grid(row=0,column=1)

    # font_scroll=Scrollbar(bottom_frame)
    # font_scroll.pack(side=RIGHT, fill=Y)

    #add Size to size listbox
    font_sizes=(8,10,12,16,14,18,20,22,24,26,28,30,32)


    #Create Font list box
    font_listbox=Listbox(bottom_frame, selectmode=SINGLE)
    font_listbox.grid(row=1,column=0)
    # font_scroll.configure(command=font_listbox.yview)

    #create Size listbox
    size_listbox=Listbox(bottom_frame, selectmode=SINGLE)
    size_listbox.grid(row=1,column=1)
    # font_scroll.configure(command=size_listbox.yview)
    
    #add Font families to font listbox
    for f in font.families():
        font_listbox.insert('end',f)

    for size in font_sizes:
        size_listbox.insert('end',size)

    font_listbox.bind('<ButtonRelease-1>', font_chooser)
    size_listbox.bind('<ButtonRelease-1>', size_chooser)

    ok_button=Button(bottom_frame, text="Ok", command=top.destroy)
    ok_button.grid(row=2,column=2,sticky=E)

def find():
    my_text.tag_remove('found','1.0',END)
    s=find_box.get()
    if(s):
        idx=1.0
        while 1:
            idx=my_text.search(s, idx, nocase = 1,stopindex = END)
            if not idx: break

            lastidx='% s+% dc' % (idx,len(s))    
            my_text.tag_add('found', idx,lastidx)   
            idx=lastidx    

        my_text.tag_config('found', foreground ='red')
    find_box.focus_set()                 

def replace():
    my_text.tag_remove('found', '1.0',END)
    s=find_box.get()
    r=replace_box.get()

    if(s and r):
        idx='1.0'

        while 1:
            idx=my_text.search(s,idx,nocase=1,stopindex=END)
            print(idx)

            if not idx: break
            lastidx = '% s+% dc' % (idx, len(s))
            my_text.delete(idx,lastidx)
            my_text.insert(idx,r)

            lastidx = '% s+% dc' % (idx, len(r))

            my_text.tag_add('found', idx,lastidx)
            idx=lastidx

        my_text.tag_config('found', foreground ='green')
    replace_box.focus_set()

def open_pdf():
    my_text.delete("1.0",END)   #delete previous text
    #Grab File
    pdf_file=filedialog.askopenfilename(initialdir="C:/Users/DEVANSH/", title="Open File", filetype=(("PDF file", "*.pdf"),("All Files", "*.*")))

    if pdf_file:

        file=PyPDF2.PdfFileReader(pdf_file)
        page= file.getPage(0,END)
        content=page.extractText()
        my_text.insert(1.0,content)

#Create toolbar frame
toolbar_frame=Frame(root)
toolbar_frame.pack(fill=X)




#Create Main Frame
my_frame=Frame(root,width=480,height=275)
my_frame.pack(pady=5)
my_frame.grid_propagate(False)
my_frame.columnconfigure(0,weight=10)

#Create Scroll bar
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)


#Create Text Box
my_text=Text(my_frame,selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set,height=1000, width=1000)
my_text.grid_rowconfigure(0,weight=1)
my_text.grid_columnconfigure(0,weight=1)
my_text.pack(fill="both", expand=True)


#Configure Our Scrollbar
text_scroll.configure(command=my_text.yview)

#Create Menu
my_menu=Menu(root)
root.config(menu=my_menu)

#Add File Menu
file_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=lambda : open_file(False), accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=lambda : save_file(False), accelerator="Ctrl+S")
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#Add Edit Menu
edit_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="Ctrl+Y")

#Add Font Menu
font_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Font", menu=font_menu)
font_menu.add_command(label="Change Font", command=font_window)



#Add Status Bar at the bottom of the app
status_bar=Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=1)

#Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-Key-o>', open_file)
root.bind('<Control-Key-s>', save_file)



#Create Button
#Bold Button
bold_button=Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W)

#Italics Button
italic_button=Button(toolbar_frame, text="Italic", command=italic_it)
italic_button.grid(row=0, column=1, padx=10)

#Underline Button
underline_button=Button(toolbar_frame, text="Underline", command=underline_it)
underline_button.grid(row=0, column=2, padx=10)

#open pdf button
pdf_button=Button(toolbar_frame,text="Open Pdf",command=open_pdf)
pdf_button.grid(row=0,column=3)

#add find box and button
Label(toolbar_frame,text="Find:").grid(row=0,column=4,padx=10)
find_box=Entry(toolbar_frame)
find_box.grid(row=0,column=5)
# find_box.focus_set()
find_button=Button(toolbar_frame, text="Find",command=find)
find_button.grid(row=0,column=6,padx=5)

#add replace box and button
Label(toolbar_frame,text="Replace:").grid(row=0,column=7,padx=10)
replace_box=Entry(toolbar_frame)
replace_box.grid(row=0,column=8)
# find_box.focus_set()
replace_button=Button(toolbar_frame, text="Replace",command=replace)
replace_button.grid(row=0,column=9,padx=5)


mainloop()