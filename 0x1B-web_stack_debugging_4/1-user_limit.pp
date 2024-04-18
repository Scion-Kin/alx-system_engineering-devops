# When executed, the user "holberton" will be able to use the system better.
# The problem was the few read file permission assigned to this user

exec {'escalate':
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 10000/" /etc/security/limits.conf',
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 10000/" /etc/security/limits.conf',
  provider => shell,
}
