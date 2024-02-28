# Configure nginx server

exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update'],
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
        listen  80 default_server;
        listen  [::]:80 default_server;
        root    /var/www/html;
        index   index.html;

        location /redirect_me {
        return 301 http://googl.com;
        }
        error_page 404 /404.html;
        location /404 {
        root /var/www/html;
        internal;
        }",
  notify  => Service['nginx'],
}

