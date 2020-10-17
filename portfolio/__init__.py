from flask import Flask

app = Flask(__name__)

import portfolio.views
import portfolio.post_bot


