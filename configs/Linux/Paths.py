import inspect
import os
import sys
from sys import platform
# All the variables that should be hidden are here

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
higher_dir = os.path.dirname(currentdir)
parentdir = os.path.dirname(higher_dir)

sys.path.insert(0, parentdir)  # Directory of main project
# Linux
desktop = os.path.join(os.path.join(os.environ['HOME']), 'Desktop')
driver = f"{parentdir}/Resources/Driver/"
downloads = os.path.join(os.path.join(os.environ['HOME']), 'Downloads')

'''TK inter'''
title = "Extranet Automation"
graphics = f"{parentdir}/Resources/Multimedia/logo_extranet_small2.gif"
sound = f"{parentdir}/Resources/Multimedia/notification.mp3"
po_graphics = f"{parentdir}/Resources/Multimedia/"
favicon = f"{parentdir}/Resources/Multimedia/favicon.png"

'''Logs'''
log_orders = f"{parentdir}/Logs/log_orders.txt"
logs = f"{parentdir}/Logs/"
KO_changer_log_txt = f"{parentdir}/Logs/KO_changes.txt"
KO_changer_log_xlsx = f"{parentdir}/Logs/KO_changes.xlsx"
log = f"{parentdir}/Logs/log.log"
XLSX = f"{parentdir}/Logs/Keys_changed.xlsx"
XLSX_t = f"{parentdir}/Logs/Keys_changed_t.xlsx"
log_script = f"{parentdir}/Logs/log_script.log"

'''Scripts'''
Payrolls = f"{parentdir}/Other/Payrolls.py"
Translations_change_keys = f"{parentdir}/Translations/change_translations.py"
Translations_summernote = f"{parentdir}/Translations/New_keys_summernote.py"
Translations_new_keys = f"{parentdir}/Translations/New_keys.py"
Copy_translations = f"{parentdir}/Translations/Copy_translations.py"