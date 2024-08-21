#Install Nginx web server (w/ Puppet)


exec { 'Install':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx && echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html && sudo sed -i "/^\sserver_name.*/a \        rewrite ^/redirect_me https://jvstblvck.com permanent;" /etc/nginx/sites-available/default && sudo service nginx start',
  provider => shell,
}
