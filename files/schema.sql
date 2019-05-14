CREATE TABLE location_type(
 lt_id INTEGER PRIMARY KEY,
 lt_type TEXT NOT NULL
);

CREATE TABLE location(
 location_id INTEGER PRIMARY KEY,
 location TEXT NOT NULL,
 lt_id INTEGER NOT NULL,
 FOREIGN KEY(lt_id) REFERENCES location_type(lt_id)
);

CREATE TABLE category(
 category_id INTEGER PRIMARY KEY,
 c_name TEXT NOT NULL
);

CREATE TABLE tag(
 tag_id INTEGER PRIMARY KEY,
 t_name TEXT NOT NULL
);

CREATE TABLE artist(
 artist_id INTEGER PRIMARY KEY,
 a_firstname TEXT NOT NULL,
 a_lastname TEXT NOT NULL,
 a_info TEXT,
 a_webpage TEXT
);

CREATE TABLE mediaset(
 ms_id INTEGER PRIMARY KEY,
 ms_name TEXT NOT NULL,
 location_id INTEGER,
 artist_id INTEGER,
 FOREIGN KEY(location_id) REFERENCES location(location_id),
 FOREIGN KEY(artist_id) REFERENCES artist(artist_id)
);

CREATE TABLE media(
 media_id INTEGER PRIMARY KEY,
 m_name TEXT NOT NULL,
 m_description TEXT,
 m_notes TEXT,
 location_id INTEGER NOT NULL,
 ms_id INTEGER,
 artist_id INTEGER,
 FOREIGN KEY(location_id) REFERENCES location(location_id),
 FOREIGN KEY(ms_id) REFERENCES mediaset(ms_id),
 FOREIGN KEY(artist_id) REFERENCES artist(artist_id)
);

CREATE TABLE media_category(
 media_category_id INTEGER PRIMARY KEY,
 media_id INTEGER NOT NULL,
 category_id INTEGER NOT NULL,
 FOREIGN KEY(media_id) REFERENCES media(media_id),
 FOREIGN KEY(category_id) REFERENCES category(category_id)
);

CREATE TABLE media_tag(
 media_tag_id INTEGER PRIMARY KEY,
 media_id INTEGER NOT NULL,
 tag_id INTEGER NOT NULL,
 FOREIGN KEY(media_id) REFERENCES media(media_id),
 FOREIGN KEY(tag_id) REFERENCES tag(tag_id)
);

CREATE TABLE mediaset_category(
 ms_category_id INTEGER PRIMARY KEY,
 ms_id INTEGER NOT NULL,
 category_id INTEGER NOT NULL,
 FOREIGN KEY(ms_id) REFERENCES mediaset(ms_id),
 FOREIGN KEY(category_id) REFERENCES category(category_id)
);

CREATE TABLE mediaset_tag(
 ms_tag_id INTEGER PRIMARY KEY,
 ms_id INTEGER NOT NULL,
 tag_id INTEGER NOT NULL,
 FOREIGN KEY(ms_id) REFERENCES mediaset(ms_id),
 FOREIGN KEY(tag_id) REFERENCES tag(tag_id)
);

INSERT INTO location_type (lt_type)
VALUES ("url"),("filepath");

INSERT INTO category (c_name)
VALUES ('Nature'),('Portrait'),('Landscape');

INSERT INTO tag (t_name)
VALUES ('Squirrel'),('Mona Lisa'),('Stonehenge');

INSERT INTO artist (a_firstname, a_lastname)
VALUES ('John', 'Doe'), ('Jane', 'Doe');
