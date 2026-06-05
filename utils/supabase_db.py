from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# --------------------

def insert_candidate(candidate):

    supabase.table(
        "candidates"
    ).insert(
        candidate
    ).execute()

# --------------------

def get_all_candidates():

    response = supabase.table(
        "candidates"
    ).select("*").execute()

    return response.data

# --------------------

def get_user_candidates(email):

    response = (
        supabase.table("candidates")
        .select("*")
        .eq("user_email", email)
        .execute()
    )

    return response.data