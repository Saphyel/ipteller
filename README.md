# IP teller

## Intro
This app saves your public IP and send a report when is different.

By default generates a cron job that checks every hour your public IP against the page jsonip if is different will send you an email with the new IP.

## Config
You need to add your gmail details as environment variables using `GMAIL_USER` and `GMAIL_PASS` (check the docker-compose.yml). The account that you specify will be the sender and receiver of the email.

## Dev
Execute: `pip install --user -r dev-requirements.txt`

### Publish your package
Execute: `python setup.py sdist;twine upload dist/*`

### Run tests
Execute: `behave`
