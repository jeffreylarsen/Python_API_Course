-- Active: 1676670736721@@127.0.0.1@5432@python_api_course
CREATE TABLE Posts (
    "id" SERIAL NOT NULL,
    "title" VARCHAR NOT NULL,
    "content" VARCHAR NOT NULL,
    "published" BOOLEAN NOT NULL DEFAULT True,
    "created" TIMESTAMP NOT NULL DEFAULT Now(),
    --"user_id" INT NOT NULL,
    --FOREIGN KEY (id) REFERENCES Users (id),
    PRIMARY KEY (id)
);

SELECT * FROM Posts;

SELECT * FROM Posts JOIN Users ON Posts.user_id = Users.id;

SELECT Posts.*, email FROM Posts LEFT JOIN Users ON Posts.user_id = Users.id;

SELECT users.id, users.email, COUNT(posts.id) as user_post_count FROM Posts RIGHT JOIN Users ON Posts.user_id = Users.id GROUP BY Users.id;

SELECT posts.*, votes.user_id FROM posts RIGHT JOIN votes ON posts.id = votes.post_id;

SELECT posts.*, COUNT(votes.post_id) as votes
FROM posts 
LEFT JOIN votes ON posts.id = votes.post_id 
-- WHERE posts.id = 4
GROUP BY posts.id;

INSERT INTO Posts (title, content, user_id)
VALUES 
('This is my first SQL Post', 'I am writing SQL now! Fuck this was difficult.', 4), 
('This is my second SQL Post', 'I am getting the hang of this a little but shit man.', 4);

INSERT INTO posts (title, content, user_id)
VALUES 
-- ('First Post', 'First Post.', 1), 
('This is my second', 'shit man.', 2);

DELETE FROM posts;

DELETE FROM posts * WHERE id = 3;

DROP TABLE Posts;

--USERS OPTIONS

SELECT * FROM users;

INSERT INTO users (email, password) 
VALUES 
('jeff@gmail.com', 'hahah'),
('jd@gmail.com', 'hahah');

--DELETE FROM Products WHERE name = 'TV';
DELETE FROM users *;

DELETE FROM users WHERE id = 4;

DROP TABLE users;

--Votes Table Options

SELECT * FROM votes;

DELETE FROM VOTES *;

DROP TABLE votes;


SELECT posts.id AS posts_id, posts.title AS posts_title, posts.content AS posts_content, posts.published AS posts_published, posts.created AS posts_created, posts.user_id AS posts_user_id, count(votes.post_id) AS votes 
FROM posts LEFT OUTER JOIN votes ON votes.post_id = posts.id GROUP BY posts.id;

SELECT * FROM alembic_version;

DROP TABLE alembic_version;