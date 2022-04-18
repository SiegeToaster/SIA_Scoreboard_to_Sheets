# SIA Scoreboard to Sheets

## Installation
1. Download files
2. Install [Python](https://www.python.org/downloads) version 2.6 or greater
3. Install [pip package manager](https://pypi.org/project/pip/) (pip should install automatically with Python)
4. Run the following command: ```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```
5. Create a Google Cloud Platform project with the Google Sheets API enabled.  Then, create a OAuth client ID authorization credentials for a desktop application.  For instructions on how to do this, see the [Google Sheets Python Quickstart](https://developers.google.com/sheets/api/quickstart/python).

## Instructions for usage
1. Change the SPREADSHEET_ID constant to the current spreadsheet ID (currently, it is ``1jz9qTfvp5hRZGuyN7HidmstlfEkVtcUe7kynWi0bUlY``)
2. Change the SHEET_ID constant to the current Medal Hall sheet ID (currently, it is ``1532993005``)
3. Use the [Export Scoreboard](https://github.com/Soliders-in-Arms-Arma-3-Group/SIA-Mission-Framework.VR/commit/1edf5a3896aa41a4accf06376eb18d42fd8be9a3) script to copy the scoreboard data to clipboard (you must be logged in as admin for this to work)
4. Paste the data into ``input.txt``.  Make sure that the file is empty before pasting.
5. Run the python script by double clicking the ``scoreboardToSheets.py`` file.  If this doesn't work, run the script through a terminal and debug whatever error it gives.