# this is a version of the program that utilizes an existing lyrics genius package to
# populate the bot with lyrics, in teh future I would like to directly interface with the genius API
# I would also like to abstract the specific artist from the code so that the bot can more easily be
# repurposed for other artists

import lyricsgenius
import random
import tweepy

# all fo the necessary access keys for the twitter API

artist = "Alice Longyu Gao"
# this becomes unmanageable for artists with bigger discographies
all_songs = "I ˂/3 Harajuku", "Rich Bitch Juice", "She Abunai", "Dumb Bitch Juice", "Rich Bitch Juice (Laura Les Remix)", "Underrated Popstar", "100 Boyfriends", \
            "Scam", "Karma Is a Witch", "Magnificroissant", "Kanpai", "I Want My Hoe Time Back", "Never Coming Back", "Horizontal", "Yung Piece of Shit Shut Up", \
            "U Think U Can Fuck with Me Dont Ya", "DTM", "Quarantine Rly Sucks", "I ˂3 Harajuku (demo)", "Bleeding in The Studio", "Chew!", "LEGEND - ALG Mix", \
            "Crying at CVS", "I Will Eat Your Intestines", "To My White Boy Princess", "Witch Bitch Juice", "Rich Bitch Juice (Dylan Brady Remix)", \
            "Rich Bitch Juice (HANA Remix)", "Whoreroscope", "Kanye West Saved My Life", "Rich Bitch Juice (Gupi Remix)", \
            "Kawaii Queen", "A Song to Perform at an ASCAP Awards After Party When Wining",  "Princess of Manifestation", "Bros in the Hamptons", \
            "Rich Bitch Juice (Blu DeTiger Remix)", "Rich Bitch Juice (Count Baldor Remix)", "Quarantine Rly Sucks (Gupi Remix)", "She Abunai - Baauer Remix"


keys = {
    'CONSUMER_API_KEY': '3RLPfSrJjyN7vqooRflAXusXU',
    'CONSUMER_API_SECRET_KEY': 'XVrodVwTQzC1YyFL70ogjy4WP4qQh3Xigp7shSvngpZhBx8obi',
    'ACCESS_TOKEN': '2950586998-cDpgwyeFVn7O7IOSDoYIKv7yc6B0kYD5XoQ4FmZ',
    'ACCESS_TOKEN_SECRET': '4GnPnHQr2yugdN4ie0iUNwblX472cSHH7ZpcwpC6gPXZa',
}

# def get_artist_songs(artist_name):
#     genius = lyricsgenius.Genius('yxwDNA9lYhJkglJXUKx5FMyfIRRhXJHeYkUwxW_pRJ-5IlB4f4uwlN6oFhUE5NGP')
#     artist = genius.search_artist(artist_name)
#
#     artist_song_list = artist.songs
#
#     return artist_song_list

# extract one song from the list of songs
def get_single_song():
    song = random.choice(all_songs)
    return song

# retrieve the lyrics of a song
def get_song_lyrics():
    genius = lyricsgenius.Genius('yxwDNA9lYhJkglJXUKx5FMyfIRRhXJHeYkUwxW_pRJ-5IlB4f4uwlN6oFhUE5NGP')
    song = get_single_song()
    lyrics = genius.search_song(song, artist).lyrics
    return lyrics

# clean up the lyrics
def clean_lyrics():
    lyrics = get_song_lyrics()
    song_lines = lyrics.split('\n')
    for i in range(len(song_lines)):
        if song_lines[i] == "" or "[" in song_lines[i]:
            song_lines[i] = "REMOVE THIS LINE"
    song_lines = [i for i in song_lines if i != "REMOVE THIS LINE"]
    return song_lines


# formulate tweet
def make_tweet():
    lyrics = clean_lyrics()
    num = random.randrange(0, len(lyrics) - 1)
    tweet = lyrics[num] + "\n" + lyrics[num + 1]
    tweet = tweet.replace("\\", "")
    return tweet

# post tweet
# def handler(event, context):
auth = tweepy.OAuthHandler(keys['CONSUMER_API_KEY'], keys['CONSUMER_API_SECRET_KEY'])
auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)
tweet = make_tweet()
status = api.update_status(tweet)
  # return tweet


