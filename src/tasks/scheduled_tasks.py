from src.tasks import app
from src.services.slack_integration import SlackPost
from main import main


# Here we could send emails for example
@app.task(name='task.ping')
def send_email_task():
    print('pong')
    return 'ping pong'


@app.task(name='task.print_on_terminal')
def task_with_params(a, b):
    print('It Works!, {} - {}'.format(a, b))
    return 'Print working fine...'


@app.task(name='task.check_db')
def check_db_health():
    try:
        main()
        slack = SlackPost()
        slack.send_message()
        return 'DBs are okay...'
    except Exception as ex:
        return 'Not Good: {}'.format(str(ex))
