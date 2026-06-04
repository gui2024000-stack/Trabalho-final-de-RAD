function addPost() {
  const title = document.getElementById('postTitle').value;
  const content = document.getElementById('postContent').value;

  if (!title || !content) {
    alert('Preencha título e conteúdo!');
    return;
  }

  const postDiv = document.createElement('div');
  postDiv.className = 'post';
  postDiv.innerHTML = `
    <h3>${title}</h3>
    <p>${content}</p>
    <input type="text" placeholder="Comentário">
    <button onclick="addComment(this)">Comentar</button>
    <div class="commentsContainer"></div>
  `;

  document.getElementById('postContainer').appendChild(postDiv);

  document.getElementById('postTitle').value = '';
  document.getElementById('postContent').value = '';
}

function addComment(button) {
  const input = button.previousElementSibling;
  const text = input.value;
  if (!text) {
    alert('Escreva um comentário!');
    return;
  }

  const commentDiv = document.createElement('div');
  commentDiv.className = 'comment';
  commentDiv.textContent = text;

  button.nextElementSibling.appendChild(commentDiv);
  input.value = '';
}