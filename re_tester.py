try:
    from tkinter import *
except ImportError:
    from Tkinter import *

import re

root = Tk()

info = Label(root,text = "Enter your regular expression down here:")
info.pack()

re_input = Entry(root)
re_input.pack()

info2 = Label(root,text = "Enter the text to be scanned down here:")
info2.pack()


text_input = Text(root)
text_input.pack()

def exec_re_start_only():
    pattern = re_input.get()
    text = text_input.get(1.0, END)
    
    p = re.compile(pattern)
    final = p.match(text)

    if not final:
        result_var.set("No match was found.")
    else:
        result_var.set(final.group())

def exec_re():
    pattern = re_input.get()
    text = text_input.get(1.0, END)
    
    p = re.compile(pattern)
    final = p.search(text)

    if not final:
        result_var.set("No match was found.")
    else:
        result_var.set(final.group())

def exec_re_all():
    pattern = re_input.get()
    text = text_input.get(1.0, END)
    
    p = re.compile(pattern)
    final = p.findall(text)

    if not final:
        result_var.set("No match was found.")
    else:
        result_var.set(''.join(final))

button_frame = Frame(root)
button_frame.pack()
Button(root, text="Match", command=exec_re).pack(in_=button_frame, side=LEFT)
Button(root, text="Match at start only", command=exec_re_start_only).pack(in_=button_frame, side=LEFT)
Button(root, text="Match all", command=exec_re_all).pack(in_=button_frame
                                                         , side=LEFT)

result_var = StringVar()
result = Label(root,textvariable=result_var)
result.pack()

mainloop()

