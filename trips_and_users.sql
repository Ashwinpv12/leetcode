select 
    t.request_at as day,
    ROUND(
        sum(case
        when t.status in ('cancelled_by_client','cancelled_by_driver')
        then 1
        else 0
        end)* 1.0 /count(*),
        2
    ) as "Cancellation Rate"
from Trips t
join Users c
    on t.client_id = c.users_id
join users d
    on t.driver_id = d.users_id
where   
    c.banned = 'No'
    and d.banned = 'No'
    and t.request_at between '2013-10-01' and '2013-10-03'
group by
    t.request_at
having
    count(*)>=1
order by
    t.request_at;           



