playlist = {}
while True:
    print('\n---- Playlist Manager ----')
    print("1. Add Song")
    print("2. Remove Song")
    print("3. View Playlist")
    print("4. Search Song")
    print("5. Exit")

    choice = int(input("Enter your choice: ").strip())
    if choice == 1:
        title = input("Enter your Song's Title: ").strip()
        artist = input("Enter your Song's Artist: ").strip()
        if title in playlist:
            print("Song already exists")
        else:
            playlist[title] = artist
            print("Song added")
    elif choice == 2:
        title = input("Enter your Song's Title: ").strip()
        if title not in playlist:
            print("Song does not exist")
        else:
            del playlist[title]
            print(f"Song removed: {title}")
    elif choice == 3:
        if playlist:
            print("\nYour Playlist")
            for title, artist in playlist.items():
                print(f"Title: {title}, Artist: {artist}")
    elif choice == 4:
        title = input("Enter your Song's Title: ").strip()
        if title in playlist:
            print(f"{title} is in your playlist, sung by {playlist[title]}.")
    elif choice == 5:
        print("Stopping the program.. have a nice day!")
        break
    playlist = {}
while True:
    print('\n---- Playlist Manager ----')
    print("1. Add Song")
    print("2. Remove Song")
    print("3. View Playlist")
    print("4. Search Song")
    print("5. Exit")

    choice = int(input("Enter your choice: ").strip())
    if choice == 1:
        title = input("Enter your Song's Title: ").strip()
        artist = input("Enter your Song's Artist: ").strip()
        if title in playlist:
            print("Song already exists")
        else:
            playlist[title] = artist
            print("Song added")
    elif choice == 2:
        title = input("Enter your Song's Title: ").strip()
        if title not in playlist:
            print("Song does not exist")
        else:
            del playlist[title]
            print(f"Song removed: {title}")
    elif choice == 3:
        if playlist:
            print("\nYour Playlist")
            for title, artist in playlist.items():
                print(f"Title: {title}, Artist: {artist}")
    elif choice == 4:
        title = input("Enter your Song's Title: ").strip()
        if title in playlist:
            print(f"{title} is in your playlist, sung by {playlist[title]}.")
    if choice == 5:
        print("Exiting Playlist Manager.. Have a nice day!")
        break
    else:
        print("Wrong Choice.. Choose from (1-5)")
