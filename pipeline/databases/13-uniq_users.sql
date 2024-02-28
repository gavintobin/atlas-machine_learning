-- make table users
CREATE TABLE users (
    id INT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
)
