<?php require_once("connection.php"); ?>
<html>
	<head>
		<title> Search Result </title>
	</head>
	
	<body>
	<?php
	$processor=$_GET['Processor'];
	$memory=$_GET['Memory'];
	$hdd=$_GET['HDD'];
	$os=$_GET['OS'];
	$screen=$_GET['Screen'];
	
	$query = "select * from laptop_database ";
	$connector = "where";
	
	if(strcmp($processor,"any")==0) 
	{
		// User does not enter specific processor name
	}
	else  
	{
		// User has entered specific processor choice
		$query.=" {$connector} Processor='{$processor}'";
		$connector = "and";
	}
	
	if(strcmp($memory,"any")==0) 
	{
		// User does not enter specific Memory requirement
	}
	else
	{
		// User has entered specific Memory choice
		$query.=" {$connector} Memory='{$memory}'";
		$connector = "and";
	}
	
	if(strcmp($hdd,"any")==0)
	{
		// User does not enter specific HDD info
	}
	else  
	{
		// User has entered specific HDD space
		$query.=" {$connector} HDD='{$hdd}'";
		$connector = "and";
	}
	
	if(strcmp($os,"any")==0) 
	{
		// User does not enter specific Operating System
	}
	else
	{
		// User has entered specific OS
		$query.=" {$connector} OS='{$os}'";
		$connector = "and";
	}
	
	if(strcmp($screen,"any")==0) 
	{
		// User does not enter specific screen size
	}
	else  
	{
		// User has entered specific screen size
		$query.=" {$connector} Screen='{$screen}'";
	}
	
	$query.=";";
	
	$result = @mysql_query($query);
	
	if(mysql_affected_rows()==0)
	{
		echo "<br/>"."<br/>"."<h1>"."<center>"."No Results found"."</center>"."</h1>";
		exit(0);
	}
	while ($row = mysql_fetch_array($result))
	{
		?>
		 <td><center><a href = "<?php echo $row['Link'] ?>"> Select Laptop </a></center></td></br>
		 <?php
	}
	?>
	</body>
</html>