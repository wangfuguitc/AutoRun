import tkinter
import os
from conf import setting
from core import autorun

root = tkinter.Tk()
root.title('AutoRun')
root.geometry('1200x700')

search = tkinter.Entry(root, width=200, font=('', '16', ''), borderwidth=2)
search.place(relx=0.01, rely=0.015, relwidth=0.6)


def list_dir(dir):
    pass


def search_action():
    dir = search.get()
    if os.path.isdir(dir):
        label_var.set('')
        list_dir(dir)
    else:
        label_var.set('directory does not exist')


frame_left = tkinter.Frame(root, width=450, height=550, bd=3, bg='white', relief=tkinter.GROOVE)
frame_left.place(relx=0.01, rely=0.08)

scale_left = tkinter.Scrollbar(frame_left, orient=tkinter.HORIZONTAL)
scale_left.place(relwidth=1, rely=0.97)
scale_left.set(0, 0.5)

label_var = tkinter.StringVar()
label = tkinter.Label(root, textvariable=label_var, width=25, font=('', 14, ''), fg='red')
label.place(relx=0.75, rely=0.015)

search_button = tkinter.Button(root, text='search', borderwidth=3, width=10, command=search_action)
search_button.place(relx=0.65, rely=0.01)

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