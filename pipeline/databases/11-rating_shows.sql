-- shows rating
SELECT tv_shows.title AS title, tv_shows_ratings.rate AS rating
FROM tv_shows
ORDER BY  rating DESC
