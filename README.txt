Assignment 1: Twitter Data Crawler
Nick Milikich
CSE 60437 Social Sensing & Cyber-Physical Systems
February 3, 2019

This project implements three crawlers that perform various tasks related to gathering information from Twitter, and stores that information in text files. The first crawler collects profile information from users whose ID's are stored in the file IDs.dat and writes their information to Assignment1_1_output.txt. The second crawler collects social network information (the first 20 friends and followers) from users whose ID's are stored in the file IDs.dat and writes that information to Assignment1_2_output.txt. The third crawler collects the most recent 50 tweets containing one or more keywords stored in the file Keywords.dat and writes those tweets to Assignment1_3a_output.txt, and collects the most recent 50 tweets originating from the geographic location specified in Region.dat and writes those tweets to Assignment1_3b_output.txt.

The crawlers can be run simply by executing the file Assignment1.py. No arguments need to be passed to the program. This code was tested using Python version 2.7.16.

Running this source code requires that the Python packages NumPy and Tweepy be installed.

To run the source code, the following should be included in the same directory (all included in this submission):
   
   - A file named Keys.dat that contains the four keys and tokens necessary to authenticate the API.
   - A file named IDs.dat that contains a list of Twitter user ID numbers, separated by lines, that the crawler will collect information on for tasks 1 and 2.
   - A file named Keywords.dat that contains a list of keywords, separated by lines, for which to search Twitter in task 3a.
   - A file named Region.dat that contains a list of coordinates, separated by lines, in which to search for tweets. The coordinates should be in the same order as given in the assignment description (top left longitude, top left latitude, bottom right longitude, bottom right latitude).