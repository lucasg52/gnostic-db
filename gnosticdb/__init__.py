"""
The gnostic database server

flagz:
-p <port>
    Provide a port (default is 8000)
--debug
    Enable flask debug mode
"""
import sys
from .server.gnosticserver import app


def main(args):
    port = 8000
    argiter = iter(args)
    for arg in argiter:
        if arg == "-p":
            try:
                port = next(argiter)
            except StopIteration:
                print("-p was not followed by a valid argument", file=sys.stderr)
                pass
    try:
        port = int(port)
    except ValueError:
        print("-p was provided an invalid argument", file=sys.stderr)
        port = 8000
    app.run(debug = bool("--debug" in args), port=port, use_reloader=False)

