<?php

include 'conexao.php';

$time = $_POST['time'];
$texto = $_POST['texto'];


$sql = "'SELECT * FROM usuario WHERE categoria_usuario = '$time'";
$buscar = mysqli_query($conexao, $sql);

while ($array = mysqli_fetch_array($buscar)) {

	$cid =  $array['chatid_usuario'];
	$nome = $array['nome_usuario'];
	
	echo $mensagem = "sudo telegramMsg '" . $cid . "'$nome, $texto'";
	
	$saida = exec($mensagem);
	echo "<pre>$saida</pre>";

}

?>
