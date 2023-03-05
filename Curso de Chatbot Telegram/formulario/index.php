<html>

<header>
	<meta charset='UTF-8'>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
	<title>Formulario de envio</title>
</header>

<body>
	<div class="container" style="margin-top:100px; width:600px">
		<div class="form-group">
	<form action="enviomsg.php" method="post">
    			<label for="exampleFormControlSelect1">Selecione o time</label>
		    	<select class="form-control" name="time">
		      	<option>São Paulo</option>
		      	<option>Corinthians</option>
		      	<option>Palmeiras</option>
		      	
		    </select>
		</div>
		<div class="form-group">
   			 <label for="exampleFormControlTextarea1">Texto de envio</label>
   			 <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" name="texto"></textarea>
  		</div>
  		<button type="submit" class="btn btn-primary">Enviar</button>

	</form>
	</div>
</body>

</html>

