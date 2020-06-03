import webbrowser
import random
from youtube_search import YoutubeSearch
import time
import numpy as np
import pafy
import youtube_dl



def watch_vids(num_videos, links):
	print("Beginning the Algorithm...")

	#Total number of videos
	total_num_vids = len(links)

	#Sampling Random Indices with no replacement
	random_indices = np.random.choice(len(links), size=num_videos, replace=False)

	for idx in random_indices:

		#Url to video
		url = links[idx]

		#Opens the video in a new tab
		webbrowser.open_new_tab(url) #You can change this for your convenience
		
		#Getting length of YouTube Video
		video = pafy.new(links[idx]) #Creating pafy object
		time.sleep(video.length) #length attribute gives the length in seconds

def main():

	max_results = 30 #number of random BLM videos to query from YouTube
	results = YoutubeSearch('black lives matter -fox', max_results=max_results).to_dict() #query YouTube for videos, exclude Fox news

	#generate list of youtube links
	links = ["https://youtube.com" + l["link"] for l in results]


	#Edit this line to choose the amount of videos you want the algorithm to launch
	num_videos = None

	watch_vids(num_videos, links)

if __name__ == '__main__':
	main()