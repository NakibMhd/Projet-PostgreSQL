# Projet 2 : 

## Installer et configurer un serveur MySQL :

`apt install apache2 mysql-server php7.0`


### Création de l'utilisateur :

`mysql -u root -p`

`CREATE USER 'appli_web'@'localhost' IDENTIFIED BY 'appli_web';`

`GRANT ALL PRIVILEGES ON * . * TO 'appli_web'@'localhost';`

`exit`


### Création de la base de données

`mysql -u appli_web -p`

`CREATE DATABASE appli_web;`

`exit` 


### Mise en place de l'outil phpMyAdmin :

`cd /usr/share`

`sudo wget https://files.phpmyadmin.net/phpMyAdmin/4.7.9/phpMyAdmin-4.7.9-all-languages.zip`

`sudo unzip phpMyAdmin-4.7.9-all-languages.zip`

`sudo mv phpMyAdmin-4.7.9-all-languages phpmyadmin`

`sudo chown -R www-data:www-data /usr/share/phpmyadmin`

`sudo chmod -R 755 /usr/share/phpmyadmin`


### Configuration d'Apache pour phpMyAdmin : 

`sudo nano /etc/apache2/conf-available/phpmyadmin.conf`

> <Directory "/usr/share/phpmyadmin">
>
>    Order Deny,Allow
>
>    Deny from all
>
>    Allow from all
>
> < /Directory>
>
>  Alias /phpmyadmin /usr/share/phpmyadmin
>
>  Alias /phpMyAdmin /usr/share/phpmyadmin

`sudo ln -s /usr/share/phpmyadmin/ /var/www/html/phpmyadmin`


`sudo nano /etc/php/7.0/cli/php.ini` pour décommenter la ligne `extension=php_mysqli.dll`

`sudo service apache2 reload`

[http://localhost/phpmyadmin]

Login : appli_web
Password : appli_web

(Si l'extension MySQLi est toujours manquante, faire `sudo apt-get install php-mysql`) et `sudo service apache2 reload` et réessayer).
