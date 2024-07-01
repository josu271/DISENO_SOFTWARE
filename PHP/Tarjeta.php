<?php
$serverName = "DESKTOP-L9A4LJG\JOSU"; 
$connectionOptions = array(
    "Database" => "NUTRIWANKA",
    "Uid" => "jose", 
    "PWD" => "123"
);


$conn = sqlsrv_connect($serverName, $connectionOptions);

if ($conn === false) {
    die(print_r(sqlsrv_errors(), true));
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $NOMBRE = $_POST["Nombre"];
    $APELLIDO = $_POST["Apellido"];
    $NUM_TARJETA = $_POST["Num_tarjeta"];
    $MM_AA = $_POST["MM_AA"];
    $CORREO = $_POST["Correo"];

    $sql = "INSERT INTO Tarjeta (Num_tarjeta, Nombre, Apellido, MM_AA, Correo) VALUES (?, ?, ?, ?, ?)";
    $params = array($NUM_TARJETA, $NOMBRE, $APELLIDO, $MM_AA, $CORREO);

    $stmt = sqlsrv_query($conn, $sql, $params);

    if ($stmt === false) {
        die(print_r(sqlsrv_errors(), true));
    } else {

        header("Location: ../index.html");
        exit;
    }

    sqlsrv_free_stmt($stmt);
}

sqlsrv_close($conn);
?>
