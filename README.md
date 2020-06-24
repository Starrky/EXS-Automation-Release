# EXS-Automation Release
![alt text](https://i.imgur.com/seYqapQ.png)

In order to use this tool, you need to install python3: https://www.python.org/downloads/ and choose newest version of the installers for your OS:

![alt text](https://i.imgur.com/6t92U3f.png)


For Windows: from project directory in terminal/ powershell run:

```
pip3 install -r requirements.txt
```

For ubuntu additionally you have to:
```
sudo apt-get install qt
```

Main application that can run all the scripts after selection is APP.py in root project folder.

Folders explanation:
Translations- scripts to speed up adding translations to the system( Summernote, changing translations for existing keys, creating new translations)

Resources- files needed for scripts to work

Tests- scripts for automation testing of features in EX360

Other- not specified scripts( e.g Get payrolls for last month)
