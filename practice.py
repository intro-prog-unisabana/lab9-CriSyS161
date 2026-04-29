from song import Song
def print_songs(song_list):
    for song in song_list:
        print(song)
songs = [
    Song("Billie Jean", "Michael Jackson", 4.5),
    Song("tv off", "Kendrick Lamar", 3.7)
]
print_songs(songs)