# 'Holborn Racquets Club' Flask Website

An experimental Flask website for a fictional 'Holborn Racquets Clubs', for learning Flask and Python. 

The set-up of this site is based on the [Discover Flask](https://github.com/realpython/discover-flask) tutorial. 

Key features: 
- User Authentication
- Connection to SQLite database
- Bootstrap design
- Unit testing
- Write access to database (enter squash match scores)

## Notes

Deviating from the Heroku deployment set-up, `waitress` is used instead of the `gunicorn` module due to cross-platform limitations. The code used instead was:

```
waitress-serve --listen=127.0.0.1:4000 app:app
```
