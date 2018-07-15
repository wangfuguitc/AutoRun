import tkinter
import os
from conf import setting
from core import autorun

Checkbutton_Y = 0
Var_list = []
Cb_dict = {}
File_list = []

root = tkinter.Tk()
root.title('AutoRun')
root.geometry('1200x700')

search = tkinter.Entry(root, width=250, font=('', '16', ''), borderwidth=2)
search.place(relx=0.01, rely=0.015, relwidth=0.6)


def chb_action(button_list, chb_state):
    if chb_state.get():
        for botton in button_list:
            botton.deselect()
            botton.invoke()
    else:
        for botton in button_list:
            botton.select()
            botton.invoke()


def make_button(dir_list, main_dir, main_list, checkbutton_x, *args):
    global Checkbutton_Y
    global Var_list
    global Cb_dict
    Checkbutton_Y += 1
    chb_state = tkinter.IntVar()
    Cb_dict[main_dir] = []
    cb = tkinter.Checkbutton(canvas_left, text=main_dir, anchor='w', width=120, variable=chb_state, onvalue=1, offvalue=0, command=lambda: chb_action(Cb_dict[main_dir], chb_state))
    if args:
        Cb_dict[args[0]].append(cb)
    canvas_left.create_window(450+20*checkbutton_x, 21*Checkbutton_Y, window=cb)
    checkbutton_x += 1
    for file in dir_list[0]:
        Checkbutton_Y += 1
        var = tkinter.StringVar()
        Var_list.append(var)
        cb = tkinter.Checkbutton(canvas_left, text=file, anchor='w', width=120, variable=var, onvalue=os.path.join(main_dir, file), offvalue='')
        Cb_dict[main_dir].append(cb)
        canvas_left.create_window(450+20*checkbutton_x, 21*Checkbutton_Y, window=cb)
    for re_dir in dir_list[1]:
        ab_dir = os.path.join(main_dir, re_dir)
        make_button(main_list[ab_dir], ab_dir, main_list, checkbutton_x, main_dir)


def search_dir(dir):
    global Checkbutton_Y
    global Var_list
    global Cb_dict
    Checkbutton_Y = 0
    Var_list = []
    Cb_dict = {}
    dir_list = {}
    canvas_left.delete('all')
    for maindir, subdir, file_name_list in os.walk(dir):
        file_name_list = [file for file in file_name_list if file.endswith('.py')]
        dir_list[maindir] = [file_name_list, subdir]
    return dir_list


def search_action():
    main_dir = search.get()
    if os.path.isdir(main_dir):
        label_var.set('')
        dir_list = search_dir(main_dir)
        make_button(dir_list[main_dir], main_dir, dir_list, 0)
    else:
        label_var.set('directory does not exist')


def add_action():
    global File_list
    global Var_list
    File_list = [var.get() for var in Var_list if var.get()]


frame_left = tkinter.Frame(root, width=450, height=550, bd=3, bg='white', relief=tkinter.GROOVE)
frame_left.place(relx=0.01, rely=0.08)

canvas_left = tkinter.Canvas(frame_left, bg='white', width=450, height=550, scrollregion=(0, 0, 2000, 2000))

hbar_left = tkinter.Scrollbar(frame_left, orient=tkinter.HORIZONTAL)
hbar_left.pack(side=tkinter.BOTTOM, fill=tkinter.X)
hbar_left.set(0, 0.5)
hbar_left.config(command=canvas_left.xview)

vbar_left = tkinter.Scrollbar(frame_left, orient=tkinter.VERTICAL)
vbar_left.pack(side=tkinter.RIGHT, fill=tkinter.Y)
vbar_left.set(0, 0.5)
vbar_left.config(command=canvas_left.yview)

canvas_left.config(xscrollcommand=hbar_left.set, yscrollcommand=vbar_left.set)
canvas_left.pack()

label_var = tkinter.StringVar()
label = tkinter.Label(root, textvariable=label_var, width=25, font=('', 14, ''), fg='red')
label.place(relx=0.75, rely=0.015)

search_button = tkinter.Button(root, text='search', borderwidth=3, width=10, command=search_action)
search_button.place(relx=0.65, rely=0.01)

add_button = tkinter.Button(root, text='add', borderwidth=3, width=10, command=add_action)
add_button.place(relx=0.43, rely=0.4)

root.mainloop()



# if __name__ == '__main__':
#     BasePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     ReportPath = os.path.join(BasePath, 'report')
#     report_dir = os.path.join(ReportPath, str(time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())))
#     os.makedirs(report_dir)
#     case_list = []
#     dir_list = []
#     for file in os.listdir(os.path.join(BasePath, 'case')):
#         file_path = os.path.join(BasePath, 'case', file)
#         if file.split('.')[-1] == 'py':
#             case_list.append(file_path)
#         elif os.path.isdir(file_path):
#             dir_list.append(file_path)
#     result_list = run_case(case_list, report_dir)
#     html_report(case_list, result_list, report_dir)