from pyramid_mailer.message import Message

def send_email_to_member(request, user_id, body, subject = 'hello', sender = 'admin@fibo.com'):
	email = request.user.email
	message = Message(subject = subject,
						sender = sender,
						recipients = [email],
						body = body)
	request.mailer.send(message)

