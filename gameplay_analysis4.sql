with first_login as(
    select 
        player_id,
        min(event_date) as first_date
    from Activity
    group by player_id
)

select 
    round(
      count(distinct a.player_id) * 1.0
      / (select count(*) from first_login),
      2
    ) as fraction
from first_login f
join Activity a
  on a.player_id = f.player_id
  and a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY);