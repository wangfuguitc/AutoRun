import os
import time
import subprocess

BasePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ReportPath = os.path.join(BasePath, 'report')


def run_case(case_list, report_dir):
    result_list = []
    for case in case_list:
        cmd = 'python ' + '"' + case + '"' + ' >> ' + '"' + \
              os.path.join(report_dir, os.path.basename(case).replace('py', 'txt')) + '"'
        sub = subprocess.Popen(cmd, shell=True)
        sub.wait()
        result_list.append(sub.returncode)
    return result_list


def html_report(case_list, result_list, report_dir):
    pass


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
    result_list = run_case(case_list, report_dir)
    html_report(case_list, result_list, report_dir)