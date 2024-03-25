 from models import Dog

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).all()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).all()

def update_breed(session, dog, breed):
    try:
        dog.breed = breed
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error updating breed: {str(e)}")
































































        



# def create_table(base):
#     pass

# def save(session, dog):
#     pass

# def get_all(session):
#     pass

# def find_by_name(session, name):
#     pass

# def find_by_id(session, id):
#     pass

# def find_by_name_and_breed(session, name, breed):
#     pass

# def update_breed(session, dog, breed):
#     pass