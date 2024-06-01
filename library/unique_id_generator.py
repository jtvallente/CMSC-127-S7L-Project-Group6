import datetime
import random
import string

# Utililty function for unique ID
def generate_unique_id():
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    random_characters = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

    return f"{timestamp}{random_characters}"