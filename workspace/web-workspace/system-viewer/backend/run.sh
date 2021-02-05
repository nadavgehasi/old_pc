#!/bin/bash

# When runs without docker we should create the directory
mkdir -p database

# If this is the first time the app runs, use the default database
cp -n db.sqlite3.initial database/db.sqlite3

# Hand off to the CMD
exec "$@"
