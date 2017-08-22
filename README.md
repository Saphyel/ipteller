# IP teller

## Intro
This app saves your public IP and send a report when is different.

By default generates a cron job that checks every hour your public IP against the page jsonip if is different will send you an email with the new IP.

## Config
You need to add your gmail details as environment variables using `GMAIL_USER` and `GMAIL_PASS` (check the docker-compose.yml). The account that you specify will be the sender and receiver of the email.

## Future plan
- Integrate more providers of your public IP address.
- Integrate more deliveries of your new IP address.
- Integrate more places where to store your actual IP address.
