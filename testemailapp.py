import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

# Streamlit app layout
st.title('SMTP Email Sender')

# Input fields
smtp_server = st.text_input('SMTP Server', value='mx.make-contact.com')
smtp_port = st.number_input('SMTP Port', value=587)
smtp_user = st.text_input('SMTP User')
smtp_password = st.text_input('SMTP Password', type='password')
from_email = smtp_user
to_email = st.text_input('To Email', value='justin@sendengage.io')
subject = st.text_input('Subject', value='Test Email from Python')
body = st.text_area('Body', value='This is a test email sent from a Python script.')

# Send email button
if st.button('Send Email'):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Comment this out if your server doesn't use TLS
        server.login(smtp_user, smtp_password)
        text = message.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        st.success("Email sent successfully!")
    except Exception as e:
        st.error(f"Failed to send email: {e}")
