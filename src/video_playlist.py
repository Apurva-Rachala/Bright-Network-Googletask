"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, name):
        # This will be the actual name that the user has entered 
        self.name = name

        # This will be the name we will be using for the purpose of uniquely identifying the playlist
        self.id = self.name.lower()
        
        # A list of video_ids
        self.videos = []
    
    # def is_valid_name(name):
    #     if len(name.split(' ')) > 1:
    #         return False
    #     return True