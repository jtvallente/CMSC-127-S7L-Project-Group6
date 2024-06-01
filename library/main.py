from database_commands import establish_server_connection
from welcome_page import main_menu


def entry_point():
    # Establish connection to the database
    host_name = "localhost"
    user_name = "root"
    user_password = "gno8fsbhrtx"
    database_name = "food_review_db"
    connection = establish_server_connection(host_name, user_name, user_password, database_name)
    # Pass the connection to the main menu if successful
    if(connection != None):
        main_menu(connection)


entry_point()