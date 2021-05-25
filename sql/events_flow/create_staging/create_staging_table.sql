CREATE EXTENSION "pgcrypto";

CREATE TABLE IF NOT EXISTS staging.events (
	event_type int,
	event_time timestamp ,
    data JSON,
    processing_date Date
);