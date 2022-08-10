-- script that lists all shows from hbtn_0d_tvshows_rate
SELECT title, SUM(rate) AS rating
FROM tv_shows
JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC;