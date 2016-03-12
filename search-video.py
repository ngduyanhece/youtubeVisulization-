#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import json

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyB3BCCgsRq67cZEtIwWqYu6IPPsZx5mqTU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search():
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
									developerKey=DEVELOPER_KEY)

	# Call the search.list method to retrieve results matching the specified
	# query term.
	search_response = youtube.search().list(
		q="css",
		type="video",
		part="id,snippet",
	).execute()
	nextPageToken = search_response.get('nextPageToken')
	while('nextPageToken' in search_response):
		nextPage = youtube.search().list(
			q="css",
			type="video",
			part="id,snippet",
			pageToken=nextPageToken
		).execute()
		search_response['items'] = search_response['items'] + nextPage['items']

		if 'nextPageToken' not in nextPage:
			search_response.pop('nextPageToken', None)	
		else:
			nextPageToken = nextPage['nextPageToken']

	#search_videos = []

	# Merge video ids
	#for search_result in search_response.get("items", []):
		#search_videos.append(search_result["id"]["videoId"])
		#search_videos.append(search_result["id"]["videoId"])
		#video_ids = ",".join(search_videos)

		# Call the videos.list method to retrieve location details for each video.
		#video_response = youtube.videos().list(
		#	id=video_ids,
		#	part='statistics'
		#).execute()
	with open("video-details.json", "w") as outfile:
		json.dump(search_response, outfile)

youtube_search()
