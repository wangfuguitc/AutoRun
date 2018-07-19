import os
import subprocess


def run_case(case_list, report_dir):
    success = 0
    fail = 0
    for case in case_list:
        cmd = 'python ' + '"' + case + '"' + ' >> ' + '"' + \
              os.path.join(report_dir, os.path.basename(case).replace('py', 'txt')) + '"'
        sub = subprocess.Popen(cmd, shell=True)
        sub.wait()
        if sub.returncode:
            fail += 1
            html_report(case, success, fail, 'success')
        else:
            success += 1
            html_report(case, success, fail, 'fail')


def html_report(case, success, fail, state):
    pass
