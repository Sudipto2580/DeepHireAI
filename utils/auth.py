from utils.supabase_db import supabase
import hashlib

from utils.supabase_db import supabase
import hashlib

def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()

def signup(
    fullname,
    username,
    email,
    password,
    phone,
    linkedin,
    github,
    portfolio,
    twitter,
    instagram
):

    try:

        data = {

            "fullname": fullname,
            "username": username,
            "email": email,
            "password": hash_password(password),
            "phone": phone,
            "linkedin": linkedin,
            "github": github,
            "portfolio": portfolio,
            "twitter": twitter,
            "instagram": instagram,
            "theme": "Dark"

        }

        supabase.table(
            "users"
        ).insert(
            data
        ).execute()

        return True

    except Exception as e:

        print(e)

        return False
    
def login(
    email,
    password
):

    response = supabase.table(
        "users"
    ).select(
        "*"
    ).eq(
        "email",
        email
    ).eq(
        "password",
        hash_password(password)
    ).execute()

    if response.data:

        return response.data[0]

    return None

def get_user(email):

    response = supabase.table(
        "users"
    ).select(
        "*"
    ).eq(
        "email",
        email
    ).execute()

    if response.data:

        return response.data[0]

    return None


