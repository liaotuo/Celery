from .celery import app

@app.task
def leijun():
	print('Are you OK !!!')
