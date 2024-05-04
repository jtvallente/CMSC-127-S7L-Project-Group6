# Food Reviews Information System
# CMSC 127 Final Project

## Description
This information system allows users to record, in electronic form, data on food reviews and food items from food establishments.

## Features
- Add, update, and delete a food review (on a food establishment or a food item)
- Add, delete, search, and update a food establishment
- Add, delete, search, and update a food item

## Reports
- View all food establishments
- View all food reviews for an establishment or a food item
- View all food items from an establishment
- View all food items from an establishment that belong to a food type (meat, veg, etc.)
- View all reviews made within a month for an establishment or a food item
- View all establishments with a high average rating (rating >= 4) (ratings from 1-5; highest is 5)
- View all food items from an establishment arranged according to price
- Search food items from any establishment based on a given price range and/or food type

## Setup
1. Clone the repository to your local machine.
2. Open your MySQL client and connect to your local MySQL server (use mysql.server start for macOS and then use mysql -u root -p)
4. Install the mysql connector by running this on the terminal 'pip3 install mysql-connector-python'
5. Run or source the SQL script `database_commands.sql` that is in root folder of this app to create the necessary database and table.
6. Open the the connector.py and change the password to the password of your own mysql.
7. Run the python app using 'Python3 App.py'

## Technologies Used
- MySQL
- Python3


## Team Members
- James Lourence T. Vallente
- Angelica Mae Licup
- Christian Rojano

## Notes to the members:
- Please add the files/functions inside the library folder


