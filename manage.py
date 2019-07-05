from personal_okrs import db, create_app
from personal_okrs.data_model import *

app = create_app()

db.drop_all(app=app)
db.create_all(app=app)