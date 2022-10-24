CREATE TABLE IF NOT EXISTS token(
    id SERIAL PRIMARY KEY,
    token TEXT,
    expires_in TEXT,
    maxRequestsForHourPeriod INTEGER,
    maxRequestsForDayPeriod INTEGER,
    expires TEXT
);