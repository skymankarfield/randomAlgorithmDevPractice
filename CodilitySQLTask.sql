----------Create tables------------
CREATE TABLE transfers(name varchar(30) not null, money integer not null);
INSERT INTO transfers VALUES('andrea', -10000);
INSERT INTO transfers VALUES('mark', 149513);
INSERT INTO transfers VALUES('kassidy', -5016);
INSERT INTO transfers VALUES('andrea', 17500);
INSERT INTO transfers VALUES('andrea', 2500);
INSERT INTO transfers VALUES('jim', 100000);
INSERT INTO transfers VALUES('jim', -50);
INSERT INTO transfers VALUES('jim', -50);
INSERT INTO transfers VALUES('jim', -50);
INSERT INTO transfers VALUES('kassidy', -2013);
----------Create tables------------

----------Create table sum_of_deposits------------
CREATE TABLE sum_of_deposits AS
    SELECT name, sum(money) as sum_of_deposits
    FROM transfers WHERE money > 0
    GROUP BY name;
----------Create table sum_of_deposits------------

----------Create table sum_of_withdrawals------------
CREATE TABLE sum_of_withdrawals AS
    SELECT name, abs(sum(money)) as sum_of_withdrawals
    FROM transfers WHERE money < 0
    GROUP BY name;
----------Create table sum_of_withdrawals------------

----------Create final table [name, sum_of_deposits, sum_of_withdrawals]------------
CREATE TABLE atm AS
SELECT *
FROM sum_of_deposits LEFT JOIN sum_of_withdrawals USING(name)
UNION ALL
SELECT name, NULL, sum_of_withdrawals
FROM sum_of_withdrawals LEFT JOIN sum_of_deposits USING(name)
WHERE sum_of_deposits IS NULL
ORDER BY name;
----------Create final table [name, sum_of_deposits, sum_of_withdrawals]------------

----------Change values null to 0------------
UPDATE atm SET sum_of_deposits=0 WHERE sum_of_deposits IS NULL;
UPDATE atm SET sum_of_withdrawals=0 WHERE sum_of_withdrawals IS NULL;
----------Change values null to 0------------

----------Show final table------------
SELECT * FROM atm;
----------Show final table------------
