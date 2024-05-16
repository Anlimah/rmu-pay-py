CREATE DATABASE IF NOT EXISTS laf_pick_dev_db;
USE laf_pick_dev_db;

CREATE TABLE customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) GENERATED ALWAYS AS (CONCAT(first_name, ' ', last_name)) STORED,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255),
    gender VARCHAR(15)
);

CREATE TABLE notification_setting (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sms_enabled BOOLEAN DEFAULT 0,
    email_enabled BOOLEAN DEFAULT 0,
    app_enabled BOOLEAN DEFAULT 0,
    customer INT NOT NULL,
    CONSTRAINT fk_notification_setting_customer FOREIGN KEY (customer) REFERENCES customer (id) ON DELETE CASCADE ON UPDATE CASCADE
);