Python Generators Project
Overview

This project demonstrates advanced usage of Python generators to efficiently handle large datasets, process data in batches, and simulate real-world scenarios. It leverages the yield keyword for memory-efficient data processing while integrating with MySQL for dynamic data fetching.

Learning Objectives

Master Python Generators: Iterative data processing for memory efficiency.

Handle Large Datasets: Batch processing and lazy loading without overloading memory.

Simulate Real-world Scenarios: Live updates and streaming contexts.

Optimize Performance: Memory-efficient aggregate calculations (e.g., average age).

Integrate SQL: Fetch and process data dynamically from MySQL.

Requirements

Python 3.x

MySQL with database ALX_prodev and table user_data

Understanding of yield and generator functions

Basic knowledge of database schema design and seeding

Git and GitHub for version control

Project Structure

seed.py – Sets up database, tables, and seeds sample data

0-stream_users.py – Generator to fetch users one by one

1-batch_processing.py – Generator for batch processing and filtering users over age 25

2-lazy_paginate.py – Generator for lazy loading paginated data

4-stream_ages.py – Generator to yield user ages and calculate average memory-efficiently

README.md – Project overview

Usage

Seed the database:

python 0-main.py


Stream users one by one:

python 1-main.py


Batch processing:

python 2-main.py


Lazy loading paginated data:

python 3-main.py


Compute memory-efficient average age:

python 4-main.py

Notes

Uses generators (yield) for memory-efficient operations.

Demonstrates practical integration of Python with SQL databases.

Focused on scalable, real-world data handling techniques.
