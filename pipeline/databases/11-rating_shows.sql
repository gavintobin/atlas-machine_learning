-- shows rating
SELECT tv_shows.title AS title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
ORDER BY  rating DESC
