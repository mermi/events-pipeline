CREATE EXTENSION "pgcrypto";

CREATE TABLE IF NOT EXISTS events (
    row_id varchar PRIMARY KEY,
	event_type int,
	event_time timestamp ,
    data JSON,
    processing_date Date
);