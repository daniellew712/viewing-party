# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if not title or not genre or not rating: 
        return None
    new_movie = {"title": title, "genre": genre, "rating": rating}
    return new_movie


def add_to_watched(user_data, movie):
    if not user_data or not movie: 
        return None
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    if not user_data or not movie: 
        return None
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"] == title:

            user_data["watchlist"].remove(movie)

            user_data["watched"].append(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    if len(user_data["watched"]) == 0:
        return 0.0
    
    avr_rating = 0.0
    sum_of_ratings = 0
    for movie in user_data["watched"]:
        sum_of_ratings += movie["rating"]
        avr_rating = sum_of_ratings/len(user_data["watched"])
    return avr_rating

def get_most_watched_genre(user_data):
    if not user_data:
        return None
    
    freq_genre_dict = {}

    for movie in user_data["watched"]: 
        genre = movie["genre"]
        freq_genre_dict[genre] = freq_genre_dict.get(genre, 0) + 1

    most_freq_genre = ["", 0]

    for key, value in freq_genre_dict.items():
        if most_freq_genre[1] < value:
            most_freq_genre = [key, value]

    if most_freq_genre[1] == 0:
        return None
    else:
        return most_freq_genre[0]

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

