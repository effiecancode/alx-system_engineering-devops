# Fix apache2 web server by editing wp-settings.php
# Actually fix a typo in th file

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin/'
}
