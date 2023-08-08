# import Flask, sys, and subprocess

import sys
from flask import render_template, Flask, request
import subprocess
import os

myip = subprocess.check_output(['ipconfig', 'getifaddr', 'en0'])
myip = myip.decode('utf-8').strip()

if sys.argv[1] is None:
	print('''Usage: python3 receiver.py <port number>
Example: python3 receiver.py 9999''')

# Initialize Flask

app = Flask(__name__)

# Homepage

@app.route('/')
def homepage():
	return render_template('receiver.html', myip=myip), 200

# Download function

@app.route('/downloads', methods=['POST'])
def downloads():
	if request.method == "POST":
		f = request.files['file']
		print(f"[+] {f.filename} Received from {request.remote_addr}!")
		if (f.filename != ""):
			print(f"[+] Saving {f.filename}...")
			f.save(f.filename)
			print("[+] Done!")
			return render_template('r1.html')

# Run app

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=sys.argv[1])