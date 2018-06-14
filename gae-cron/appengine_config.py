import os
import google
import imp
import inspect

from google.appengine.ext import vendor

# Add any libraries install in the "lib" folder.
vendor.add('lib')

# whitelists the socket and ssl libraries for the dev app server, and uses the system-level socket library instead of the one packaged with the App Engine SDK. Your mileage may vary.    
if os.environ.get('SERVER_SOFTWARE', '').startswith('Development'):
    from google.appengine.tools.devappserver2.python import sandbox
    sandbox._WHITE_LIST_C_MODULES += ['_ssl', '_socket']

    runtime_path = os.path.realpath(inspect.getsourcefile(inspect))
    runtime_dir = os.path.dirname(runtime_path)

    # Patch and reload the socket module implementation.
    system_socket = os.path.join(runtime_dir, 'socket.py')
    imp.load_source('socket', system_socket)

    # Patch and reload the ssl module implementation.
    system_ssl = os.path.join(runtime_dir, 'ssl.py')
    imp.load_source('ssl', system_ssl)