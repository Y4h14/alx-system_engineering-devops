# updating traffic ulimit
 
exec { 'ulimit-update':
  command  => 'sed -i "s/15/2001/" /etc/default/nginx',
  provider => 'shell',
  notify   => Exec['nginx-restart']
}

# Restart Nginx
exec { 'nginx-restart':
  command => 'sudo service nginx restart',
  provider    => 'shell',
}
