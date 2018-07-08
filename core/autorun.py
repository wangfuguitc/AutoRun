import os
import time
import subprocess

BasePath = os.path.abspath('..')
ReportPath = os.path.join(BasePath, 'report')


def run_case(case_list, report_dir):
    for case in case_list:
        cmd = 'python ' + '"' + case + '"' + ' >> ' + '"' + \
              os.path.join(report_dir, os.path.basename(case).replace('py', 'txt')) + '"'
        sub = subprocess.Popen(cmd, shell=True)
        sub.wait()
        print(sub.returncode)


if __name__ == '__main__':
    report_dir = os.path.join(ReportPath, str(time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())))
    os.makedirs(report_dir)
    case_list = []
    dir_list = []
    for file in os.listdir(os.path.join(BasePath, 'case')):
        file_path = os.path.join(BasePath, 'case', file)
        if file.split('.')[-1] == 'py':
            case_list.append(file_path)
        elif os.path.isdir(file_path):
            dir_list.append(file_path)
    run_case(case_list, report_dir)