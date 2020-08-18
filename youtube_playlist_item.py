#!/usr/bin/env python3

from youtube_connect import YoutubeConnect
# from youtube_playlist import YoutubePlaylist
from time_pattern import TimePattern
from youtube_playlist_duration import YoutubePlaylistDuration

class YoutubePlaylistItem:
    
    youtube = YoutubeConnect()
    youtube_connection = youtube.getConnection()

    # playlist = YoutubePlaylist()
    # playlist_id = playlist.getPlaylistId()

    def __init__(self, nextPageToken, playlist_id):
        self.nextPageToken = nextPageToken
        self.playlist_id = playlist_id


    def getPlaylistItem(self):

        playlist_item_request = self.youtube_connection.playlistItems().list(
                part='contentDetails',
                playlistId=self.playlist_id,
                maxResults=50,
                pageToken=self.nextPageToken
            )
        
        playlist_item_response = playlist_item_request.execute()
        
        return playlist_item_response


    def getVideoId(self):

        playlist_item_response = self.getPlaylistItem()

        video_id = []
        for item in playlist_item_response['items']:
            video_id.append(item['contentDetails']['videoId'])
        # print(video_id)
        return video_id
    

    def getAllVideoIds(self):

        all_video_ids = ','.join(self.getVideoId())

        return all_video_ids

    
    def getVideoResponse(self):

        video_request = self.youtube_connection.videos().list(
            part='contentDetails',
            id=self.getAllVideoIds()
        )   
        video_response = video_request.execute()

        return video_response
    

    def getVideoDuration(self):
        
        video_duration = []
        total_seconds = 0

        video_response = self.getVideoResponse()

        for item in video_response['items']:
            duration = item['contentDetails']['duration']

            time_pattern = TimePattern()
            
            hours = time_pattern.hour_pattern.search(duration)
            hours = int(hours.group(1)) if hours else 0 # Ternary condition
            
            minutes = time_pattern.minute_pattern.search(duration)
            minutes = int(minutes.group(1)) if minutes else 0
            
            seconds = time_pattern.second_pattern.search(duration)
            seconds = int(seconds.group(1)) if seconds else 0
            
            video_duration.append(YoutubePlaylistDuration(hours, minutes, seconds))

        for video in video_duration:
            total_seconds += int(video.getDurationSeconds())
        
        return int(total_seconds)
    
    
    def getVideoResponseViewCount(self):
        
        video_request = self.youtube_connection.videos().list(
            part='statistics,snippet',
            id=self.getAllVideoIds()
        )   
        video_response = video_request.execute()

        return video_response
    
    def getVideoViewCount(self):
        
        videos = []

        video_response = self.getVideoResponseViewCount()

        for item in video_response['items']:
            video_views = item['statistics']['viewCount']
            video_id = item['id']
            video_name = item['snippet']['title']
            youtube_link = f"https://www.youtu.be/{video_id}"

            videos.append(
                {
                    'views': int(video_views),
                    'url': youtube_link,
                    'name': video_name
                }
            )

        return videos