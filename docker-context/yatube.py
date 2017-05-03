#!/usr/bin/python3.6

from sanic import Sanic
from sanic.response import json
from sanic.response import html

app = Sanic()

@app.route("/")
async def root(request):
    return json({"hello": "world"})

@app.route("/register")
async def register(request):
    return json({"hello": "world"})

@app.route("/login")
async def login(request):
    return json({"hello": "world"})

@app.route("/favicon.ico")
async def favicon(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
