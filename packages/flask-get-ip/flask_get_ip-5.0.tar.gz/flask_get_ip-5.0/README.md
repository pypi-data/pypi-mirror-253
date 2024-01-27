Securely getting the IP address of a Flask http request client

```python
from flask import Flask
from flask_get_ip import get_ip

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, " + get_ip()
```