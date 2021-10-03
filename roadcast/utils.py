from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail.message import EmailMessage
import six
import threading

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, public, timestamp):
        return six.text_type(public.pk)+six.text_type(timestamp)+six.text_type(public.is_email_verified)

generate_token = TokenGenerator()

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list,sender):
        self.subject=subject
        self.recipient_list=recipient_list
        self.html_content = html_content
        self.sender = sender
        threading.Thread.__init__(self)
    
    def run(self):
        msg = EmailMessage(self.subject, self.html_content,
            self.sender, self.recipient_list)
        msg.send()

def send_html_mail(subject, html_content, recipient_list, sender):
    EmailThread(subject, html_content, recipient_list, sender).start()