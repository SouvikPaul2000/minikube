from src import app
from src.models import db, post_schema,posts_schema
import os
        
if __name__ == '__main__':
    
    app.run(host ="0.0.0.0" ,debug=True)
      
