from django.core.mail import send_mail
from django.conf import settings

def send_email_to_anyone():
    subject = 'Email from Django server'
    message = 'gooners squad'
    from_email = settings.EMAIL_HOST_USER
    recipients = ['co23334@ccet.ac.in','co23363@ccet.ac.in', 'co23318@ccet.ac.in', 'co23322@ccet.ac.in']

    send_mail(subject, message, from_email, recipients)