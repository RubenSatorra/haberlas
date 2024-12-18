<?php
    //Configuración del correo
    $to = 'reciomatamoros13@gmail.com'; // Reemplaza con tu correo electrónico
    $from = 'kitaroto05@gmail.co'; // Reemplaza con una dirección que controlas

    // Validación y sanitización de datos (¡ESENCIAL!)
    if (!isset($_POST["fname"], $_POST["email"], $_POST["message"], $_POST["phone"])) {
        die("Error: Faltan datos del formulario.");
    }

    $firstname = filter_var($_POST["fname"], FILTER_SANITIZE_STRING);
    $email = filter_var($_POST["email"], FILTER_SANITIZE_EMAIL);
    $phone = filter_var($_POST["phone"], FILTER_SANITIZE_STRING);
    $text = filter_var($_POST["message"], FILTER_SANITIZE_STRING);


    //Protección CSRF (implementa un sistema de tokens CSRF aquí.  Es crucial para la seguridad!)
    // ...  (Código para manejo de tokens CSRF) ...


    //Construcción del mensaje
    $headers = 'MIME-Version: 1.0' . "\r\n";
    $headers .= "From: " . $from . "\r\n"; // Usa tu correo como remitente
    $headers .= 'Content-type: text/html; charset=utf-8' . "\r\n"; // Usa UTF-8

    $message = '<table style="width:100%">
        <tr>
            <td>' . htmlspecialchars($firstname) . '</td>
        </tr>
        <tr><td>Email: ' . htmlspecialchars($email) . '</td></tr>
        <tr><td>Teléfono: ' . htmlspecialchars($phone) . '</td></tr>
        <tr><td>Mensaje: ' . nl2br(htmlspecialchars($text)) . '</td></tr>
    </table>';

    // Envío del correo y manejo de errores
    if (mail($to, 'Nuevo Mensaje desde tu sitio web', $message, $headers)) {
        echo 'El mensaje se ha enviado correctamente.';
    } else {
        echo 'Error al enviar el mensaje. Por favor, intenta de nuevo más tarde.';
        // En un entorno de producción, registra el error para depuración.
    }

?>