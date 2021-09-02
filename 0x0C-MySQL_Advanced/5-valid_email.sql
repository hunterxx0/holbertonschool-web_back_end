-- Email validation to sent
delimiter !!
CREATE TRIGGER e_val
BEFORE UPDATE ON users FOR EACH ROW
BEGIN
IF NEW.email <> OLD.email THEN SET NEW.valid_email = 0;
END IF;
END;
!!