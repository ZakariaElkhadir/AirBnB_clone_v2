-- echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
-- echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | mysql -uroot -p
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
