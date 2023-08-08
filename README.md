# Receiver

An easy file sharer using a web server.

# Installation and quick start

`git clone https://github.com/Codeiology/Receiver.git`

`cd Receiver`

`python3 receiver.py`

* Only tested on macOS.

# Usage

At the end of the output for `python3 receiver.py`, there should be something like:


`[*] running on http://127.0.0.1:5000`

`[*] running on http://192.168.0.5:5000`


In this case, other devices on the same network can navigate to `http://192.168.0.5:5000` in a browser. From there, it should be easy.
Once you send a file via the webserver, it should appear in the Receiver directory. You can move it wherever you want.
