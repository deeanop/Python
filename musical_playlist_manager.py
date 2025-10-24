import time
import random

main_playlist = list()

print("Welcome to the Musical Playlist Manager!\n" 
"                    ~~~Menu~~~\n" 
"1. Add Song at the end.\n" 
"2. Add Song at a certain position.\n" 
"3. Search Song.\n" 
"4. Delete Song by name.\n" 
"5. Delete Song by position\n" 
"6. Sort the playlist alphabetically.\n" 
"7. Sort the playlist reverse alphabetically.\n"
"8. Give the number of songs.\n"
"9. Run the playlist in order.\n"
"10. Run the playlist randomly.\n" 
"11. Run the playlist in a loop.\n"
"12. Add a sub-playlist.\n" 
"13. Display the playlist.\n"
"14. Export the playlist's content to a .txt file.\n"
"15. Exit.\n" 
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

choice = int(input("Enter a command from 1 to 15. "))
while True:
    if choice == 1:
        song_name = input(" You have chosen to add a song to the end. Enter the name of your song. ")
        main_playlist.append(song_name)
        print("The song was added at the end of your playlist.\n")
    elif choice == 2:
        song_name = input("You have chosen to add a song to a given position. Enter the name of your song. ")
        position = int(input("Enter the position where the song will be inserted"))
        main_playlist.insert(position, song_name)
        print("The song was added at the given position.\n")
    elif choice == 3:
        song_name = input("You have chosen to search a song in your playlist. Enter the name of your song. ")
        if song_name in main_playlist:
            position = main_playlist.index(song_name)
            print(f"The song was found in the playlist in the {position} position.\n")
        else:
            print("The song was not found in your playlist.\n")
    elif choice == 4:
        song_name = input("You have chosen to delete a song by name. Enter the name of your song. ")
        if song_name in main_playlist:
            main_playlist.remove(song_name)
            print("The song was removed from your playlist.\n")
        else:
            print("The song is not in your playlist.\n")
    elif choice == 5:
        position = int(input("You have chosen to delete a song by its position. Enter the position of your song. "))
        if position < len(main_playlist):
            main_playlist.pop(position)
            print("The song was eliminated from your playlist.\n")
        else:
            print("The position is out of range.\n")
    elif choice == 6:
        print("You have chosen to sort the playlist alphabetically.\n")
        main_playlist.sort()
        print("Your playlist was sorted alphabetically.\n")
    elif choice == 7:
        print("You have chosen to sort the playlist alphabetically reversed.\n")
        main_playlist.sort(reverse = True)
        print("Your playlist was sorted alphabetically reversed.\n")
    elif choice == 8:
        print("You have chosen to get the number of the songs in your playlist.\n")
        number_of_songs = len(main_playlist)
        print(f"Your playlist has {number_of_songs} songs.\n")
    elif choice == 9:
        print("You have chosen to run the playlist in order.\n")
        for i in main_playlist:
            print(i)
            time.sleep(10)
        print("Your playlist has finished.\n")
    elif choice == 10:
        print("You have chosen to run the playlist randomly.\n")
        finished_songs = []
        while len(finished_songs) < len(main_playlist):
            song_number = random.randint(0, len(main_playlist) - 1)
            if song_number not in finished_songs:
                print(main_playlist[song_number])
                finished_songs.append(song_number)
                time.sleep(10)
        print("Your playlist has finished.\n")
    elif choice == 11:
        iterations = int(input("Tou have chosen to run your playlist in a loop. Enter the name of iterations. "))
        for i in range(iterations):
            for j in main_playlist:
                print(j)
                time.sleep(10)
        print("Your playlist has finished.\n")
    elif choice == 12:
        sub_playlist = []
        song_name = input("You have chosen to add a sub-playlist. Enther the name of a song. Write 'Stop' to finish the process. ")
        while song_name != "Stop":
            sub_playlist.append(song_name)
            print("The song was added to your sub-playlist.\n")
            song_name = input("Enther the name of a song. Write 'Stop' to finish the process. ")
        main_playlist.extend(sub_playlist)
        print("The sub-playlist was added to your main playlist.\n")
    elif choice == 13:
        print("You have chosen to display your playlist.\n")
        for i in main_playlist:
            print(f"{main_playlist.index(i)}. {i}")
        print("\n")
    elif choice == 14:
        file_name = input("You have chosen to export the playlist's content. Enter the name of the file. ")
        with open(file_name, "w") as file:
            for i in main_playlist:
                file.write(i + "\n")
        print(f"Your playlist was exported to {file_name}.\n")
    elif choice == 15:
        print("You have chosen to exit the program. Goodbye.\n")
        exit()
    else:
        print("Unknown command.\n")
    choice = int(input("Enter a command from 1 to 15. "))
    