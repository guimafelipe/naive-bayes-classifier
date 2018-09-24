# Naive Bayes Classifier

## Using the program

You can run it using

```
python3 main.py
```

It will build the naive bayes tables and as you for a input. I this input, you will need to pass four values.
These will be the movie id (check out the movies.dat file), the sex (M or F), the ocupation (a integer between 0 and 20), and
the age (1, 18, 25, 35, 45, 50 or 56).

So, as instance, if we are a 21 years old college student woman and we want to know the most probable rate we would give to Toy Story
 (which id is 1), we should pass the following as input: `1 M 4 18`.
 
 As result, we will get the estimated rate for naive bayes algorithm, and also the priori algorithm.
