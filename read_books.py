import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]


def main():
    client = create_client(SUPABASE_URL, SUPABASE_KEY)
    response = client.table("books").select("*").execute()

    for book in response.data:
        status = "read" if book["read"] else "unread"
        print(f'{book["title"]} by {book["author"]} ({status})')


if __name__ == "__main__":
    main()
