from Main import YoutubeConverter as YTC_class

YTC = YTC_class()

while True:
    print("1. Download a song")
    print("2. Download a playlist")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        while True:
            print("Use a URL or a name")
            print("1. URL")
            print("2. Name")
            print("3. Back")
            choice = input("Enter your choice: ")
            if choice == "1":
                url = input("Enter the URL of the song: ")
                YTC.Song_Download(url=url)
            elif choice == "2":
                name = input("Enter the name of the song: ")
                YTC.Song_Download(name=name)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
    elif choice == "2":
        url = input("Enter the URL of the playlist: ")
        YTC.Playlist_Download(url=url)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")