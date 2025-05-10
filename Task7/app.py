from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)

@app.route('/set/<key>/<value>')
def set_value(key, value):
    r.set(key, value)
    return f"Set {key} = {value}"

@app.route('/get/<key>')
def get_value(key):
    value = r.get(key)
    return f"{key} = {value.decode() if value else 'None'}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)