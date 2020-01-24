<!DOCTYPE html>
<!-- Setting Cookie or incrementing cookie if it exists -->
<?php
if (!isset($_COOKIE['visitCount'])) $_COOKIE['visitCount'] = 0;
$visitCount = $_COOKIE['visitCount'] + 1;
setcookie('visitCount',$visitCount,time()+3600*24*365);
?>

<html>
    <head>
        <title> Lab 5 - Part I </title>
        <link rel="stylesheet" href="./css/style.css">
        <link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">
    </head>
    <body>
    <h1>Lab 5 - Part I</h1>
    <?php
    $x = $_POST['x'];
    $y = $_POST['y'];
    echo "<table>";
    for($i = 1; $i <= $x; $i++) {
        echo "<tr>";
        for($j = 1; $j <= $y; $j++) {
            $answer = $j * $i;
            echo "<td>$answer</td>";
        }
        echo "</tr>";
    }
    echo "</table>";
    ?>
    <br/>
    <?php
    if ($visitCount > 1) {
    echo("This is visit number $visitCount.");
    } else {
    echo('Welcome first timer!');
    }
    ?>
    </body>
</html>
