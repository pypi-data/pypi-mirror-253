"""Flask api to execute various Arya jobs/candidates services"""

from apiroutes import create_app

app = create_app()
app.run('0.0.0.0', port=1501)