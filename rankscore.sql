select 
    score,
    DENSE_RANK() OVER (order by score desc) AS 'rank'
    
 FROM Scores
 order by score desc;