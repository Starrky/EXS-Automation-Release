# EXS-Automation Release
![alt text](https://i.imgur.com/seYqapQ.png)


# Installation

**In order to use this tool, you need to install python3 and chrome browser and keep it updated**: https://www.python.org/downloads/ and choose newest version of the installers for your OS.

Chrome download link: https://www.google.com/chrome/ :

![alt text](https://i.imgur.com/6t92U3f.png)

(select "Add to path" checkbox during installation)

## After installing Chrome and Python

**For Windows** from project directory in terminal/ powershell run:
```
pip install -r requirements.txt
```
(To do that go to the folder this project is downloaded to and **Shift + right click** then select **Open command windows here**, then just simply paste the text from above (it will install all necessarry modules for python so everything works).

### **Configs folder is sent personally, since it contains sensitive data**
**Then ask for access to configs folder, you will have to download it and put into Project root folder (config folder should be visible near APP.py)**

**For ubuntu**  you have to:

```
pip3 install -r requirements.txt
sudo apt-get install qt
```



# Usage
Main application that can run all the scripts after selection is **APP.py** in root project folder.
Just start the APP.py (double click left mouse button), then you will have 3 options:

![alt text](https://i.imgur.com/MXtotAo.png)

**Automation** - Here you can find scripts to change passwords for accounts used in automation (useful since they have to be reset every month), Payrolls export for previous month, Copy translation (copy english key translations to other languages).

**Translation** - Here you will find translation scripts (summernote add, Change translations, Add new translation). All translations are changed/ added for both Staging and Production server (Dev not included). 

**Kill driver** - Kills driver processes that might still be present in the background.
uncomment (remove '#') lines 60-65 in text editor in APP.py if you are not using Chrome browser: this is commented so it won't turn off your personal browser)


## How to use translation scripts

When you click on Translations button from main menu, new window will appear with usage and looks slightly differing between them. 

![alt text](https://i.imgur.com/ZcoYIln.png)

If you need to **Change translations** then just simply choose that tab on the top of the window, then you will need to provide: 
- App key name
- Old polish translation
- Old english translation
- New polish translation
- New english translation

Then you select which domain should be checked (messages and forms are most common) and click **Start**. -- also applies to other tabs 

Other tabs (Summernote and Add new) are more simple, since you only have to provide App key and polish+ english translations you want to add to the system.

**Summernote** is used in HTML formatted situations(programmers have to turn on summernote functionality (HTML text editor on key) to the key and it usually looks like this: ```app.access_permission_request_modal.summernote_text``` with './_summernote' at the end.

**Add new** just adds new translations to Polish, English and REF (Doesn't add to others to speed up the process, since english is default fallback language if key is not translated in other languages). That's also where **Copy translations** from **Automation** menu comes into play- if you already added all the translations you wanted, then just go back to main menu and choose Automation, then **Copy translations** and english translations will be copied over to every other language so they can easily translate those keys later.

## Side note
**(We need old polish/ english translations because most languages already have keys translated and it will confuse their local users to suddenly have something translated to english. So script goes through all languages currently in the system and checks if old translations are existent and if they are then they are changed to new ones.)**


# Folders explanation

**Translations**- scripts to speed up adding translations to the system (Summernote, changing translations for existing keys, creating new translations)

**Resources**- files needed for scripts to work (images, notification sound, icons)

**Tests**- scripts for automation testing of features in EX360 (currently not included in this branch)

**Other**- not specified scripts (e.g Get payrolls for last month)
