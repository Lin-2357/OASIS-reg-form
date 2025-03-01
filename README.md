# OASIS-reg-form
Check if an RSO constitution file contains the required clauses, follow the steps if you are using it for the first time, otherwise you skip step 3.

## Step 1
Download the constitution file into the same folder as this readme file. (Recommend for mac users to download it into desktop)
## Step 2
Convert the file to pdf format (using save as) if it is word or other format, and copy the file name on the clipboard (with or without the .pdf extension are both fine).
## For MacOS Users
If using it for the first time, right Click on this folder (contains this README), select "open in terminal", copy the below command and paste in the terminal window, press enter.
```
chmod +x start.command
chmod +x build.command
```
## Step 3
Make sure you have python installed on your device (use https://www.python.org/downloads/ if not). If you are using it for the first time, click and run build.bat for windows, or run build.command for mac.
## Step 4
Click and run start.bat for windows, run start.command for mac.
## Step 5
There will be a terminal window popping up showing you the clause checking result. Double check manually for the missing clauses (there may actually be a clause with different wording or font or other reasons that the script failed to recognize).
## Step 6
If the constitution has missing clauses, the deny message will be copied onto you clipboard, paste it in Callink and hit deny. Otherwise hit approve.