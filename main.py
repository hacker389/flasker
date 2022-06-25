from django.shortcuts import redirect
from flask import Flask, render_template, make_response, session, redirect, request
from werkzeug.exceptions import abort

from date import db_session
from config import app


def main():
    db_session.global_init("db/blogs.db")
    app.run()

if __name__ == '__main__':
    main()
