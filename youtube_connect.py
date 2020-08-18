#!/usr/bin/env python3

import os
from googleapiclient.discovery import build


class YoutubeConnect:
    
    api_key = os.environ.get('GOOGLE_API_KEY')

    def __init__(self):
        pass


    def getConnection(self):
        
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        
        return youtube