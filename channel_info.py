#!/usr/bin/env python3

from youtube_connect import YoutubeConnect

class ChannelInfo:

    def __init__(self, username):
        self.username = username


    def sendChannelRequest(self):
        
        youtube = YoutubeConnect()
        youtube_connection = youtube.getConnection()
        
        channel_request = youtube_connection.channels().list(
            part='contentDetails, statistics',
            forUsername=self.username
        )
        
        return channel_request


    def getChannelInfo(self):
        
        channel_request = self.sendChannelRequest()
        channel_response = channel_request.execute()
        
        return channel_response


    def getChannelId(self):

        channel_response = self.getChannelInfo()
        # print(channel_response)
        channel_id = channel_response['items'][0]['id']
        
        return channel_id

    def getVideoCount(self):
        
        channel_response = self.getChannelInfo()
        videoCount = channel_response['items'][0]['statistics']['videoCount']
        
        return videoCount