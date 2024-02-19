-- echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
-- echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | mysql -uroot -p
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
