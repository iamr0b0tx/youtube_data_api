# -*- coding: utf-8 -*-

# import the std lib modules
import os
from json import dump
from time import strftime, ctime
from csv import writer

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v2'
CLIENT_SECRETS_FILE = 'client_secret.json'

def read_input(filepath):
	# read params
	try:
		with open(filepath) as file_object:
			return file_object.read().replace('\n', ',').replace('\r', ',').replace(' ', '').strip()
	except Exception as e:
		print(e)

def get_service():
	flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
	credentials = flow.run_console()
	return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def execute_api_request(client_library_function, **kwargs):
	response = client_library_function(
		**kwargs
	).execute()

	return response

if __name__ == '__main__':
	# Disable OAuthlib's HTTPs verification when running locally.
	# *DO NOT* leave this option enabled when running in production.
	os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
	
	# initialize
	youtubeAnalytics = get_service()

	# initilize
	try_again = None

	while try_again  != 'q':
		print("\nEdit the [dimensions.txt] and [metrics.txt] to specify the parameters you wish to obtain")
		print("NOTE: Make sure you have your [client_secret.json] in this folder")
		print("NOTE: You can press [enter] without the dates to use a default day")

		print("\nResult Time range\n===============")
		start_date = input("Type the day you want result to start (YYYY-MM-DD) and press enter: ")
		end_date = input("Type the day you want result to end (YYYY-MM-DD) and press enter: ")
		
		if not start_date.strip():
			start_date = strftime('%Y-01-01')

		if not end_date.strip():
			end_date = strftime("%Y-%m-%d")

		data_object = execute_api_request(
				youtubeAnalytics.reports().query,
				ids='channel==MINE',
				startDate=start_date,
				endDate=end_date,
				metrics=read_input('metrics.txt'),
				dimensions=read_input('dimensions.txt'),
				sort='day'
		)

		# the output recieved
		output_filepath = f'results/{ctime().replace(":", "_")}'

		# save as json
		with open(f'{output_filepath}.json', 'w') as output_file_object:
			dump(data_object, output_file_object)

		# save as csv
		with open(f'{output_filepath}.csv', 'w', newline='') as output_file_object:
			wr = writer(output_file_object)

			# get the headers
			wr.writerow([head["name"] for head in data_object["columnHeaders"]])

			# get the rows of data
			wr.writerows(data_object["rows"])

		# if you wish to try again
		try_again = input("Type ['q' and enter] to quit or just [enter] to continue: ").strip()