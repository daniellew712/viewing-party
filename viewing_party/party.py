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
    
    total_rating = 0.0
    avg_rating = 0.0

    for movie in user_data["watched"]:

        total_rating += movie["rating"]

    avg_rating = total_rating/len(user_data["watched"])

    return avg_rating

def get_most_watched_genre(user_data):

    frequency_genre = {}
    if len(user_data["watched"]) == 0:
        return None
    for movie in user_data["watched"]:
        genre = movie["genre"]
        frequency_genre[genre] = frequency_genre.get(genre, 0) + 1

    max_movie_genre = None
    max_count = 0

    for genre, num in frequency_genre.items():
        if num > max_count:
            max_count = num
            max_movie_genre = genre
    return max_movie_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    movie_friends_watched = []
    unique_movie = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            movie_friends_watched.append(movie["title"])

    for movie in user_data["watched"]:
        if movie["title"] not in movie_friends_watched:
            unique_movie.append(movie)
    return unique_movie

def get_friends_unique_watched(user_data):
    movie_friends_watched = []
    user_not_watched = []
    user_watched = []
    #movie that friends have all watched
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            movie_friends_watched.append(movie)
    #movie that user has watched
    for movie in user_data["watched"]:
        user_watched.append(movie["title"])
    #append the movie that friends watched but user not watched
    for movie in movie_friends_watched:
        if movie["title"] not in user_watched and movie not in user_not_watched:

            user_not_watched.append(movie)

    return user_not_watched
  
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    
    recomme_movie_list = []
    user_watched_set = set()
    for movie in user_data["watched"]:
        user_watched_set.add(movie["title"])
    
    unique_title_set = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched_set:
                    if movie["host"] in user_data["subscriptions"]:
                        if movie["title"] not in unique_title_set:
                            recomme_movie_list.append(movie)
                            unique_title_set.add(movie["title"])

    return recomme_movie_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
#first function of wave 5







