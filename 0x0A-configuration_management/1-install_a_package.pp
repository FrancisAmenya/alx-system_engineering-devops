#Installs puppet

package { 'python3-pip':
  ensure => installed,
}

# Install Flask 2.1.0 using pip
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  unless  => '/usr/bin/pip3 show Flask | grep 2.1.0',
  require => Package['python3-pip'],
}
