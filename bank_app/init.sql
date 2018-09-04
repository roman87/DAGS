CREATE DATABASE romantest;
CREATE DATABASE currency;
\c currency;
CREATE TABLE bank (id serial PRIMARY KEY, time date, ccy VARCHAR(3), base_ccy VARCHAR(3), buy float, sale float, bank VARCHAR(255));
