#Filename: 2-execute_a_command.pp

exec { 'killmenouw':
    command => 'pkill -f killmenow',
    onlyif  => 'pgrep -f killmenow',
}
