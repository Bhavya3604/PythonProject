from tkinter import *
from tkinter import filedialog
from tkinter import font

root=Tk()
root.title('Word Clone')
root.iconbitmap('c:/Users/DEVANSH/Downloads/smiley.ico')

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
    text_file=filedialog.askopenfilename(initialdir="C:/Users/DEVANSH/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Word File", "*.docx"), ("All Files", "*.*")))
    
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
    my_text.insert(END,content)
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
    #Configure a tag
    my_text.tag_configure("bold", font=bold_font)
    #Define Current tags
    current_tags=my_text.tag_names("sel.first")

    #If statement to see if tag has been set 
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")

    


#Italic Text
def italic_it():
    #Create our font
    italic_font=font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant="italic")
    #Configure a tag
    my_text.tag_configure("italic", font=italic_font)
    #Define Current tags
    current_tags=my_text.tag_names("sel.first")

    #If statement to see if tag has been set 
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")
    
#Underline text
def underline_it():
    #Create Our Font
    underline_font=font.Font(my_text, my_text.cget("font"))
    underline_font.configure(underline=True)
    #Configure a tag
    my_text.tag_configure("underline", font=underline_font)
    #Define Current Tags
    current_tags=my_text.tag_names("sel.first")

    #If statement to see if tag has been set 
    if "underline" in current_tags:
        my_text.tag_remove("underline", "sel.first", "sel.last")
    else:
        my_text.tag_add("underline", "sel.first", "sel.last")


#Create toolbar frame
toolbar_frame=Frame(root)
toolbar_frame.pack(fill=X)


#Create Main Frame
my_frame=Frame(root)
my_frame.pack(pady=5)

#Create Scroll bar
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Create Text Box
my_text=Text(my_frame, selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

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
italic_button=Button(toolbar_frame, text="Underline", command=underline_it)
italic_button.grid(row=0, column=2, padx=10)


mainloop()