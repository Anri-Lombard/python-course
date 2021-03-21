from c128ch1 import albums

SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONG_LIST_INDEX]
    else:
        break

    print(f"Please choose your song from {albums[choice - 1][0]}'s album (invalid choice exists): ")
    for index, (also_index, final_song) in enumerate(songs_list):
        print(f"{index + 1}: {final_song}")

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        song = songs_list[song_choice - 1][SONG_TITLE_INDEX]
    else:
        continue

    if 1 <= song_choice <= len(songs_list):
        print(f"\nJukebox playing {song}\n")
    print(f"{'-' * 40}")
