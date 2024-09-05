import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def config(self):
        self.SECRET_KEY = os.getenv('SECRET_KEY')
        self.ITOP_URL = os.getenv('ITOP_URL')
        self.API_URL = os.getenv('API_URL')
        self.PORT = os.getenv('PORT')
