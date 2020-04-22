def check_movies(flight_length, movie_lengths):

    length = 0

    movies = {}
    for movie in movie_lengths:
        movies[movie] = movie
        length += 1

    if (length == 1) and (flight_length != movie_lengths[0]):
        return False
    elif (length == 1) and (flight_length == movie_lengths[0]):
        return True

    for movie in movie_lengths:
        remaining_time = flight_length - movie
        if movies.get(remaining_time, "Missing") == "Missing":
            return False
        else:
            return True


def can_two_movies_fill_flight_solution(movie_lengths, flight_length):
    # Movie lengths we've seen so far
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    # We never found a match, so return False
    return False


length = 120
movies = [30, 90, 20, 1, 4, 3]
print(check_movies(length, movies))
