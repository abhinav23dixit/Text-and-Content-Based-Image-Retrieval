<!DOCTYPE html>
<html>

   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
   <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<link rel="stylesheet" href="css/iconic-bootstrap.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<head>
    
    
    
    
    
            
    
  <title>Content Based Image Retreival</title>
  <style type="text/css">
.loader {
  border: 16px solid #0077FF;
  border-radius: 50%;
  border-top: 16px solid #3498db;
  width: 120px;
  height: 120px;
  -webkit-animation: spin 2s linear infinite; /* Safari */
  animation: spin 2s linear infinite;
}

/* Safari */
@-webkit-keyframes spin {
  0% { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}  
  body {
      background-color:#F0FFF0 ;
      text-align: center;
      margin-top:250px;
      margin-bottom: auto;
      color: black;
  }
  .modal {
    width: 500px; 
    margin: 0 auto; 
    margin-top:250px;
  }
  

    form {
      text-align: center;
    }
  </style>
</head>



<body>
     <h1 >CONTENT BASED IMAGE RETRIEVAL</h1>
     <br>
     <br>
    

     <button type="button" id="imagebtn" class="btn btn-primary" data-toggle="modal" data-target="#imagemodal"  >
        IMAGE SEARCH
      </button>      
  
      <button type="button" id="textbtn" class="btn btn-primary" data-toggle="modal" data-target="#textmodal"  >
          TEXT SEARCH
        </button>

     <div class="modal fade bd-example-modal-lg" id="textmodal" tabindex="-1" role="dialog"   >
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">TEXT SEARCH</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form action="search.php" method="post" enctype="multipart/form-data">
                <div class="input-group">
                  <input type="text" class="form-control" name="searchterm" placeholder="Search Query" required>
                  <div class="input-group-append" id="button-addon">
                    <button class="btn btn-outline-secondary" id="submit2" type="submit" name="submit2" onclick="myFunction()">Search</button>
                    
                  </div>
                </div>
             </form>
            </div>
          </div>
          <div class="loader" id="myDIV1" style="display:none;margin-top:50px;margin-left:auto;margin-right: auto"></div>
        </div>
      </div>
    </div>








    <div class="modal fade bd-example-modal-lg" id="imagemodal" tabindex="-1" role="dialog" >
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">IMAGE SEARCH</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
                <form action="upload.php" method="post" enctype="multipart/form-data">
                  <div class="input-group">
                    <div class="custom-file">
                      <input type="file" class="custom-file-input" id="fileToUpload" name="fileToUpload" accept=".jpg, .png, .jpeg" required>
                      <label class="custom-file-label">Choose file</label>
                    </div>
                    <div class="input-group-append">
                      <button class="btn btn-outline-secondary" id="submit" type="submit" onclick="myFunction2()">Search</button>
                    </div>
                  </div>              
              </form>

            
          
          </div>


          </div>
        <div class="loader" id="myDIV" style="display:none;margin-top:50px;margin-left:auto;margin-right: auto"></div>
  
      </div>
    </div>

    <script>
function myFunction() {
    var x = document.getElementById("myDIV1");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function myFunction2() {
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
    </script>
  <script type="text/javascript" src="js/jquery-3.3.1.min.js"></script>
    <!-- Bootstrap tooltips -->
    <script type="text/javascript" src="js/popper.min.js"></script>
    <!-- Bootstrap core JavaScript -->
    <script type="text/javascript" src="js/bootstrap.min.js"></script>
    <!-- MDB core JavaScript -->
    <script type="text/javascript" src="js/mdb.min.js"></script>
 <script type="text/javascript" src="js/materialize.min.js"></script>


</body>
<footer style="margin-top: 250px">
	<h4>Collaborators</h4>
	<hr>
	Abhinav Dixit &nbsp; Ishaan Rajput &nbsp; Abhishek Sharma &nbsp; Harshita Rastogi &nbsp; John Prasad


</footer>
</html>

