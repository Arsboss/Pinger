from flask import Flask
import subprocess
app = Flask(__name__)

@app.route('/')
def main():
    subprocess.call(['sh', './Ping.sh'])
    return '4-check ping, saved to out.txt'

@app.route('out.txt')
def show_output():
    with open('out.txt') as f:
        return f.read()
