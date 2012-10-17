<?php require_once("connection.php"); ?>
<html>
	<head>
	</head>
	
	<body>
		<form action="search.php" method="get">	
				<b>Processor :</b>
				<select name="Processor">
					<option value="any">Any</option>
					<option value="Pentium Dual Core (2nd Generation)">Pentium Dual Core (2nd Generation)</option>
					<option value="Core i3 (1st Generation)">Core i3 (1st Generation)</option>
					<option value="Core i3 (2nd Generation)">Core i3 (2nd Generation)</option>
					<option value="Core i5 (2nd Generation)">Core i5 (2nd Generation)</option>
					<option value="Core i5 (3rd Generation)">Core i5 (3rd Generation)</option>
					<option value="Core i7 (2nd Generation)">Core i7 (2nd Generation)</option>
					<option value="Core i7 (3rd Generation)">Core i7 (3rd Generation)</option>
				</select></br>
				<b> Memory :</b>
				<select name="Memory">
					<option value="any">Any</option>
					<option value="2">2 GB</option>
					<option value="3">3 GB</option>
					<option value="4">4 GB</option>
					<option value="8">8 GB</option>
				</select></br>
				<b> Hard Disk :</b>
				<select name="HDD">
					<option value="any">Any</option>
					<option value="128">128 GB</option>
					<option value="320">320 GB</option>
					<option value="500">500 GB</option>
					<option value="1">1 TB</option>
				</select></br>
				<b> Operating System :</b>
				<select name="OS">
					<option value="any">Any</option>
					<option value="DOS">DOS/Linux/Ubuntu</option>
					<option value="Windows 7 Home Basic">Windows 7 Home Basic</option>
					<option value="Windows 7 Home Premium">Windows 7 Home Premium</option>
				</select></br>
				<b> Screen :</b>
				<select name="Screen">
					<option value="any">Any</option>
					<option value="13.3 Inch">13.3 Inch</option>
					<option value="14 Inch">14 Inch</option>
					<option value="15.6 Inch">15.6 Inch</option>
					<option value="17.3 Inch">17.3 Inch</option>
				</select></br>
				<input type="submit" name="Submit" value="search">
		</form>
	</body>
</html>