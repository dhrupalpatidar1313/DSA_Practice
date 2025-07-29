import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.environ.get('DB_URL')

class DatabaseConnection:
    """Simulate Database Connection with context management."""
    
    def __init__(self,db_name):
        self.db_name = db_name
        self.connected = False
        
    def __enter__(self):
        """Establish the Database Connection."""
        self.connected =True
        print(f"Connected to the Database '{self.db_name}'.")
        return self
    
    def __exit__(self,exc_type,exc_value , traceback):
        """Exist the Database Connection."""
        
        self.connected = False
        print(f"Disconnected from the database '{self.db_name}'.")
        
        if exc_type:
            print(f"An exception occurred : {exc_value}")
            return True
        
with DatabaseConnection('') as db :
    print()