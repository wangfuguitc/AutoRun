import os
import subprocess
import time


def run_case(case_list, report_dir):
    report_html = os.path.join(report_dir, 'report.html')
    with open(report_html, 'a') as handle:
        handle.write('''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>report</title></head><body><table style="width: 100%;border-collapse: collapse;" cellpadding="5">''')
    for case in case_list:
        cmd = 'python ' + '"' + case + '"' + ' >> ' + '"' + \
              os.path.join(report_dir, os.path.basename(case).replace('py', 'txt')) + '"'
        sub = subprocess.Popen(cmd, shell=True)
        sub.wait()
        with open(report_html, 'a') as handle:
            if sub.returncode:
                html_report(case, 'success', handle)
            else:
                html_report(case, 'fail', handle)
    with open(report_html, 'a') as handle:
        handle.write('''</table></body></html>''')


def html_report(case, state, handle):
    log = os.path.basename(case).replace('py', 'txt')
    content = '''<tr style="border-bottom: 2px solid #ddd;"><th><a href="file_path">file_path</a></th><th><a href="log_path">log</a></th><th><b style="color: red">state</b></th><th><b >time</b></th></tr>'''
    content = content.replace('file_path', case).replace('log_path', log).replace('state', state).replace('time', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    handle.write(content)
