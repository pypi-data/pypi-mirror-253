import typer
from pydurable.login import login
from pydurable.apikey import app as apikey
from pydurable.aws import app as aws


LOGIN_PORT = 54987
CLIENT_ID = '685954567384-9otb323plmau5iutge14kb4l7aei889n.apps.googleusercontent.com'
API = 'http://localhost:8000'


app = typer.Typer()
app.command()(login)
app.add_typer(apikey, name='keys')
app.add_typer(aws, name='aws')


def main():
    app()
    

if __name__ == '__main__':
    app()
