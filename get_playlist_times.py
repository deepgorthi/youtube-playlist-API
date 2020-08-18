#!/usr/bin/env python3

from channel_info import ChannelInfo
from youtube_playlist import YoutubePlaylist
from youtube_playlist_duration import YoutubePlaylistDuration
from youtube_playlist_item import YoutubePlaylistItem
from playlist_info import PlaylistInfo
from time_pattern import TimePattern

import argparse

def main(username):

    # channel = ChannelInfo(username)
    # channel_id = channel.getChannelId()

    playlist = YoutubePlaylist(username)
    playlist_id, playlist_name = playlist.getPlaylistIdTitle()

    nextPageToken = None
    total_duration = {}
    playlist_information = []

    for i in range(len(playlist_id)):

        total_duration[playlist_id[i]] = 0

        while True:

            playlist_item = YoutubePlaylistItem(nextPageToken, playlist_id[i])
            playlist_item_response = playlist_item.getPlaylistItem()

            total_duration[playlist_id[i]] += playlist_item.getVideoDuration()
            
            nextPageToken = playlist_item_response.get('nextPageToken')

            if not nextPageToken:
                break

        playlist_information.append(PlaylistInfo(playlist_id[i], playlist_name[i], total_duration[playlist_id[i]]))

    return playlist_information


def printInfo(playlist_information):

    for playlistInfo in playlist_information:
        minutes, seconds = divmod(playlistInfo.getDuration(), 60)
        hours, minutes = divmod(minutes, 60)
        print(f"Total duration of the playlist [{playlistInfo.getTitle()}] is -> {hours:02}:{minutes:02}:{seconds:02}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="Username of the Youtube Channel")
    args = parser.parse_args()
    printInfo(main(args.username))