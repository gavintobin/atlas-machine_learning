-- average scores
DELIMITER//

DECLARE avg_score DECIMAL(5,2);

    -- Calculate the average score for the given user_id
    SELECT AVG(score) INTO avg_score
    FROM scores
    WHERE id = ComputeAverageScoreForUser.user_id;

    -- Update the average score in the users table
    UPDATE users
    SET average_score = score
    WHERE id = ComputeAverageScoreForUser.user_id;
END//

DELIMITER ;
