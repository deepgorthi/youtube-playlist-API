# Cumulative Youtube Playlist Time

## Overview

`get_playlist_times.py` code provides a way to get the total playlist time of each playlist in a given youtube channel. 

## Usage

This can be run using the Username of a given channel as a CLI argument to the python3 script. 

The Username of a channel can be extracted from the URL after searching for a channel in youtube search. 

For example, after searching for AWS channel, the username is the last part of the URL. https://www.youtube.com/user/AmazonWebServices  --> [AmazonWebServices]

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

# Most Popular Videos in a Playlist

## Overview

`get_popular_video_playlist.py` file is used to get most popular videos in a choosen playlist from a youtube channel. 

## Usage

The Username of a channel can be extracted from the URL after searching for a channel in youtube search. 

For example, after searching for AWS channel, the username is the last part of the URL. https://www.youtube.com/user/AmazonWebServices  --> [AmazonWebServices]

Once the username is extracted, give it as an argument to get_playlist_times.py file.

```bash
$ python3 get_popular_video_playlist.py AmazonWebServices
```

## Input

```
1 => AWS Knowledge Center Live - Best Practices and Troubleshooting Tips from AWS Support
2 => AWS Security Control Domains
3 => AWS Community Chats
4 => AWS Launch Announcements
5 => AWS Marketplace for Machine Learning
6 => AWS Well-Architected
7 => Getting Started with Amazon Kinesis Data Streams
8 => AWS Databases
9 => AWS What's Next
10 => Stories | Sports on AWS
11 => Powered By AWS | Sports on AWS
12 => Perspectives | Sports on AWS
13 => Ads | Sports on AWS
14 => IoT All the Things
15 => AWS Builder Stories
16 => Solving with AWS Solutions
17 => Migrate to Amazon EMR
18 => AWS for Microsoft Workloads: Amazon FSx for Windows File Server Series
19 => This is My Model
20 => AWS In Conversation With...
21 => AWS Has Proof
22 => 2020 AWS PubSec Customer References
23 => Conversations with Leaders
24 => Powered by Purpose, A Humanitarian Cloud Journey | AWS Imagine Grant Documentary Series
25 => AWS re:Invent 2019
26 => Continuous Monitoring in AWS GovCloud (US)
27 => AWS Thinkbox
28 => AWS Educate
29 => AWS Viewpoints
30 => AWS DeepRacer TV - Season 1
31 => AWS Curiosity Kid
32 => AWS Public Sector Summit - Canberra 2019
33 => AWS Public Sector Summit ASEAN - Singapore 2019
34 => Business Applications for Connected Data, Data Anlyst
35 => AWS ML Partner Webinars - Go deep on Machine Learning topics with AWS, just for APN partners
36 => AWS, We Have Proof
37 => AWS Summit Bahrain 2019
38 => IMAGINE: A Better World, Global Nonprofit Conference 2019
39 => AWS Changes the Game
40 => Open Source at AWS
41 => ISV Offerings in AWS Marketplace
42 => Windows Workloads on AWS
43 => AWS in the Public Sector - Italy
44 => twitch.tv/aws AWS Launchpad at New York Summit
45 => AWS Machine Learning
46 => Amazon SageMaker Technical Deep Dive Series
47 => APN Technical Baseline Review
48 => AWS New York Summit 2019 | Breakout Sessions
49 => AWS Fintech Day 2019
50 => AWS Management and Governance
Choose the index of playlist: 3
```

## Output

```
Title: What is a 2 Pizza Team?
URL: https://www.youtu.be/f27QQuzLoWY
Views: 937
============================================================
Title: Championing Inclusion and Diversity
URL: https://www.youtu.be/h-wmZcDVDRk
Views: 904
============================================================
Title: What is a Narrative?
URL: https://www.youtu.be/lw9EO04MpJU
Views: 641
============================================================
Title: What are the Amazon Leadership Principles?
URL: https://www.youtu.be/XcU3ul_eak4
Views: 566
============================================================
Title: Interactive Video Service
URL: https://www.youtu.be/_p81-WU1lQ0
Views: 258
============================================================
Title: AWS Partner: CEVO
URL: https://www.youtu.be/rJfXhlQow8Q
Views: 157
============================================================
Title: Stake on AWS Customer Story
URL: https://www.youtu.be/k5CAm1eGXsA
Views: 128
============================================================
Title: Grays Online on AWS Customer Story
URL: https://www.youtu.be/f5ZtJ93DcyE
Views: 96
============================================================
```

```
Choose the index of playlist: 3
Title: What is a 2 Pizza Team?
URL: https://www.youtu.be/f27QQuzLoWY
Views: 937
============================================================
Title: Championing Inclusion and Diversity
URL: https://www.youtu.be/h-wmZcDVDRk
Views: 904
============================================================
Title: What is a Narrative?
URL: https://www.youtu.be/lw9EO04MpJU
Views: 641
============================================================
Title: What are the Amazon Leadership Principles?
URL: https://www.youtu.be/XcU3ul_eak4
Views: 566
============================================================
Title: Interactive Video Service
URL: https://www.youtu.be/_p81-WU1lQ0
Views: 258
============================================================
Title: AWS Partner: CEVO
URL: https://www.youtu.be/rJfXhlQow8Q
Views: 157
============================================================
Title: Stake on AWS Customer Story
URL: https://www.youtu.be/k5CAm1eGXsA
Views: 128
============================================================
Title: Grays Online on AWS Customer Story
URL: https://www.youtu.be/f5ZtJ93DcyE
Views: 96
============================================================
Choose the index of playlist: 5
Title: AWS re:Invent 2018 – Announcing Machine Learning Solutions in AWS Marketplace
URL: https://www.youtu.be/rAMg6I5Hp4M
Views: 2651
============================================================
Title: AWS re:Invent 2018: [NEW LAUNCH!] Machine Learning w/ Amazon SageMaker & AWS Marketplace (AIM371)
URL: https://www.youtu.be/VKaJN3ylmUM
Views: 2105
============================================================
Title: Try Machine Learning Models from AWS Marketplace in Minutes
URL: https://www.youtu.be/7X4pIV8Wccw
Views: 1415
============================================================
Title: Deploy and Perform Inference on ML Models From AWS Marketplace Using a Jupyter Notebook
URL: https://www.youtu.be/j2urTXii2Sk
Views: 1322
============================================================
Title: Accelerate Machine Learning Projects with Hundreds of Algorithms and Models in AWS Marketplace
URL: https://www.youtu.be/OrmHHVI1uPk
Views: 1020
============================================================
Title: AWS re:Invent 2019: Deep dive on using AWS Data Exchange for ML and data analytics (MKT212)
URL: https://www.youtu.be/KgxTClsHSr4
Views: 700
============================================================
Title: (M09) Accelerating Machine Learning Projects
URL: https://www.youtu.be/GkKZt0s_ku0
Views: 686
============================================================
Title: Overview of how AWS Marketplace Supports Machine Learning Workloads
URL: https://www.youtu.be/-cwtovsr-ow
Views: 644
============================================================
Title: AWS re:Invent 2019: Build ML-powered applications with speed (MKT249-P)
URL: https://www.youtu.be/iLOXaWpK6ag
Views: 459
============================================================
Title: Explore the AWS Marketplace Developer Challenge: Machine Learning Powered Solutions
URL: https://www.youtu.be/BRCS7Q3u-ck
Views: 297
============================================================
Choose the index of playlist: q
Breaking from the input...
```

Inspired by @CoreyMSchafer's series on Youtube API. While Corey goes through how to use the Youtube API, I extended it to get the total times of each playlist in a given channel. 