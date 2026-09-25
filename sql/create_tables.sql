create table if not exists finances (

    id varchar(100) primary key,
    source varchar(100),
    amount numeric(10,2),
    note varchar(100),
    sub_note varchar(100),
    transaction_date date,
    date_range varchar(100),
    owner varchar(100)

);