<?php
$serverName = "DESKTOP-L9A4LJG\JOSU"; // Cambia esto a tu servidor
$connectionOptions = array(
    "Database" => "NUTRIWANKA",
    "Uid" => "jose", 
    "PWD" => "123"
);

// Conectar a la base de datos
$conn = sqlsrv_connect($serverName, $connectionOptions);

if ($conn === false) {
    die(print_r(sqlsrv_errors(), true));
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $NOMBRE = $_POST["NOMBRE"];
    $APELLIDO = $_POST["APELLIDO"];
    $DNI = $_POST["DNI"];
    $CONTRA = $_POST["CONTRA"];
    $CORREO = $_POST["CORREO"];
    $CIUDAD = $_POST["CIUDAD"];

    $sql = "INSERT INTO USUARIO (DNI_USUARIO, CONTRA, NOMBRE, APELLIDO, CORREO, CIUDAD) VALUES (?, ?, ?, ?, ?, ?)";
    $params = array($DNI, $CONTRA, $NOMBRE, $APELLIDO, $CORREO, $CIUDAD);

    $stmt = sqlsrv_query($conn, $sql, $params);

    if ($stmt === false) {
        die(print_r(sqlsrv_errors(), true));
    } else {
        // Redirigir a otra página después de la inserción exitosa
        header("Location: ../index.html");
        exit;
    }

    sqlsrv_free_stmt($stmt);
}

sqlsrv_close($conn);
?>
