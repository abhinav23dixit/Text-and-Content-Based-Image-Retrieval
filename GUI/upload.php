<?php

			$file = $_FILES['fileToUpload'];
			$fileName = $_FILES['fileToUpload']['name'];
			$fileTmpName = $_FILES['fileToUpload']['tmp_name'];
			$fileNameNew = "file.jpg";
			$fileDestination = 'uploads/'.$fileNameNew;
			move_uploaded_file($fileTmpName, $fileDestination);
			header("Location: result.php");
?>