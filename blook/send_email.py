

# need to pip install sendgrid 


from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='julianooi80@gmail.com',
    to_emails='mrjulianooii@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient("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")
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)