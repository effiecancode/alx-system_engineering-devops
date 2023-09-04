# Automation: creates a custom HTTP header response with Puppet.

exec { 'configure_custom_header':
  command     => 'apt-get -y update && apt-get -y install nginx',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
  require     => Package['nginx'],
  provider    => shell,
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('my_module/nginx_default.erb'),
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => 'service nginx restart',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
  require     => Package['nginx'],
  provider    => shell,
}

