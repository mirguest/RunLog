
-- useage:

--     $ mysql --user=root -p
--     > create database runlog;
--     > grant all privileges on runlog.* to 'run'@'localhost' identified by 'run';
--     > exit
--     $ mysql -u run -prun --database=runlog < schema.sql

SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+8:00";

ALTER DATABASE CHARACTER SET "utf8";

drop table if exists daily_run_log;
create table daily_run_log (
    id int not null auto_increment primary key,
    runner_id int not null references runners(id),
    day date not null
);

create index date_index on daily_run_log (day);

drop table if exists runners;
create table runners (
    id int not null auto_increment primary key,
    email varchar(100) not null unique,
    name varchar(100) not null
);
