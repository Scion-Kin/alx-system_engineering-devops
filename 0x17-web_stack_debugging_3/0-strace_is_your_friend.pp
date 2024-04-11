# automated puppet fix for a php configuration error

exec { 'Fix wordpress site':
  require  => shell,
  command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php'
}
