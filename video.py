from pytube import *
from threading import *
import os

class VideoCollection:
    """
    This is a class to store a collection of object variables of type Video
    """
    collection = {}


    def get_videos(self):
        return self.collection

    def add_video(self, video):
        self.collection[video.get_id()] = video

    def count(self):
        return self.collection.__len__()

    def count_err(self, errDict):
        return errDict.get(0).__len__()

# class MultiDownloader(Thread):
#     """
#     This is a class that downloads a video
#     """
#
#     def __init__(self, dir_name="", url=""):
#         super().__init__()
#         self.video_manager = VideoManager()
#
#     def run(self):
#         self.video_manager.download()


class VideoManager:
    """
    This is a class to manage the video catalog
    """

    err = []
    base_prefix_path = "C:\\Users\\"

    def __init__(self):
        self.video_collection = VideoCollection()
        self.error_handler = ErrorHandler()

    def download_multiple(self,
                          videos: list,
                          dir_name: str = None,
                          path: str = "DEFAULT",
                          format: str = "mp4"):
        """
        Function to download multiple videos

        :param videos:
        :param dir_name:
        :param path:
        :param format:
        :return:
        """
        for video_id in videos:
            self.download(video_id=video_id, dir_name=dir_name, path=path, format=format)

    def download(self,
                 video_id: str,
                 dir_name: str = None,
                 path: str = "DEFAULT",
                 format: str = "mp4"):
        """
        Function to download a single video
        :param video_id: Video() type object: ID, URL and FILENAME
        :param dir_name: Directory name
        :param path: Absolute path
        :param format: File extension
        :return: bool
        """
        usr = os.getlogin()

        # Find the video with video_id = video_id
        vid = self.video_collection.get_videos().get(video_id)
        if not vid:
            print("ERROR: Video not found")
            return False
        elif vid:
            pass

        yt = YouTube(vid.get_url())
        yt.set_filename(vid.get_filename())
        video = yt.get(format)

        if path == "DEFAULT" and dir_name :

            path = self.base_prefix_path + usr + "\\Desktop\\" + dir_name
            self.err.append(path)
            ch = self.error_handler.existing_dir()
            if ch == False:
                f = input("Folder name on which to save video: ")
                path = "C:\\Users\\" + usr + "\\Desktop\\" + f
            self.make_dir(path)
            video.download(path)

        elif path=="DEFAULT" and dir_name == None:

            path = self.base_prefix_path + usr + "\\Desktop"
            video.download(path)

        elif path !="DEFAULT" and dir_name:
            self.err.append(path)
            ch = self.error_handler.existing_dir()
            if ch == False:
                f = input("Folder name on which to save video: ")
                path = "C:\\Users\\" + usr + "\\Desktop\\" + f
            self.make_dir(path)

        elif path !="DEFAULT" and dir_name == None:
            path = path
            try:
                video.download(path)
            except OSError:
                self.myself = self.__class__()
                self.myself.go_through_collection(filename="nfskja")
                print("ERROR: filename '" + vid.get_filename() + "' for video ID " + vid.get_id() + \
                     " is being used by video ID " + self.myself.go_through_collection(filename=vid.get_filename()))

    def go_through_collection(self, filename=None, id=None, url=None):
        if filename:
            s = self.video_collection.get_videos()
            for self.key in s:
                print(self.key)
                t_f = s.get(self.key).get('filename') is filename
                if t_f == False:
                    continue
                else:
                    return self.key

    def make_dir(self, dir_path: str):
        """
        Create directory if it does not exist
        :param dir_path:
        :return:
        """
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        else:
            pass

    def play(self):
        pass

    def stop(self):
        pass

    def replay(self):
        pass

    def delete(self):
        pass

    def add(self, video_obj_id):
        vid = self.video_collection
        self.myself = self.__class__()
        self.myself.go_through_collection(filename=vid.get_videos().get(video_obj_id).get('filename'), id=vid.get_videos().get(video_obj_id).get('id'), url=vid.get_videos().get(video_obj_id).get('url'))
        self.video_collection.add_video(video_obj_id)

class Video():
    """
    This class stores video information
    """

    def __init__(self,
                 id: str,
                 url: str,
                 filename: str):

        self.id = id
        self.url = url
        self.filename = filename

    def get_url(self):
        return self.url

    def get_id(self):
        return self.id

    def get_filename(self):
        return self.filename

class ErrorHandler():
    tnames=[]
    def __init__(self):
        r = VideoManager
        n = len(r.err)
        self.name = "thread"
        a = 0
        for i in range(n):
            a += 1
            self.tnames.append(self.name+str(a))


    def path_not_found(self):
        pass

    def existing_dir(self, store_in_dir=False):
        rev = VideoManager()
        reviser = rev.err
        a = 0
        for item in reviser:
            check_path = reviser[a]
            a += 1
            if store_in_dir == True:
                pass
            elif store_in_dir == False:
                if os.path.exists(item):
                    optY = ['y', 'Y']
                    optN = ['n', 'N']
                    print("The path for directory you have chosen already exists: " + check_path)
                    self.chopt = input("Download video in this directory? [Y]es / [n]o? ")
                    if self.chopt in optY:
                        break
                    elif self.chopt in optN:
                        return False
                    else:
                        print("Enter 'y' or 'n': ")
                        redo = ErrorHandler()
                        redo.existing_dir(check_path)
                else:
                    pass

# Create Video Manager object
vmanager = VideoManager()

# Create video objects
video1 = Video(id="Test",url="https://www.youtube.com/watch?v=CkIrizsP64c&list=PL1A2CSdiySGIPxpSlgzsZiWDavYTAx61d",filename="Test")
video2 = Video(id="Test2",url="https://www.youtube.com/watch?v=tKdWpiSZO8M&index=2&list=PL1A2CSdiySGIPxpSlgzsZiWDavYTAx61d",filename="Test2")

# Add videos to 'collection' dictionary
vmanager.add(video1)
vmanager.add(video2)

# Downloads videos on selected path
vmanager.download(video_id="Test", path= "C:\\Users\\")
vmanager.download(video_id="Test2", path= "C:\\Users\\")

