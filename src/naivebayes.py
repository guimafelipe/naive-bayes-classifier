import inputparser

if __name__ == "__main__":
    ratings = inputparser.get_data()

    genre_freq = {}
    age_freq = {}
    gender_freq = {}
    ocupation_freq = {}
    
    for rate in ratings:
        _stars = rate.stars - 1
        for genr in rate.movie.genre:
            if genr not in genre_freq:
                genre_freq[genr] = [0]*5
            genre_freq[genr][_stars] += 1
        _age = rate.user.age
        if _age not in age_freq:
            age_freq[_age] = [0]*5
        age_freq[_age][_stars] += 1
        _gender = rate.user.gender
        if _gender not in gender_freq:
           gender_freq[_gender] = [0]*5 
        gender_freq[_gender][_stars] += 1
        _ocupation = rate.user.ocupation
        if _ocupation not in ocupation_freq:
            ocupation_freq[_ocupation] = [0]*5
        ocupation_freq[_ocupation][_stars] += 1

    print(genre_freq)
    print(gender_freq)
    print(age_freq)
    print(ocupation_freq)