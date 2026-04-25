from db import get_connection

def add_lead(name, email, business):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO leads (name, email, business_name)
    VALUES (?, ?, ?)
    """, (name, email, business))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_lead("Test User", "test@email.com", "Test Agency")
    print("Lead added.")
