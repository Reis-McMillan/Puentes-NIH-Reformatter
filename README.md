# Puentes-NIH-Reformatter
This is a simple, user-friendly program which allows RAs with the Purdue Puentes Project to quickly reformat NIH health data on a Windows computer.

## Requirements
- Python 3.10 installed
- Pandas library installed
- Tkinter library installed
- Windows OS

## Installation
Click [here](https://github.com/Reis-McMillan/Puentes-NIH-Reformatter/archive/refs/heads/master.zip) to ZIP file for the program. The ZIP file can be extracted to any directory and the program should be able to run from there. Note that it is important none of the files in the extracted folder are moved or deleted. The file called "Purdue Puentes NIH Data Reformatter" is the appropriate file to run, just click to open the file and the program should launch. If the user wishes, they can choose to create a Desktop shortcut or simply keep the script in the Desktop directory.

## Running the Program
Upon launching the program it is important that the RA selects the wave and participant type of the file they intend to be working with. These options can be selected in the two listboxes in the top-left of the program.

![](https://github.com/Reis-McMillan/Puentes-NIH-Reformatter/blob/4153215d722a7fcc2e059fd16de750fc0d391eee/README%20photos/wave_and_participant.png)

### Checking the Data before Reformatting
Before the data can be reformatted by the program it is important that the RA check and correct any abnormalities in the data. To assist the RA with this, the program has a feature called "Preliminary Check" which checks the file to be reformatted for any entries in the data which seem to be abnormal. The RA must simple click the button labeled "Preliminary Check" and select the file they intend to reformat, and the program will output the PINs of participant whose data it found to be abnormal.

![](https://github.com/Reis-McMillan/Puentes-NIH-Reformatter/blob/4153215d722a7fcc2e059fd16de750fc0d391eee/README%20photos/prelim_check.png)

### Reformatting the Data
Once the RA has checked the abnormalities the program identified in the data and feel that the file is ready to be reformatted, they need only select the button labeled "Reformat NIH Data" and a file explorer will open where the RA can select the file to be reformatted. Once the file has been reformatted, the program will prompt the RA to name and save a new file (the old file will remain as is). Note that it is very important that the RA end the file name with ".csv"; the program will not do this for the RA. 

![](https://github.com/Reis-McMillan/Puentes-NIH-Reformatter/blob/cb5809d4749a80e77adae35f79c20c9a4bed2764/README%20photos/reformat.png)

Once the file has been saved, the program will output the PINs of participants where it is unsure that the data has been reformatted correctly. The RA should check these PINs and verify that the data is correct, or make the necessary modifications to ensure that the data is correct.
