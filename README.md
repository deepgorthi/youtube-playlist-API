# youtube-playlist-times

## Overview

This code provides a way to get the total playlist time of each playlist in a given youtube channel. 

## Usage

This can be run using the Username of a given channel as a CLI argument to the python3 script. 

The Username of a channel can be extracted frim the URL after searching for a channel in youtube search. 

For example, after searching for AWS channel, the username is the last part of the URL. https://www.youtube.com/user/AmazonWebServices  --> <AmazonWebServices>

Once the username is extracted, give it as an argument to get_playlist_times.py file.

```bash
$ python3 get_playlist_times.py AmazonWebServices
```

## Output
```
Total duration of the playlist [AWS Knowledge Center Live - Best Practices and Troubleshooting Tips from AWS Support] is -> 02:02:45
Total duration of the playlist [AWS Security Control Domains] is -> 00:15:22
Total duration of the playlist [AWS Community Chats] is -> 00:30:03
Total duration of the playlist [AWS Launch Announcements] is -> 00:41:33
Total duration of the playlist [AWS Marketplace for Machine Learning] is -> 05:51:01
Total duration of the playlist [AWS Well-Architected] is -> 00:04:03
Total duration of the playlist [Getting Started with Amazon Kinesis Data Streams] is -> 00:21:50
Total duration of the playlist [AWS Databases] is -> 07:47:19
Total duration of the playlist [AWS What's Next] is -> 23:27:23
Total duration of the playlist [Stories | Sports on AWS] is -> 00:43:50
Total duration of the playlist [Powered By AWS | Sports on AWS] is -> 00:13:48
Total duration of the playlist [Perspectives | Sports on AWS] is -> 01:08:45
Total duration of the playlist [Ads | Sports on AWS] is -> 00:04:39
Total duration of the playlist [IoT All the Things] is -> 03:26:39
Total duration of the playlist [AWS Builder Stories] is -> 00:09:24
Total duration of the playlist [Solving with AWS Solutions] is -> 01:57:25
Total duration of the playlist [Migrate to Amazon EMR] is -> 01:12:34
Total duration of the playlist [AWS for Microsoft Workloads: Amazon FSx for Windows File Server Series] is -> 01:18:51
Total duration of the playlist [This is My Model] is -> 00:14:56
Total duration of the playlist [AWS In Conversation With...] is -> 03:16:36
Total duration of the playlist [AWS Has Proof] is -> 00:03:37
Total duration of the playlist [2020 AWS PubSec Customer References] is -> 00:37:57
Total duration of the playlist [Conversations with Leaders] is -> 05:41:10
Total duration of the playlist [Powered by Purpose, A Humanitarian Cloud Journey | AWS Imagine Grant Documentary Series] is -> 00:24:31
Total duration of the playlist [AWS re:Invent 2019] is -> 10:08:48
Total duration of the playlist [Continuous Monitoring in AWS GovCloud (US)] is -> 00:24:47
Total duration of the playlist [AWS Thinkbox] is -> 03:52:50
Total duration of the playlist [AWS Educate] is -> 00:32:51
Total duration of the playlist [AWS Viewpoints] is -> 00:10:55
Total duration of the playlist [AWS DeepRacer TV - Season 1] is -> 02:01:52
Total duration of the playlist [AWS Curiosity Kid] is -> 00:02:04
Total duration of the playlist [AWS Public Sector Summit - Canberra 2019] is -> 28:58:01
Total duration of the playlist [AWS Public Sector Summit ASEAN - Singapore 2019] is -> 11:26:43
Total duration of the playlist [Business Applications for Connected Data, Data Anlyst] is -> 00:00:00
Total duration of the playlist [AWS ML Partner Webinars - Go deep on Machine Learning topics with AWS, just for APN partners] is -> 26:19:45
Total duration of the playlist [AWS, We Have Proof] is -> 00:02:04
Total duration of the playlist [AWS Summit Bahrain 2019] is -> 01:51:08
Total duration of the playlist [IMAGINE: A Better World, Global Nonprofit Conference 2019] is -> 08:34:45
Total duration of the playlist [AWS Changes the Game] is -> 00:04:26
Total duration of the playlist [Open Source at AWS] is -> 32:04:58
Total duration of the playlist [ISV Offerings in AWS Marketplace] is -> 00:07:54
Total duration of the playlist [Windows Workloads on AWS] is -> 00:25:56
Total duration of the playlist [AWS in the Public Sector - Italy] is -> 09:19:20
Total duration of the playlist [twitch.tv/aws AWS Launchpad at New York Summit] is -> 04:07:57
Total duration of the playlist [AWS Machine Learning] is -> 00:44:21
Total duration of the playlist [Amazon SageMaker Technical Deep Dive Series] is -> 04:30:05
Total duration of the playlist [APN Technical Baseline Review] is -> 00:39:52
Total duration of the playlist [AWS New York Summit 2019 | Breakout Sessions] is -> 12:05:30
Total duration of the playlist [AWS Fintech Day 2019] is -> 03:33:17
Total duration of the playlist [AWS Management and Governance] is -> 07:41:33

```

Inspired by @CoreyMSchafer's series on Youtube API. While Corey goes through how to use the Youtube API, I extended it to get the total times of each playlist in a given channel. 