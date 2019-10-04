<?php

if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'eve', 'password');
    mysqli_select_db($link, 'Target');
    
    $query = "SELECT * from Users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $results = mysqli_query($link, $query) or die(mysqli_error($link));

    if(mysqli_num_rows($results) > 0) {
        echo "Successful login!<br>";
    } else {
        echo "Access denied!<br>";
    }
    
    mysqli_close($link);
}

?> 
