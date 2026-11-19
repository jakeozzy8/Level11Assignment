import pandas as pd

# Load the original catalog (this file is never modified)
df = pd.read_csv("video_games_raw.csv")
last_row = len(df) - 1

print("VIDEO GAME CATALOG MANAGER")

# Ask for a row number and keep asking until it's a valid row
row_choice = int(input("Enter a row number to inspect: "))

while not (0 <= row_choice <= last_row):
    row_choice = int(input(f"Please enter a number between 0 and {last_row}: "))

# Display the selected game using .iloc[] (access a row by position)
selected_game = df.iloc[row_choice]

print("\nSelected Game:")
print(f"Title: {selected_game['Title']}")
print(f"Platform: {selected_game['Platform']}")
print(f"Genre: {selected_game['Genre']}")
print(f"Rating: {selected_game['Rating']}")
print(f"Current Status: {selected_game['Status']}")

# Update the game's status using .at[] (change one specific value)
update_status = input("\nEnter a new status:\n")
df.at[row_choice, "Status"] = update_status

# Add the Recommended column: "No" by default, then .loc[] sets "Yes"
# for games rated at least 8 that cost $40 or less
df["Recommended"] = "No"
df.loc[
    (df["Rating"] >= 8) & (df["Price"] <= 40),
    "Recommended"
] = "Yes"

# Filter and display the recommended games using .query()
recommended_games = df.query("Recommended == 'Yes'")[["Title", "Platform", "Price", "Rating"]]

print("\nRecommended Games:")
print(recommended_games)

# Save the updated catalog to a new file using .to_csv()
df.to_csv("video_games_cleaned.csv", index=False)

print("\nThe catalog has been updated.")
print("Saved as video_games_cleaned.csv.")
