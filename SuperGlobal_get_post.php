<?php
//
//$username = "EMPTY";
//$pass = "EMPTY";
//
//if( isset($_GET['username']) && isset($_GET['password']) ){
//    $username = $_GET['username'];
//    $password = $_GET['password'];
//    $pass = "****";
//}
//
//echo "username = $username password = $pass";
//?>
<!---->
<!--<html>-->
<!--    <head>-->
<!---->
<!--    </head>-->
<!--    <body>-->
<!--        <form action="/SuperGlobal_get_post.php" method="get"> <!--get به طور پیش فرض قرار داده میشود پس لازم به تکرار آن نیست-->-->
<!--            <label>username: </label>-->
<!--            <input type="text" name="username">-->
<!--            <label>password: </label>-->
<!--            <input type="text" name="password">-->
<!--            <button type="submit">send</button>-->
<!--        </form>-->
<!--    </body>-->
<!--</html>-->

<?php

$username = "EMPTY";
$pass = "EMPTY";

if( isset($_POST['username']) && isset($_POST['password']) ){
    $username = $_POST['username'];
    $password = $_POST['password'];
    $pass = "****";
}

echo "username = $username password = $pass";
?>

<html>
<head>

</head>
<body>
<form action="/SuperGlobal_get_post.php" method="post">
    <label>username: </label>
    <input type="text" name="username">
    <label>password: </label>
    <input type="text" name="password">
    <button type="submit">send</button>
</form>
</body>
</html>