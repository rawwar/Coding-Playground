with raw_reviews as (
select * from airbnb.raw.raw_reviews
)

select 
listing_id,
date as review_date,
comments as review_text,
sentiment as review_statement
    
from
    raw_reviews