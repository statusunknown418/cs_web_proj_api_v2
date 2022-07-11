# Api Repo
This contains the source code for the randomized theater - spectators simulator

## Stack
- Django 🤮
- Python

## Local dev

1. Clone the repo
2. run: 
```
$ brew install poetry # for macOS (if not installed before)
$ poetry install # will setup local development env
$ poetry run ./manage.py
$ poetry run ./manage.py runserver
```
3. Start playing with this rather simple api

## What's next

Something that could be upgraded is the persistance (aka DB) integration,
this is managed on the frontend side using localstorage.

I (Alvaro) would like to say that despite the benefits this stack may have,
it's not that nice to develop with it (at least for someone coming from web/mobile with JS/TS).

PD: Sorry python lovers
