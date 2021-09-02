-- In and not out
CREATE TABLE IF NOT EXISTS users (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
email VARCHAR(256) NOT NULL UNIQUE,
name VARCHAR(256),
country ENUM('TN', 'US','CO') NOT NULL DEFAULT 'TN');
