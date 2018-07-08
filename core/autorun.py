import os
import subprocess


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
