#!/usr/bin/env python3

from channel_info import ChannelInfo
from youtube_playlist import YoutubePlaylist
from youtube_playlist_item import YoutubePlaylistItem
from view_count import ViewCount

import argparse

def main(username):

    # channel = ChannelInfo(username)
    # channel_id = channel.getChannelId()

    playlist = YoutubePlaylist(username)
    playlist_id, playlist_name = playlist.getPlaylistIdTitle()

    nextPageToken = None
    videos = {}
    view_count_information = []

    for i in range(len(playlist_id)):

        videos[playlist_id[i]] = []

        while True:

            playlist_item = YoutubePlaylistItem(nextPageToken, playlist_id[i])
            playlist_item_response = playlist_item.getPlaylistItem()

            videos[playlist_id[i]] = playlist_item.getVideoViewCount()
            # print(videos[playlist_id[i]])
            videos[playlist_id[i]].sort(key=lambda vid: vid['views'],reverse=True)

            nextPageToken = playlist_item_response.get('nextPageToken')

            if not nextPageToken:
                break

        view_count_information.append(ViewCount(playlist_id[i], playlist_name[i], videos[playlist_id[i]]))

    return view_count_information


def printInfo(view_count_information):

    for i in range(1, len(view_count_information)+1):
        print(f"{i} => {view_count_information[i-1].getTitle()}")

    while True:
        
        try:
            user_choice = input("Choose the index of playlist: ")
            selection = int(user_choice,base=10)
            print(f"".center(60,'='))
            if selection in range(1, len(view_count_information)+1):
                for video in view_count_information[selection-1].getPopularVideos():
                    print(f"Title: {video['name']}") 
                    print(f"URL: {video['url']}")
                    print(f"Views: {video['views']}")
                    print(f"".center(60,'='))

            elif not selection in range(1, len(view_count_information)+1):
                print(f"{selection} is out of bounds of the playlist number. Please choose between 1 and {len(view_count_information)+1}")
        
        except ValueError:
            print(f"Breaking from the input...")
            break
        

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="Username of the Youtube Channel")
    args = parser.parse_args()

    printInfo(main(args.username))