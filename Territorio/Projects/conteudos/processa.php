<?php
date_default_timezone_set('America/Fortaleza');
$nome=filter_input(INPUT_POST,'nome',FILTER_SANITIZE_SPECIAL_CHARS);
$email=filter_input(INPUT_POST,'email',FILTER_SANITIZE_EMAIL);
$mensagem=filter_input(INPUT_POST,'mensagem',FILTER_SANITIZE_SPECIAL_CHARS);

$erros=[];

if(!$nome||mb_strlen($nome)<2){
    $erros[]="Nome inválido";
}
if(!$email||!filter_var($email,FILTER_VALIDATE_EMAIL)){
    $erros[]= "Email inválido";
}
if(!$mensagem|| mb_strlen($mensagem)<5){
    $erros[]= "Mensagem muito curta";
}
?>
<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <title>Resultado do Formulário</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <main class="conteudo">
            <section class="secao">
                <h1>Resultado do envio</h1>
                <?php if (!empty($erros)) : ?>
                    <p><strong>Ocorreram problemas:</strong></p>
                    <ul>
                        <?php foreach($erros as $e):?>
                            <li><?php echo htmlspecialchars($e,ENT_QUOTES,"UTF-8");?></li>
                            <?php endforeach;?>
                    </ul>
                    <p>\use o botão para voltar do navegador para corrigir e tentar novamente.</p>
                    <?php else: ?>
                        <p>Olá,<strong><?php echo htmlspecialchars($nome,ENT_QUOTES,'UTF-8');?></strong>.>
                        <p>Recebemos seu contato em <?php echo date('d/m/Y H:1');?></p>
                        <p>Resumo do que foi enviado</p>
                        <ul>
                            <li>E-mail:<?php echo htmlspecialchars($email,ENT_QUOTES,'UTF-');?></li>
                            <li>Mensagem:<?php echo nl2br(htmlspecialchars($mensagem,ENT_QUOTES,'UTF-8'));?></li>
                        </ul>
                        <p>Este é um teste inicial.Em aulas futuras poderemos salvar os dados em arquivo ou banco de dados.</p>
                        <p><a href="index.html">Voltar à página inicial</a></p>
                        <?php endif;?>
            </section>
        </main>
    </body>
</html>