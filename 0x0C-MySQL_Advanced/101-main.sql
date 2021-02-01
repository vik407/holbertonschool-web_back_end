-- Show and compute overall weighted score
SELECT * FROM users;
SELECT * FROM projects;
SELECT * FROM corrections;

CALL ComputeOverallWeightedScoreForUsers();

SELECT "--";
SELECT * FROM users;