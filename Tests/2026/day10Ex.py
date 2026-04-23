
Album= {
    "title": "The Dark Side of the Moon",
    "artist": "Pink Floyd",
    "year": 1973,
    "tracks":("Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse")
}
print(Album)
#Iterate over the keys and values of the dictionary you create in exercise 1. For each key and value, you should print the name of the key, and then the value alongside it.
for key, value in Album.items():
    print(f'{key}: {value}')

# #Delete the track list and year of release from the dictionary you created. Once you've done this, add a new key to the dictionary to store the date of release. The date of release for The Dark Side of the Moon was March 1st, 1973.
# del Album["tracks"]
# del Album["year"]
# Album["release_date"] = "March 1st, 1973"
# for key, value in Album.items():
#     print(f'{key}: {value}')
print(Album["artist"])
print(Album.get("artists", "wrong text"))