import tkinter as tk
from tkinter import ttk
# window
window= tk.Tk()
window.title('open the window')
window.geometry("400x400")
# menu
menu = tk.Menu(window)
menu.add_cascade(label='homework one')
window.configure(menu=menu)
# sub menu
file_menu = tk.Menu(menu , tearoff = False)
file_menu.add_command(label='New', command=lambda :print('New_file'))
file_menu.add_command(label='open', command=lambda :print('open_file'))
file_menu.add_separator()
menu.add_cascade(label='file', menu=file_menu)
#next menu
file_menu = tk.Menu(menu , tearoff = False)
file_menu.add_command(label='home work', command=lambda :print('New_file make a table'))
file_menu.add_command(label='excercise', command=lambda :print('open_file work computer and function'))
file_menu.add_separator()
menu.add_cascade(label='time table', menu=file_menu)
#next menu
# another submenu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label='check', command=lambda :print('open_file work computer and function') )
help_menu.add_command(label='check1', command=lambda :print('open_file work computer and function1') )
help_menu.add_command(label='check2', command=lambda :print('open_file work computer and function2') )
help_menu.add_command(label='check3', command=lambda :print('open_file work computer and function3') )
menu.add_cascade(label='help', menu=help_menu)
window.configure(menu = menu)
# other sub menu
excercise_menu = tk.Menu(menu, tearoff=False)
excercise_menu.add_command(label='excercise test 1', command=lambda :print('excercise make me power '
                                                                           'ful in the computer working') )
menu.add_cascade(label='excercise', menu=excercise_menu)
# run
window.mainloop()