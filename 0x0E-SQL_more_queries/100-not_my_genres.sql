-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_show_genres
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE `title` = 'Dexter'
ORDER BY name ASC;