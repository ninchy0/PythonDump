
from pytube import YouTube


class YoutubeDownloader:

    def __init__(self, link):

        # ask for the link from user
        self.link = link
        self.yt = YouTube(link)

    def download(self):

        # Showing details
        print("Title: ", self.yt.title)
        print("Number of views: ", self.yt.views)
        print("Length of video: ", self.yt.length)
        print("Rating of video: ", self.yt.rating)

        # Getting the highest resolution possible
        self.yt = self.yt.streams.get_highest_resolution()

        # Starting download
        print("Downloading...")
        self.yt.download()
        print("Download completed!!")


if __name__ == '__main__':

    link = input("Enter the link of YouTube video you want to download: ")
    myObj = YoutubeDownloader(link)
    myObj.download()
