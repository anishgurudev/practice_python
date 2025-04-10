tup =  (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
 )
#album,artist, release year, track
album,artist, release_year, track = tup

# Convert this outer tuple to a dictionary with four keys.
albums = {"album" : "The Dark Side of the Moon",
          "artist": "Pink Floyd",
          "release_year": 1973,
          "tracks": (
              "Speak to Me",
              "Breathe",
              "On the Run",
              "Time",
              "The Great Gig in the Sky",
              "Money","Us and Them",
              "Any Colour You Like",
              "Brain Damage",
              "Eclipse"
          )
          }
# 2) Iterate over the keys and values of the dictionary you create in exercise 1. For each key and value, you should print the name of the key, and then the value alongside it.
for key,value in albums.items():
    print(f"{key}: {value}")
# 3) Delete the track list and year of release from the dictionary you created. Once you've done this, add a new key to the dictionary to store the date of release. The date of release for The Dark Side of the Moon was March 1st, 1973.
del albums["release_year"]
albums["date of release"] = "13th july 2012"
# print(albums[release_year])
print(albums.get("release_year","uknown"))

for key,value in albums.items():
    print(f"{key}: {value}")
# If you use a different album for the exercises, update the date accordingly.

# 4) Try to retrieve one of the values you deleted from the dictionary. This should give you a KeyError. Once you've tried this, repeat the step using the get method to prevent the exception being raised
print(albums[release_year])
