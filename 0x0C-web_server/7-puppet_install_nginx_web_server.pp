# Install and configure Nginx

package { 'nginx':
  ensure => 'present',
}

exec { 'install':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx',
  provider => 'shell',
  require  => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  require => Exec['install'],
}

exec { 'configure':
  command  => 'sudo sed -i "s/listen 80 default_server;/listen 81;/g" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => File['/var/www/html/index.html'],
}

exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => 'shell',
  require  => Exec['configure'],
}

