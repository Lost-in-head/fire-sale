from db import get_connection
from send_email import send_email

def process_leads():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, email FROM leads WHERE status = 'new'")
    leads = cursor.fetchall()

    for lead in leads:
        lead_id, email = lead

        send_email(
            email,
            "Quick question",
            "Hey — I help agencies get more clients. Worth a quick chat?"
        )

        cursor.execute(
            "UPDATE leads SET status = 'contacted' WHERE id = ?",
            (lead_id,)
        )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    process_leads()
  
