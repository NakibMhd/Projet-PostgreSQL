`apt-get install postgressql postgressql-client`

`sudo -s -u postgres`

`createuser -d -P appli_web`

`createdb -O appli_web appli_web`

`exit` 

`psql -U appli_web -h localhost appli_web`
