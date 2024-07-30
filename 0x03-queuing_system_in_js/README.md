Queuing System in JS

# Redis Basic

This project demonstrates the basic usage of Redis, including installation, key-value operations, and server management.

## Installation and Setup

1. Download and extract Redis:
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
Copy
2. Compile Redis:
make
Copy
## Usage

1. Start the Redis server:
src/redis-server &
Copy
2. Use the Redis CLI to interact with the server:
src/redis-cli
Copy
3. Set a key-value pair:
SET Holberton School
Copy
4. Retrieve a value:
GET Holberton
Copy
## Server Management

1. Find the Redis server process:
ps aux | grep redis-server
Copy
2. Kill the Redis server:
kill [PID_OF_Redis_Server]
Copy
## Data Persistence

The `dump.rdb` file in the project root contains the persisted Redis data. When Redis loads this file, it should have the "Holberton" key set to "School".

## Requirements

- Running `GET Holberton` in the Redis client should return "School"
- The `dump.rdb` file should be present in the project root

## Author

Davis Koech

## Acknowledgments

This project is part of the ALX Backend curriculum.