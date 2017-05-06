from flask import Flask, render_template, redirect, url_for, flash
import optparse
from worker import task

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Set your own key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    task.delay("World.")
    flash(u"Add job queue!!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    default_host = 'localhost'
    default_port = 5000

    parser = optparse.OptionParser()
    parser.add_option("-H", "--host",
                      help="Hostname of the Flask app " + \
                           "[default {0}]".format(default_host),
                      default=default_host)
    parser.add_option("-P", "--port",
                      help="Port for the Flask app " + \
                           "[default {0}]".format(default_port),
                      default=default_port)
    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug",
                      help=optparse.SUPPRESS_HELP)
    options, _ = parser.parse_args()
    app.debug = True
    app.run(debug=options.debug,
            host=options.host,
            port=int(options.port))
