# modifying client's ssh config file

file_line {'diable pass auth'
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '   PasswordAuthentication no',
  replace => true,
}

file_line { 'identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '   IdentityFile ~/.ssh/school',
  replace => true,
}
