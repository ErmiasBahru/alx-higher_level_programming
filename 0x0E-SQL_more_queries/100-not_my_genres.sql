-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT g.name
FROM tv_genres g
WHERE g.name NOT IN (
      SELECT g.name
      FROM tv_genres g
      INNER JOIN tv_show_genres m ON g.id = m.genre_id
      INNER JOIN tv_shows s ON m.show_id = s.id
      WHERE s.title = 'Dexter'
)
ORDER BY g.name ASC;
