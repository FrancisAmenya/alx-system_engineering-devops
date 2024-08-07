#Installs puppet
package { 'python3-pip':
  ensure => installed,
}

# Install Flask 2.1.0 using pip
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
