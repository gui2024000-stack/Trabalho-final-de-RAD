<?php
$conn = new mysqli("localhost","root","","forum");

if ($conn->connect_error) {
    die("Erro de conexão: " . $conn->connect_error);
}

if(isset($_POST['mensagem'])){

    $msg = $_POST['mensagem'];

    $stmt = $conn->prepare("INSERT INTO mensagens (mensagem) VALUES (?)");
    $stmt->bind_param("s", $msg);
    $stmt->execute();
}
?>

<form method="POST">
<input type="text" name="mensagem" placeholder="Digite sua mensagem">
<button type="submit">Enviar</button>
</form>

<hr>

<?php

$result = $conn->query("SELECT * FROM mensagens ORDER BY id DESC");

while($row = $result->fetch_assoc()){
 echo htmlspecialchars($row['mensagem']) . "<br>";
}

?>