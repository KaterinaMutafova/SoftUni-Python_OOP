from project_ex8_spoopify.album import Album
from project_ex8_spoopify.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        filtered_albums = [a for a in self.albums if a.name == album_name]
        if not filtered_albums:
            return f"Album {album_name} is not found."
        the_album = filtered_albums[0]
        if the_album.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(the_album)
        return f"Album {album_name} has been removed."

    def details(self):
        result = f"Band {self.name}\n"
        for a in self.albums:
            result += a.details()
        return result



song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())











