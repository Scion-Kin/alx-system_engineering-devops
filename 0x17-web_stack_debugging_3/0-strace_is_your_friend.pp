# automated puppet fix (to find out why Apache is returning a 500 error)

exec { 'Fix wordpress site':
  require  => shell,
  command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php'
}
