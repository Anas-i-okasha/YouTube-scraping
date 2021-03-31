from pytube import YouTube
link = input('Enter the video link? ')
video = YouTube(link)
# print(f'the video title is :{video.title}')
# print(f'video rating is : {video.rating}')
# print(f'video views is : {video.views}')
# print(f'video length is : {video.length} in second')

# print(video.streams)
def finish():
    print('download succsess')

video.streams.get_lowest_resolution().download(output_path='D:\python\youtube_download')
video.register_on_complete_callback(finish())