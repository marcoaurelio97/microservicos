import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to, text):
    me = "testeemailfacens@gmail.com"
    you = to

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = me
    msg['To'] = you

    html = """\
    <html>
      <head></head>
      <body>
        <p>
            {}
        </p>
      </body>
    </html>
    """.format(text)

    part = MIMEText(html, 'html')

    msg.attach(part)

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("testeemailfacens@gmail.com", "segredo123")
    s.sendmail(me, you, msg.as_string())
    s.quit()
