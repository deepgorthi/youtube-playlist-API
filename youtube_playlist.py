#!/usr/bin/env python3

from youtube_connect import YoutubeConnect
from channel_info import ChannelInfo

class YoutubePlaylist:
    
    youtube = YoutubeConnect()
    youtube_connection = youtube.getConnection()

    def __init__(self, username):
        self.username = username


    def sendPlaylistRequest(self, nextPageToken):

        channel = ChannelInfo(self.username)
        channel_id = channel.getChannelId()

        playlist_request = self.youtube_connection.playlists().list(
            part='contentDetails, snippet',
            channelId = channel_id,
            maxResults=50,
            pageToken=nextPageToken
        )

        return playlist_request
    

    def getPlaylistResponse(self):
        
        playlist_request = self.sendPlaylistRequest(None)
        playlist_response = playlist_request.execute()

        return playlist_response


    def getPlaylistIdTitle(self):

        playlist_response = self.getPlaylistResponse()
        playlist_id = [item['id'] for item in playlist_response['items']]
        playlist_name = [item['snippet']['title'] for item in playlist_response['items']]

        return playlist_id, playlist_name
    
    def getPlaylistName(self):

        playlist_response = self.getPlaylistResponse()
        playlist_name = [item['snippet']['title'] for item in playlist_response['items']]

        return playlist_name