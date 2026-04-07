# shared/email_utils.py
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import streamlit as st


RECIPIENT_EMAIL = "wijdan.psyc@gmail.com"


def send_report_email(pdf_bytes: bytes, subject: str, body: str, filename: str) -> bool:
    """
    Send a PDF report via Gmail SMTP.
    Credentials are read from Streamlit secrets:
      [email]
      sender = "yourapp@gmail.com"
      password = "your_app_password"
    Returns True on success, False on failure.
    """
    try:
        sender = st.secrets["email"]["sender"]
        password = st.secrets["email"]["password"]
    except Exception:
        return False

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    # Attach PDF
    part = MIMEBase("application", "octet-stream")
    part.set_payload(pdf_bytes)
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f'attachment; filename="{filename}"')
    msg.attach(part)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, RECIPIENT_EMAIL, msg.as_string())
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False
