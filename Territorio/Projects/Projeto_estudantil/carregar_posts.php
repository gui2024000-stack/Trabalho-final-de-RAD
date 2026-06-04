<?php

$conn = new mysqli("localhost","root","","forum");

$result = $conn->query(
"SELECT * FROM posts ORDER BY id DESC"
);

while($row = $result->fetch_assoc()){

echo "<div class='post'>";

echo "<h3>" .
htmlspecialchars($row["titulo"]) .
"</h3>";

echo "<p>" .
htmlspecialchars($row["conteudo"]) .
"</p>";

echo "</div>";

}

?>