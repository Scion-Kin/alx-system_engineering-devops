# Installs a Nginx server and sets custom HTTP header

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

exec { 'add_header':
  provider    => shell,
  command     => 'sudo sed -i "42i\	add_header X-Served-By $(hostname);" /etc/nginx/nginx.conf'
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}