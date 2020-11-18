import pytest
import json
from flask import Flask, Response, redirect, url_for, request, jsonify, render_template

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


if __name__ == '__main__':
    app.run(debug=True, port=8000)