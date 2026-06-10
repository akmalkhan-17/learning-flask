from dotenv import load_dotenv
import os

load_dotenv()

class Config: ##wrapping config into class is a good practise
		SECRET_KEY = os.getenv('SECRET_KEY','myDefaultSecretKey') ##if env variable is not set, it will use the default value
	
