# os config update  
exec { 'increase_holberton_hard_limit':
  command  => 'sed -i "/holberton hard/s/5/2000/" /etc/security/limits.conf',
  provider => 'shell'
}

exec { 'increase_holberton_soft_limit':
  command  => 'sed -i "/holberton soft/s/4/2048/" /etc/security/limits.conf',
  provider => 'shell'
}
