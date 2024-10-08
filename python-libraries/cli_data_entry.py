from rich.console import Console
from rich.table import Table
import csv
import os

# Create a Console instance
console = Console()
console.print("Here is some Music Data:", style="bold cyan")

# Create a table
table = Table(title="Popular Music")

# Define table columns
table.add_column("Song Title", justify="left", style="cyan", no_wrap=True)
table.add_column("Artist", justify="left", style="green")
table.add_column("Release Year", style="yellow")
table.add_column("Spotify Streams (in million)", justify="right", style="magenta")


# Add some music data 

table.add_row("Kill Bill", "SZA", "2023", "2,100")
table.add_row("Shape of You", "Ed Sheeran", "2017", "3,500")
table.add_row("greedy", "Tate McRae", "2023", "1,000")
table.add_row("As It Was", "Harry Styles", "2022", "2,300")


# Print the table to the console
console.print(table)


console.print("\n[bold cyan]Now I want you to enter your preferred music:[/bold cyan]")



# Expand on this script
def get_user_input():
    song_title = input("Enter the song name: ")
    artist_name = input("Enter the name of the artist: ")
    release_year = input("Enter the release year of the music: ")
    streams = input("Enter the streams of the song (in million): ")
    return song_title, artist_name, release_year, streams


#Function to confirm if the data is correct
def confirm_data(song_title, artist_name, release_year, streams):
    console.print(f"\n[bold yellow]Please confirm the data you entered:[/bold yellow]")
    console.print(f"Song Title: {song_title}")
    console.print(f"Artist: {artist_name}") 
    console.print(f"Release Year: {release_year}")
    console.print(f"Spotify Streams: {streams} million")
    return input("\nIs the data correct? (yes/no): ").strip().lower() == 'yes'


# Function to save data to a file
def save_data_to_file(data, filename="music_data.csv"):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, filename)
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Song Title", "Artist", "Release Year", "Spotify Streams (in million)"])
        for i in range(len(data)):
            writer.writerow(data[i])
    console.print(f"\n[bold green]Data has been saved to: {file_path}[/bold green]")


# main function to run the script
def main():
    music_data = []
    
    while True:
        
        song_title, artist_name, release_year, streams = get_user_input()

        
        if confirm_data(song_title, artist_name, release_year, streams):
            music_data.append([[song_title], [artist_name], [release_year], [streams]])
            console.print("\n[bold green]Data confirmed and added.[/bold green]")
        else:
            console.print("\n[bold red]Please re-enter the data.[/bold red]")
            continue

        
        if input("\nDo you want to add another song? (yes/no): ").strip().lower() != 'yes':
            break
    
    # Save the data to a file
    save_data_to_file(music_data)

if __name__ == "__main__":
    main()



