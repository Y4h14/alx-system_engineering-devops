# install and configure nginx

package {'nginx'
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx',
  provider => shell,
}

exec {'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html''
  provider => 'shell',
}

exec {'run':
  command  => 'sudo sed -i 's/listen 80 default_server;/listen 81;/g' /etc/nginx/sites-available/default',
  provider => shell',
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
