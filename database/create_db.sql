CREATE TABLE IF NOT EXISTS Activities (
    activity_id TEXT PRIMARY KEY,
    username TEXT,
    added at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (username) REFERENCES Users(username)
);

CREATE TABLE IF NOT EXISTS text_channels (
	guild_id TEXT,
	channel_id TEXT,
);

CREATE TABLE IF NOT EXISTS events (
	event_id INT,
	campus_id INT,
	events_type INT
)
