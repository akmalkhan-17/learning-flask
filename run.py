from app import create_app
from app.extensions import db
from app.models import User

app = create_app()

with app.app_context():
    # db.create_all() need to remove after the database is created, otherwise it will throw an error because the table already exists

    # User.query.delete()
    # db.session.commit()

    print(
        db.metadata.tables.keys()
    )  # this will print the names of all the tables in the database, if you see users in the list, then it means that the table was created successfully

if __name__ == "__main__":
    app.run(debug=True)
