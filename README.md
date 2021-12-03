# autobattlebot

## installing dependencies
this project uses pipenv to manage dependencies.  
install it using the instructions at https://pypi.org/project/pipenv/, then use `pipenv install` to install dependencies, and `pipenv shell` to enter the virtualenv
 

## setting up the db
we're using [dbmate](https://github.com/amacneil/dbmate) for managing the database

first, install it, add the url of the database to the .env, ie  
`DATABASE_URL="postgres://<user>:<password>@<url>:<port>/<db name>?sslmode=disable"`

then, to migrate the db to the current schema, run `dbmate up`

