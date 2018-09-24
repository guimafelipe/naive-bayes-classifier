import inputparser

def normalize(arr, _n_stars):
	for key in arr:
		for ind, el in enumerate(arr[key]):
			arr[key][ind] = el/_n_stars[ind]

class Naive_Bayes:
	def __init__(self):
		self.ratings = inputparser.get_data()

		self.genre_freq = {}
		self.age_freq = {}
		self.gender_freq = {}
		self.ocupation_freq = {}
		
		self.n_stars = [0]*5

		for rate in self.ratings:
			_stars = rate.stars - 1
			self.n_stars[_stars] += 1
			for genr in rate.movie.genre:
				if genr not in self.genre_freq:
					self.genre_freq[genr] = [0]*5
				self.genre_freq[genr][_stars] += 1
			_age = rate.user.age
			if _age not in self.age_freq:
				self.age_freq[_age] = [0]*5
			self.age_freq[_age][_stars] += 1
			_gender = rate.user.gender
			if _gender not in self.gender_freq:
				self.gender_freq[_gender] = [0]*5 
			self.gender_freq[_gender][_stars] += 1
			_ocupation = rate.user.ocupation
			if _ocupation not in self.ocupation_freq:
				self.ocupation_freq[_ocupation] = [0]*5
			self.ocupation_freq[_ocupation][_stars] += 1
		
		# normalize(self.gender_freq, self.n_stars)
		# normalize(self.age_freq, self.n_stars)
		# normalize(self.genre_freq, self.n_stars)
		# normalize(self.ocupation_freq, self.n_stars)
	
	def query(self, genre, age, gender, ocupation):
		probs = [1]*5
		tot_rats = sum(self.n_stars)
		tot_oc = sum(self.ocupation_freq[ocupation])
		tot_gender = sum(self.gender_freq[gender])
		tot_genre = sum(self.genre_freq[genre])
		tot_age = sum(self.age_freq[age])
		for ind, _ in enumerate(probs):
			# P(R|X) = P(X|R)*P(R)/P(X)
			probs[ind] *= (self.ocupation_freq[ocupation][ind]/self.n_stars[ind])*(self.n_stars[ind]/tot_rats)/(tot_oc/tot_rats)
			probs[ind] *= (self.gender_freq[gender][ind]/self.n_stars[ind])*(self.n_stars[ind]/tot_rats)/(tot_gender/tot_rats)
			probs[ind] *= (self.age_freq[age][ind]/self.n_stars[ind])*(self.n_stars[ind]/tot_rats)/(tot_age/tot_rats)
			probs[ind] *= (self.genre_freq[genre][ind]/self.n_stars[ind])*(self.n_stars[ind]/tot_rats)/(tot_genre/tot_rats)
		return probs

	def priori_query(self, movie_id):
		n = 0
		tot = 0
		for rate in self.ratings:
			if rate.movie.id == movie_id:
				n += 1
				tot += rate.stars
		return tot/n

if __name__ == "__main__":
	nb = Naive_Bayes()
	print(nb.query("Comedy", 1, "F", 10))
	pass