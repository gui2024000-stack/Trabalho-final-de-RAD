<?php
include 'conexao.php';

$mensagem = ""; // inicia vazio

// Processa o formulário apenas se houver POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nome = $_POST['nome'];
    $email = $_POST['email'];
    $senha = $_POST['senha'];

    $sql = "INSERT INTO cadastro (nome, email, senha) VALUES ('$nome', '$email', '$senha')";

    if ($conn->query($sql) === TRUE) {
        $mensagem = "Usuário cadastrado!";
    } else {
        $mensagem = "Erro: " . $conn->error;
    }
} else {
    $mensagem = "Conectado com sucesso!";
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Cadastro de Usuário</title>
    <link rel="stylesheet" href="styleCad.css">z
</head>
<body>
<h1>Cadastro de usúario</h1>
<form method="POST" action="">
    Nome: <input type="text" name="nome" required><br>
    Email: <input type="email" name="email" required><br>
    
    Senha: 
    <div style="display:flex;">
        <input type="password" id="senha" name="senha" required style="flex:1;">
        <button type="button" onclick="mostrarSenha()">👁️</button>
    </div><br>

    <button type="submit">Cadastrar</button>
</form>

<?php if (!empty($mensagem)) echo "<div class='mensagem-rodape'>$mensagem</div>"; ?>

<script>
function mostrarSenha() {
    var campo = document.getElementById("senha");
    var botao = event.currentTarget;

    if (campo.type === "password") {
        campo.type = "text";
        botao.textContent = "🙈";
    } else {
        campo.type = "password";
        botao.textContent = "👁️";
    }
}
</script>

</body>
</html>