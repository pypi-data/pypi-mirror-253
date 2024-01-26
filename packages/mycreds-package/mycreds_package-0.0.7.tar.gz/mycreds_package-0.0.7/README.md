# MyCreds Project
1/23/24 V1.1


## Project Description
The MyCreds project is a python program developed for WatSPEED internal use. Given a course and section number, the program scrapes the student portal (DestinyOne) for a list of students who passed and their data. The program also produces files needed to be uploaded to MyCreds: MyCredsCertificate.csv, and PDF certificates for each passing student.


## Setup
Complete the following setup in order.

### Download Python
This program is written using Python. Download the [latest version of Python](https://www.python.org/downloads/). Run the Python installer. Click repair if you've already installed Python.

### Git Setup
Download [Git](https://git-scm.com/download/win).

### Download VSCode
This MyCreds program was developed and tested in VSCode. Download [VSCode](https://code.visualstudio.com/download).

### VSCode Terminal Setup
1. Open VSCode.
2. Press `F1` or `Ctrl+Shift+P` to show all commands.
3. Enter "Terminal: Select Default Profile" and select "Git Bash".
4. Open a terminal by clicking View > Terminal. Alternatively, press `Ctrl+~`. All commands in this setup are run in the VSCode terminal.

### Cloning MyCreds Repository
1. Click File > Open Folder... and navigate to the directory in which you wish to install the MyCreds project folder.
2. Make a local clone of the repository by running the command `git clone https://github.com/wongd1532/MyCreds`.
3. Navigate to the MyCreds directory by running the command `cd MyCreds`.

### Dependencies
This program uses a couple Python libraries:
- selenium is used for webscraping
- ReportLab is used to generate PDFs

These dependencies are included in the requirements.txt file. To install these libraries, run the command `pip install -r requirements.txt`. If you have installation issues, you can troubleshoot here:
- [selenium Installation](https://pypi.org/project/selenium/)
- [ReportLab Installation](https://docs.reportlab.com/install/open_source_installation/)


## How to run the program
1. To switch the main branch, run the command `git switch main`.
2. To run the program, run the command `python MyCreds.py`. The program will prompt you for a number of inputs which are detailed in the following steps.
3. Enter a valid course and section number. Course numbers must be 4 digits, and section numbers must be 3 digits. These values are not checked until web navigation.
4. Provide your WatIAM credentials. Your password is not displayed for your security.
5. The program scrapes D1, processes the data, then generates a CSV. Find your MyCredsCertificate.csv in the MyCreds project folder. The program prompts you for a cert type. Enter 'bronze', 'silver', or 'gold' without the quotations.
6. The program generates a folder of PDF certificates called newBatch located in the MyCreds project folder. 


## Follow-up and Notes
MyCredsCertificate.csv is overwritten every time you run the program. However, the newBatch folder is not and the new PDF certificates are added to this folder. Only PDFs with the same file name are overwritten. Before running the script again, you should clean up the newBatch folder after each use by:
- Moving the contents of the newBatch folder to another folder,
- Renaming the newBatch folder,
- Deleting the newBatch folder itself, or
- Deleting the contents of the newBatch folder

It is not uncommon for the program to crash during webscraping. This is caused by the page rendering slower than the navigation occurs. In the past 50 runs, the program has crashed 6 (12%) times. This is not a concern, simply run the program again.

If the program is updated and you need to update your project code, run `git fetch origin`. On the main branch, run `git pull`.


## Next Steps
Possibly provide auto-login feature where getCredentials detects whether or not a creds.txt file exists and pulls personal creds to perform SSO login. This way, the user does not have to login every time. The .gitignore file must reflect this.


## Notes
This section is for less important notes, finer details, and strange behaviours.

### Student Full Name
If a student's name exceeds approximately 60 characters, the cert may cut off the student's name.

### Course Name
The course name is split into 2 lines IF the course name has at least 3 words and is longer than 20 characters. The upper line will always contain more characters in this case. If the course name has greater than 60 characters, the font size will be reduced. If the course name exceeds approximately 115 characters, the cert may cut off the course name.

### Why does the cert quality look different than the old ones in a bad way?
I was provided .bmp files of the template certificates, which I converted to .jpg files for usability. This conversion may have reduced quality. The certificate is just text over the .jpg file, so the certificate may look slightly different.

### Why do the bronze certs not have a watermark?
The .bmp image provided to me did not have the watermark on the bronze template. If you have a watermarked .jpg of a blank bronze certificate template, feel free to replace the bronzeCertTemp.jpg file in the templates folder. Make sure to give it the same name.

### Contact
If you have additional questions, feel free to contact the developer at d78wong@uwaterloo.ca. This is my first released project and I hope it'll be useful for a long time to come! :D