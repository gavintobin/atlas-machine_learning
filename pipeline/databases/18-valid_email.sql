-- valid email
CREATE TRIGGER ResetValidEmail
AFTER UPDATE ON users
FOR EACH ROW
WHEN OLD.email <> NEW.email
BEGIN
    UPDATE users
    SET valid_email = FALSE
    WHERE id = NEW.id;
END;

