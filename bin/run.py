import inspect
import json

import pytest
import os.path
import argparse
import sys
import time
import requests

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
project_dir = os.path.dirname(current_dir)
reports_dir = project_dir + "/reports/"
tests_dir = project_dir + "/tests/"
report_file_name = "UI_Report.html"
log_file_name = "UI_Log.log"
sys.path.insert(0, project_dir)
from lib.utils.ConfigParser import ConfigParser
# from src.lib.SendEmail import SendReportEmail

# Parsing Commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument('-config', action='store', dest='file_name', help='Provide Config File Name', required=True)
parser.add_argument('-modules', action='store', dest='modules', help='Provide Config File Name', required=False)
parsed = parser.parse_args()
file_path = project_dir + "/config/" + parsed.file_name

# Checking config file exists or not
print(file_path)
if not os.path.isfile(file_path):
    print("Config file does not exists...")
    exit(1)
else:
    print("Config file found: " + file_path)

cfg = ConfigParser(file_path)
host = cfg.safe_get('DEFAULT', 'url').split(".", 1)[1]
report_dir_name = reports_dir + "" + host + "_" + str(time.time())
# is_agms = "AGMS-ENABLED" if cfg.safe_get('AUTOMATION.RUN', 'IS_AGMS_ENABLED') == "True" else "AGMS-DISABLED"

try:
    os.mkdir(report_dir_name)
    print("Report Directory ", report_dir_name, " Created ")
except FileExistsError:
    print("Report Directory ", report_dir_name, " already exists")
html_report_file = report_dir_name + "/" + report_file_name
log_file = report_dir_name + "/log_file_" + str(time.time()) + ".log"


def run_test():
    test_args = []
    arglist = list(test_args)
    arglist.append(tests_dir)
    arglist.append("-rapsx")
    if parsed.modules is not None:
        module = " or ".join(parsed.modules.split(","))
        print("executing tests cases from module: " + module)
        arglist.append("-m " + module)
    else:
        parsed.modules = "All"
        print("executing all tests cases...")
    print(html_report_file)
    arglist.append("--html=" + html_report_file)
    arglist.append("--self-contained-html")
    arglist.append("--conf_file=" + file_path)
    arglist.append("--op_path=" + report_dir_name)
    print(arglist)
    pytest.main(arglist)


# def send_report():
#     r = requests.get('http://qbep01.' + host + ':50259/info')
#     data = json.loads(r.text)
#     qbep_version = data["build"]["version"]
#     print(qbep_version)
#     to = cfg.safe_get('AUTOMATION.RUN', 'mail_to')
#     if to is not None:
#         subject = host + " - " + is_agms + " - QBEP-" + qbep_version + " (" + parsed.modules + ")"
#         SendReportEmail(subject, to, html_report_file, report_file_name, log_file).send_mail()


sys.stdout = open(log_file, 'w')
run_test()
# send_report()

# std, err = capture.reset()
# print(std)
