# automated puppet fix for a php configuration error

exec { 'Fix wordpress site':
  command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
