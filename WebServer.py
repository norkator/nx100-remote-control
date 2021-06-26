"""
This is simple web server demo
"""

from nx100_remote_control.module import WebServer


def start_app():
    WebServer.run(addr="localhost", port=8080)  # 0.0.0.0 (available from host ip)


start_app()
