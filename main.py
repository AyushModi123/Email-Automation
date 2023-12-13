import ssl
import time
from email.message import EmailMessage
import smtplib
import pandas as pd

CSV_PATH = "" #Full path of csv file

df = pd.read_csv(CSV_PATH, usecols=['Email', 'Company Name', "Recruiter's Name"])
df = df.dropna()

company_names = list(df['Company Name'])
company_mails = list(df['Email'])
recruiter_names = list(df["Recruiter's Name"])
sender_name = "" # Your Name

smtp_server = 'smtp.gmail.com'
smtp_port = 465
sender_email = '' #Your Email
sender_password = ''  # App password
subject = 'Software Developer Eager To Join Your Team'

context = ssl.create_default_context()
server = smtplib.SMTP_SSL(smtp_server, smtp_port, context=context)
server.login(sender_email, sender_password)


for recruiter_name, company_name, company_mail in zip(recruiter_names, company_names, company_mails):
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["Subject"] = subject
    message = f"""
Dear {recruiter_name},

I hope this email finds you well. My name is {sender_name}, and I am writing to express my interest in the Software Position at {company_name}, as advertised on your website. With a strong background in software development and a passion for creating innovative solutions, I believe I can contribute effectively to your team.

In my previous role at [], I successfully designed and implemented [specific projects or applications] that resulted in [quantifiable achievements or improvements]. My skills include proficiency in [relevant programming languages}, experience with [specific technologies or tools], and a solid understanding of [relevant industry trends or best practices].

I am particularly drawn to {company_name} because of its reputation for [mention a specific aspect of the company that appeals to you, such as cutting-edge technology, commitment to innovation, or a positive company culture]. I am confident that my technical skills, coupled with my ability to work collaboratively and adapt to new challenges, align well with the values and goals of {company_name}.

Enclosed is my resume that provides additional details about my professional experience and skills. I would welcome the opportunity to further discuss how my background and expertise can contribute to the success of your team during an interview.

Thank you for considering my application. I look forward to the possibility of discussing how my skills and experiences align with the needs of {company_name}.

Best regards,

{sender_name}
[Contact Details]"""
    msg["To"] = [str(st) for st in company_mail.split(' ') if st]
    msg.set_content(message)
    try:
        server.send_message(msg)
        print(f'Mail sent to {company_mail}')
    except Exception as e:
        print(f'An error occurred while sending email to {company_mail}:', e)
        break
    del msg
    time.sleep(5)    


server.quit()
