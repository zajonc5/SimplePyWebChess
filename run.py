from app import create_app

app = create_app(False)
app.run('0.0.0.0')
