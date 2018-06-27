from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
	Debug = True,
	MAIL_SERVER = 'smtp.googlemail.com',
	MAIL_PORT = 587,
	MAIL_USE_TLS = 1,
	MAIL_USERNAME = 'ajayaravindh55@gmail.com',
	MAIL_PASSWORD = 'gsav*2705'
)

@app.route('/', methods = ['GET', 'POST'])
def index():
	if(request.method == "POST"):
		mail = Mail(app)
		sender = request.form.get("name")
		sender_mail = request.form.get("mail")
		msg = request.form.get("message")

		mesg = Message("Portfolio website: " + sender + " from " + sender_mail, sender = sender_mail, recipients = ['ajcodes55@gmail.com'])
		mesg.body = msg
		mail.send(mesg)
		return "Mail Sent Successfully. <a href = '/'>Go Back</a>"
	else:
		return render_template('index.html')