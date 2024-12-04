CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    concert_name VARCHAR(100) NOT NULL,
    user_name VARCHAR(100),
    status VARCHAR(20) NOT NULL CHECK (status IN ('available', 'reserved', 'purchased'))
);