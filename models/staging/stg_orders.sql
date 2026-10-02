select
    id as order_id,
    user_id as customer_id,
    status,
    order_date,
    amount
from {{ source('jaffle_shop', 'orders') }}
