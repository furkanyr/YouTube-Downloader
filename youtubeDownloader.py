from pytube import YouTube

url = input("enter url: ")

YouTube(url).streams.get_highest_resolution().download("")