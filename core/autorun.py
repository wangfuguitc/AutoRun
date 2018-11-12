import os
import subprocess
import time


def run_case(case_list, report_dir):
    report_html = os.path.join(report_dir, 'report.html')
    print(report_html)
    with open(report_html, 'a') as handle:
        handle.write('''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>report</title></head><body><script>window.onload=function (){var success;var fail;var total;var rate;success = document.getElementsByClassName('success').length;fail = document.getElementsByClassName('fail').length;total = success+fail;rate = ((success/total)*100).toFixed(2);document.getElementById('success').innerHTML="success: "+success;document.getElementById('fail').innerHTML="fail: "+fail;document.getElementById('total').innerHTML="total: "+total;document.getElementById('rate').innerHTML="rate: "+rate+"%";}</script><table style="width: 100%;font-size:22px"><tr><th id="success"></th><th id="fail"></th><th id="total"></th><th id="rate"></th><th ><input type="radio" name="filter" checked value="'all" onclick="filter('all')">all</th><th ><input type="radio" name="filter"  value="'success" onclick="filter('fail')">success</th><th ><input type="radio" name="filter"  value="'fail" onclick="filter('success')">fail</th><script>function filter(name) {var tr_list=document.getElementsByTagName('tr');for (var i=0;i<tr_list.length;i++){tr_list[i].style.display='';}var tag_list=document.getElementsByClassName(name);for (var i=0;i<tag_list.length;i++){tag_list[i].style.display='none';}}</script></tr></table><table style="width: 100%;border-collapse: collapse;" cellpadding="5">''')
    for case in case_list:
        cmd = 'python ' + '"' + case + '"' + ' >> ' + '"' + \
              os.path.join(report_dir, os.path.basename(case).replace('py', 'txt')) + '"'
        sub = subprocess.Popen(cmd, shell=True)
        sub.wait()
        with open(report_html, 'a') as handle:
            if sub.returncode:
                html_report(case, 'fail', handle)
            else:
                html_report(case, 'success', handle)
    with open(report_html, 'a') as handle:
        handle.write('''</table></body></html>''')


def html_report(case, state, handle):
    log = os.path.basename(case).replace('py', 'txt')
    content = '''<tr style="border-bottom: 2px solid #ddd;" class="state"><th align="left" style="width: 50%"><a href="file_path">file_path</a></th><th><a href="log_path">log</a></th><th><b style="color: red">state</b></th><th><b >time</b></th></tr>'''
    content = content.replace('file_path', case).replace('log_path', log).replace('state', state).replace('time', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    handle.write(content)
