<?
$resposta = 'False';
if (isset($_GET['UID'])){
	$_uid = $_GET['UID'];

	$json_file = fopen('cadastro.json', 'r');
	$json_file = fread($json_file,filesize('cadastro.json'));
	$json = json_decode($json_file, true);


	#TODO

}

echo $resposta;
?>