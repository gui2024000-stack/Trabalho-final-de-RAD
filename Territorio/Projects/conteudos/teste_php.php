<?php
date_default_timezone_set('America/Fortaleza');
$agora=date('d/m/Y H:1');
?>
<!DOCTYPE html>
<html lang="pt-BR"></html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial scale=1">
    <title>Teste do PHP</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <main class="conteudo">
        <section class="secao">
            <h1>PHP em funcionamento</h1>
            <p>Se você está vendo a página renderizada, o PHP está configurado corretamente.</p>
            <p>Data e hora do servidor:<strong><?php echo $agora;?></strong></p>
            <p><a href="index.html">Abrir página inicial</a></p>
            <p><a href="#" onclick="location.href='teste_php.php?phpinfo=1';return false;">Exibir informações do PHP</a></p>
            <?php
            if(isset($_GET['phpinfo'])){
                phpinfo();
            }
            ?>
        </section>
    </main>
</body>