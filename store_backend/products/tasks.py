from conf.celery import app
from conf.settings import SECRET_KEY


@app.task
def send_spam_email(user_email):
    print(f'Сообщение на почту: {user_email}')


@app.task
def send_spam_every_5_second():
    print('Это работает @app.task ------ send_spam_every_5_second')
    print(f'SECRET_KEY ==== {SECRET_KEY}')
