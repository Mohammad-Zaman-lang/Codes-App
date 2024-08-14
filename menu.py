import tkinter as tk
from tkinter import ttk
# window
window= tk.Tk()
window.title('open the window')
window.geometry("600x400")
# menu
menu = tk.Menu(window)
menu.add_cascade(label='homework one')
window.configure(menu=menu)
# sub menu
file_menu = tk.Menu(menu , tearoff = False)
file_menu.add_command(label='New', command=lambda :print('New_file'))
file_menu.add_command(label='open', command=lambda :print('open_file'))
file_menu.add_command(label='excercise', command=lambda :print('open the built_in'))

file_menu.add_separator()
menu.add_cascade(label='homework one', menu=file_menu)
#next menu
file_menu = tk.Menu(menu , tearoff = False)
file_menu.add_command(label='home work', command=lambda :print('New_file make a table'))
file_menu.add_command(label='excercise', command=lambda :print('open_file work computer and function'))
file_menu.add_separator()
menu.add_cascade(label='homework two', menu=file_menu, command=lambda :print("homework two"))
#next menu
# another submenu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label='check', command=lambda :print('open_file work computer and function') )
help_menu.add_command(label='check1', command=lambda :print('open_file work computer and function1') )
help_menu.add_command(label='check2', command=lambda :print('open_file work computer and function2') )
help_menu.add_command(label='check3', command=lambda :print('open_file work computer and function3') )
menu.add_cascade(label='homework tree', menu=help_menu, command=lambda :print("put in inhere homework tree"))
window.configure(menu = menu)
# other sub menu
excercise_menu = tk.Menu(menu, tearoff=False)
excercise_menu.add_command(label='excercise test 1', command=lambda :print('excercise make me power '
                                                                           'ful in the computer working') )
menu.add_cascade(label='about this code', menu=excercise_menu)

label=ttk.Label(window,text='in the name of allah', background='red' )
label.grid(row=1,column=0, )

# run
window.mainloop()