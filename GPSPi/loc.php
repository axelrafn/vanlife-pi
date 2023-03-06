<?php
$servername = "localhost";
$db_user = '';
$db_pass = '';
$db_name = "";

$conn = new mysqli($servername, $db_user, $db_pass, $db_name);

function sanitize($str) {
    $str = strtolower($str);
    $str = stripslashes($str);
    $str = htmlspecialchars($str);
    return $str;
}

if ($conn->connect_error) {
  die("Inital connection failed!" . $conn->connect_error);
}

if(isset($_GET['lat']) && isset($_GET['lon'])){
  $dags = new Datetime();
  $sql = "INSERT INTO location (dags, lat, lon) VALUES ('".$dags->format('U')."', '".sanitize($_GET['lat'])."', '".sanitize($_GET['lon'])."')";
  $result = $conn->query($sql);
}
?>