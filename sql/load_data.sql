insert into finances (

    id
    , source
    , amount
    , note
    , sub_note
    , transaction_date
    , date_range
    , owner

)

values (
    %s
    ,%s 
    ,%s 
    ,%s 
    ,%s 
    ,%s
    ,%s
    ,%s
)

on conflict (id) do update set 
    transaction_date = excluded.transaction_date
;