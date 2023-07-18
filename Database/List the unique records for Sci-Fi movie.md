List the unique records for Sci-Fi movies where male 24-year-old students 
have given 5-star ratings.

+---------------------+
| Tables_in_movielens |
+---------------------+
| genres              |
| genres_movies       |
| movies              |
| occupations         |
| ratings             |
| users               |
+---------------------+

SELECT * FROM rating WHERE  user_id=(SELECT users.id FROM users LEFT JOIN occupations ON users.occupation_id = occupations.id WHERE users.gender = 'M' AND users.age = 24 AND occupations.name = 'Student')


SELECT * FROM ratings WHERE  user_id IN (SELECT users.id FROM users LEFT JOIN occupations ON users.occupation_id = occupations.id WHERE users.gender = 'M' AND users.age = 24 AND occupations.name = 'Student');

SELECT DISTINCT movies.title
FROM movies
LEFT JOIN genres_movies ON movies.id = genres_movies.movie_id
LEFT JOIN genres ON genres.id = genres_movies.genre_id
LEFT JOIN ratings ON movies.id = ratings.movie_id
LEFT JOIN users ON users.id = ratings.user_id
LEFT JOIN occupations ON users.occupation_id = occupations.id 
WHERE users.gender = 'M' 
  AND users.age = 24 
  AND occupations.name = 'Student'
  AND ratings.rating = 5
  AND genres.name = 'Sci-Fi'
ORDER BY movies.title;
