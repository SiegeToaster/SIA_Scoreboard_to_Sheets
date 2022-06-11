from __future__ import print_function
import ast

import os.path

import discord

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1nzlE0FmtF6EY8WbHU5wwC4sLaDbEYtnzGRy893yEhv4'
SHEET_ID = 1083149368
FILE_PATH = os.getcwd()
TOKEN_PATH = FILE_PATH + "/token.json"

DISCORD_TOKEN = ''
DISCORD_CHANNEL_ID = 874088908210700300 # events channel for example

def main():
	try:
		service = build('sheets', 'v4', credentials=auth())
		sheets = service.spreadsheets()
	except HttpError as err:
		print(err)
		return

	scores = get_scores()
	send_to_sheets(sheets, scores)

def auth():
	creds = None
	# The file token.json stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists(TOKEN_PATH):
		creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				FILE_PATH + '/credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open(TOKEN_PATH, 'w') as token:
			token.write(creds.to_json())

	return creds

def get_scores():
	file = open("input.txt", "r")
	txt = file.read()
	return txt

def send_to_sheets(sheets, value):
	rows = [{"values": [
		{
			"userEnteredValue": {
				"stringValue": value
			}
		}
	]}]
		
	requests = [{
		"updateCells": {
			"fields": "userEnteredValue",
			"rows": rows,
			"start": {
				"columnIndex": 0,
				"rowIndex": 0,
				"sheetId": SHEET_ID
			}
		},
	}]

	result = sheets.batchUpdate(
		spreadsheetId=SPREADSHEET_ID, body={ "requests": requests }
	).execute()

	# print(result) # DEBUG
	print("spreadsheet updated")

if __name__ == '__main__':
	main()