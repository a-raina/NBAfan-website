CREATE TABLE nba2014 (

player text,
position text,
age int,
team text,
minutesPlayed numeric(10,3),
fieldGoalPercentage numeric(10,3),
threePointPercentage numeric(10,3),
freeThrowPercentage numeric(10,3),
totalreboundsPG numeric(10,3),
assistsPG numeric(10,3),
stealsPG numeric(10,3),
blocksPG numeric(10,3),
personalFoulsPG numeric(10,3),
pointsPG numeric(10,3)
);


tr "\r" "\n" < /Accounts/weissb/nba2013.csv > nba2013.csv

\copy nba2013 FROM '/Accounts/weissb/nba2013.csv' DELIMITER ',' CSV