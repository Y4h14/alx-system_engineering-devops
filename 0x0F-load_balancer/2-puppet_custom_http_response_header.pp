# automating creating a custom HTTP header

exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
}

file { '/var/www/htmlindex.html':
  ensure  => file,
  content => 'Hello World!',
  require => package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
        listen  80 default_server;
        listen  [::]:80 default_server;
        root    /var/www/html;
        index   index.html;

        # Add custom header
        add_header X-Served-By \$hostname;

        location /redirect_me {
        return 301 http://googl.com;
        }
        error_page 404 /404.html;
        location /404 {
        root /var/www/html;
        internal;",
  notify  => Service['nginx'],
    
service { 'nginx':
  ensure     => running,
  enable     => true,
}
