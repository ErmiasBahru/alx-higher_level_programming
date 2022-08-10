-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT tv_shows.title AS title FROM tv_shows
INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = "Comedy"
ORDER BY title ASC;