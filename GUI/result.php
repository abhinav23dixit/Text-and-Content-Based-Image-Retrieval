<!DOCTYPE html>
<html>
<?php
header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");
?>


    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<head>
	<title>Result</title>
	<style type="text/css">
		body {
            background-color:#F0FFF0 ;
               
        font-family: 'Montserrat';
		font-weight: bold;
			margin-left:8%;
			color: black;
			
		}
	</style>
	
	<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
</head>
<body>
	<h2 style="font-size:50px">RESULT</h2><br>
	<h3 >Input Image:</h3>
	
	

	<img src="uploads/file.jpg" width='350px' hspace='25px' vspace='4px'>

	

	
	<?php	
		$result = exec("C:\\Users\\ishaa\\Anaconda3\\python.exe C:\\xampp\\htdocs\\Predict.py");
		$myfile = fopen("uploads/description.txt", "r");
		echo fgets($myfile);
		fclose($myfile);
	?>
	<br>
	<h3>Similar Images:</h3>
		<?php
		    
		        $dirname = "uploads/matched-images/";
		        $images = glob($dirname."*.jpg");
		        $inputFile = fopen("uploads/matched_images.txt", "r");
		        foreach($images as $image) {
		            //echo '<img src="'.$image.'" height="250px" hspace="4px" vspace="4px"/>';    
		                        if (($line = fgets($inputFile)))
		                        {
		                            
		                              echo "<img src=\"" . $image. "\" width='350px' hspace='25px' vspace='4px'>\n";     
		                                echo  "$line <br /><br />";
		                        } 
		                        else 
		                        {
		                            echo "Image '$image' has no metadata";
		                        } 
		        }
		        fclose($inputFile);
		        
		                
		?>
  
    
    
</body>
</html>