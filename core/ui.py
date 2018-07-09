import tkinter
from conf import setting
from core import autorun

root = tkinter.Tk()
root.title('AutoRun')
root.geometry(setting.Size)

search = tkinter.Entry(root, width=200, font=('', '16', ''), borderwidth=2)
search.place(relx=0.01, rely=0.01, relwidth=0.6)

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