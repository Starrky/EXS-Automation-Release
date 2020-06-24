import inspect
import os
import sys

# All the variables that should be hidden are here
# Linux
# desktop = os.environ['HOME']
# desktop = os.path.join(os.path.join(os.environ['HOME']), 'Desktop')

user_profile = os.environ['USERPROFILE']
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
project = os.path.dirname(currentdir)
sys.path.insert(0, project)     # Directory of main project
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


'''Main folders'''
resources = f"{project}\\Resources\\"  # Resources used for project
multimedia = f"{project}\\Multimedia\\"  # Graphics and notification sound


'''Resources'''
accounts = "Accounts.cfg"
paths = "Paths.cfg"
payrolls = "Payrolls.cfg"
sites = "Sites.cfg"


'''Logs'''
log_orders = f"{project}\\Logs\\log_orders.log"
logs = f"{project}\\Logs\\"
log = f"{project}\\Logs\\log.log"
XLSX = f"{project}\\Logs\\Keys_changed.xlsx"

