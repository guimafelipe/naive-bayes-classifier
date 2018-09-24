import src.naivebayes as naive
import src.inputparser

if __name__ == "__main__":
	nb = naive.Naive_Bayes()

	while(True):
		qry = input("Introduza o id do filme, seu sexo, sua ocupação e sua faixa etária:").split(" ")
		movie_id = int(qry[0])
		gender = qry[1]
		ocupation = int(qry[2])
		age = int(qry[3])

		result = nb.query(movie_id , age, gender, ocupation)

		sum_res = sum(result)
		curr_max_w = 0
		predicted = 0
		for star, wheight in enumerate(result):
			if curr_max_w < wheight:	
				curr_max_w = wheight
				predicted = star + 1
		priori_res = nb.priori_query(movie_id)
		print(nb.movies[movie_id].name, ". Bayes:", predicted, ", Priori: ", priori_res ,"\n")


