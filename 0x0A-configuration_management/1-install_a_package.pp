# install flask from pip3

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  creates => '/usr/local/lib/python3.10/dist-packages/Flask',
  path    => '/usr/bin',
}
