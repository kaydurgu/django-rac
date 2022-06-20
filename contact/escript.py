import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail:
    
    def __init__(self) -> None:
    
        self.site_mail = "kaydurgu@outlook.com"
        self.password = "Zhanbolot12345"
        self.me = 'kaydurgu@gmail.com'

    def send(self, sender_name, sender_email, text):
        
        message = MIMEMultipart('alternative')
        
        message['Subject'] = sender_name + 'Отправил вам письмо'
        message['From'] = self.site_mail
        message['To'] = self.me

        template_html = f"""\
            <html>
                <head></head>
                    <body>
                        <p><b>{sender_name}</b> отправил вам письмо <br><br>
                            {text}  <br><br>
                            ответить {sender_email}
                        </p>
                    </body>
            </html>
        """
        base = MIMEText(template_html, 'html')
        message.attach(base)

        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(self.site_mail, self.password)
            server.sendmail(self.site_mail, self.me, message.as_string())

