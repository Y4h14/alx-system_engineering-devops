# create a manifest that kills a process named killmenow

exec { 'killmenouw':
    command => 'pkill -f killmenow'
}
