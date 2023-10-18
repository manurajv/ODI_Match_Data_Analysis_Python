import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from urllib.request import urlopen

# Load the data from CSV files
match_data = pd.read_csv('ODI_Match_Data.csv')
match_info = pd.read_csv('ODI_Match_info.csv')

def visualize_matches_over_years():
    # Group matches by year and count them
    matches_per_year = match_data['season'].str[:4].value_counts().sort_index()

    # Plot the number of matches per year
    plt.figure(figsize=(10, 6))
    matches_per_year.plot(kind='bar')
    plt.title('Number of ODI Matches Per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Matches')
    plt.xticks(rotation=45)
    plt.show()

def visualize_top_run_scorers():
    # Group and sum runs scored by each player
    top_run_scorers = match_data.groupby('striker')['runs_off_bat'].sum().nlargest(10)

    # Plot the top run scorers
    plt.figure(figsize=(10, 6))
    top_run_scorers.plot(kind='bar')
    plt.title('Top 10 Run Scorers in ODI Matches')
    plt.xlabel('Batsman')
    plt.ylabel('Total Runs')
    plt.xticks(rotation=45)
    plt.show()

def visualize_result_distribution():
    # Count the number of matches with each result
    result_distribution = match_info['result'].value_counts()

    # Plot the result distribution
    plt.figure(figsize=(8, 8))
    result_distribution.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Distribution of Match Results')
    plt.show()

def visualize_matches_won_by_country():
    # Count the number of matches won by each country
    matches_by_country = match_info['winner'].value_counts()

    # Plot the matches won by countries
    plt.figure(figsize=(10, 6))
    matches_by_country.plot(kind='bar')
    plt.title('Matches Won by Countries')
    plt.xlabel('Country')
    plt.ylabel('Number of Matches')
    plt.xticks(rotation=45)
    plt.show()

def visualize_top_wicket_takers():
    # Filter the data where 'wicket_type' is not null and not 'run out'
    filtered_data = match_data[(match_data['wicket_type'].notnull()) & (match_data['wicket_type'] != 'run out')]
    
    # Group the filtered data by the bowlers and calculate their total wickets
    wicket_takers = filtered_data['bowler'].value_counts().nlargest(10)

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    wicket_takers.plot(kind='bar')
    plt.title('Top 10 Highest Wicket Takers in ODI Matches')
    plt.xlabel('Bowler')
    plt.ylabel('Total Wickets')
    plt.xticks(rotation=45)
    plt.show()

def visualize_top_player_of_the_match():
    top_players = match_info['player_of_match'].value_counts().nlargest(10)

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    top_players.plot(kind='bar')
    plt.title('Top 10 Players with the Most Player of the Match Awards')
    plt.xlabel('Player')
    plt.ylabel('Number of Awards')
    plt.xticks(rotation=45)
    plt.show()

# Function to fetch a background image from a URL
def get_background_image_from_url(url):
    response = urlopen(url)
    image = Image.open(response)
    return ImageTk.PhotoImage(image)

# Define the URL for the background image
background_image_url = 'https://wallpapers.com/images/featured-full/cricket-ground-9yo8w016faiow66m.jpg'

# Create a GUI window
root = tk.Tk()
root.title('Cricket Data Analysis')

# Set the width and height of the GUI window
window_width = 800
window_height = 600 
root.geometry(f"{window_width}x{window_height}")

# Load and display the background image from the URL
bg_image = get_background_image_from_url(background_image_url)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for the text with bold letters
title_label = ttk.Label(root, text="ODI Men's Cricket Matches (2002-2023)", font=("Helvetica", 14, "bold"))
title_label.pack(pady=30)

# Create buttons to execute the selected function
button1 = ttk.Button(root, text='Matches Over Years', command=visualize_matches_over_years)
button1.pack(pady=15)

button2 = ttk.Button(root, text='Matches won by Country', command=visualize_matches_won_by_country)
button2.pack(pady=15)

button3 = ttk.Button(root, text='Result Distribution', command=visualize_result_distribution)
button3.pack(pady=15)

button4 = ttk.Button(root, text='Top Run Scorers', command=visualize_top_run_scorers)
button4.pack(pady=15)

button5 = ttk.Button(root, text='Top Wicket Takers', command=visualize_top_wicket_takers)
button5.pack(pady=15)

button6 = ttk.Button(root, text='Top Player of the match', command=visualize_top_player_of_the_match)
button6.pack(pady=15)

# Start the GUI main loop
root.mainloop()


