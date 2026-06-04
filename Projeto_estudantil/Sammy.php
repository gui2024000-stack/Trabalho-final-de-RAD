<!DOCTYPE html>
<html lang="pt-Br">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Meu primeiro site HTML</title>
    <link rel = "stylesheet" href = "styles.css">
  </head>
  <body>
    <header>
      <h1>Seja bem vindo ao Sammy!</h1>
      <p>aprenda com estudantes de todo o país</p>
    </header>
    <nav>
        <a href="cadastro.php">cadastro</a>
        <a href="ajuda.html">Ajuda</a>
        <a href="#">Suporte</a>
        <a href="Historia do projeto.html">História por trás do projeto</a>
    </nav>
    <main>
    <div class = "forum">
      <h1>Teste beta do "Sammy"</h1>
    </div>
    <div class="post-form">
      <h2>Novo post</h2>
        <input type="text" id="postTitle" placeholder="Título do post">
        <textarea id="postContent" placeholder="Escreva seu post aqui..."></textarea>
        <button onclick="addPost()">Postar</button>
        
    </div>
    <hr>
   <div id="postContainer">
<?php include "carregar_posts.php"; ?>
</div>

    </main>
    <footer>
      &copy;2026.Todos os direitos reservados a mim :)
    </footer>
     <script src="posts.js"></script>
  </body>
</html>