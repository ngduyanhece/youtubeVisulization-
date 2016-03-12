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
  res = youtube.search().list(
    q="javascript",
    part="id,snippet",
    maxResults=50
  ).execute()
  nextPageToken = res.get('nextPageToken')
  while ('nextPageToken' in res):
      nextPage = youtube.search().list(
      part="id,snippet",
      q="javascript",
      maxResults="50",
      pageToken=nextPageToken
      ).execute()
      res['items'] = res['items'] + nextPage['items']

      if 'nextPageToken' not in nextPage:
          res.pop('nextPageToken', None)
      else:
          nextPageToken = nextPage['nextPageToken']
 #search_videos = []

 # Merge video ids
 #for search_result in search_response.get("items", []):
 #  search_videos.append(search_result["id"]["videoId"])
 #video_ids = ",".join(search_videos)

 # Call the videos.list method to retrieve location details for each video.
  #video_response = youtube.videos().list(
   #id=video_ids,
   #part='statistics'
  #).execute()

  #write res to a json file
  with open("data.json", "w") as outfile:
    json.dump(res, outfile)
youtube_search()
