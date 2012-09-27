from celery import task
from django.core.mail import send_mail

@task()
def send_email(to_email, from_email, subject, message, send_cc):

    recipients = [to_email]

    if send_cc:
        recipients.append(from_email)

    print to_email, from_email, subject, message, send_cc

    send_mail(subject, message, from_email, recipients)