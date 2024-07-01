<?php
// Configuración de la conexión
$serverName = "DESKTOP-L9A4LJG\JOSU"; // Puede ser "localhost" si el servidor SQL Server está en la misma máquina
$connectionOptions = array(
    "Database" => "nutriwanka",
    "Uid" => "jose",
    "PWD" => "123"
);

// Conectando a la base de datos
$conn = sqlsrv_connect($serverName, $connectionOptions);

// Verificar la conexión
if ($conn) {
    echo "Conexión establecida.";
} else {
    echo "Conexión no se pudo establecer.<br>";
    die(print_r(sqlsrv_errors(), true));
}
?>