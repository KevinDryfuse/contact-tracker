from flask_web.models import User
from werkzeug.security import check_password_hash

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed password, first name, and last name fields are defined correctly
    """
    email = 'email@domain.com'
    plaintext_password = 'ThisIsAPassword'
    first_name = 'Kevin'
    last_name = 'Dryfuse'

    user = User(email=email,
                plaintext_password=plaintext_password,
                first_name=first_name,
                last_name=last_name)

    assert user.email == email
    assert user.password_hash != plaintext_password
    assert check_password_hash(user.password_hash, plaintext_password)
    assert user.last_name == last_name
    assert user.last_name == last_name
