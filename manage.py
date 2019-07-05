from personal_okrs import db, create_app

create_app()

db.drop_all()
db.create_all()