from youtube_transcript_api import YouTubeTranscriptApi
import urllib, lxml
from lxml import etree


"""
Basic Usage
- copy-paste urls of your target videos in the same style as the 4 links that are alread in "target_urls" right below.
- run code using green button in header
- downloadable transcripts will be generated for each vid in the left 
sidebar below main.py
- In the output on the right hand side you can see an overview of download
successes and failures.
Note: Adding punctuation to transcripts programmatically is surprisingly hard.
"""


target_urls = [ 
		"https://www.youtube.com/watch?v=V37eWVm-9BA",
		"https://www.youtube.com/watch?v=Hm4Sg086uLg",
		"https://www.youtube.com/watch?v=B2-QCv-hChY",
		]


def get_title(url):
	youtube = lxml.etree.HTML(urllib.urlopen(url).read())
	video_title = youtube.xpath("//span[@id='eow-title']/@title")
	return ''.join(video_title)


def get_transcript(url):
	vid_id = url.split("youtube.com/watch?v=")[-1]
	transcript = YouTubeTranscriptApi.get_transcript(vid_id)
	transcript_text = [each["text"] for each in transcript]
	return " ".join(transcript_text)


def save_transcript(title, transcript):
	file_name = title.lower().replace(" ", "_") + ".txt"
	with open(file_name, "w") as f:
		f.write(title + "\n\n")
		f.write(transcript)


for url in target_urls:
	try:
		title = get_title(url)
		transcript = get_transcript(url)
		save_transcript(title, transcript)
		print("Success: " + title + "\n")
	except Exception as e:
		print("Error: " + title + "\n")
