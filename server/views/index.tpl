									<!-- Landing home page -->

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Quest</title>

		<!-- Custom CSS-->
		<link rel="stylesheet" type="text/css" href="/css/index.css">

		<!-- Latest compiled and minified Bootstrap CSS -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

		<!-- Usig font awesome with bootstrap -->
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/css/font-awesome.min.css">
	</head>

<!-- ____________________________________________________________________________________________________________________  -->
									<!-- Main Body -->
	<body>

	<!--  If not loggedin, show login with google-->
	% if loggedIn == 0:
		<div class="container" style = "visibility: hidden;">
			<div class="row" id = "modalRow">
				<div class="col-md-4 col-md-offset-10">
					<!-- Todo: Remove hidden style below-->
					<a id = "signInBtn" class="btn btn-block btn-social btn-google" href = "/googleLogin">
						<span class="fa fa-google"></span> Sign in
					</a>
				</div>
			</div>
		</div>			
	% end

<!-- _______________________________________________-->
		
	<!--  If loggedin, show profile in modal-->
	% if loggedIn == 1:
		<div class="container" style = "visibility: hidden;">
			<div class="row" id = "modalRow">
				<div class="col-md-4 col-md-offset-10 col-sm-4 col-sm-offset-8 col-xs-8 col-xs-offset-5">
					<h4>{{email}}</h4>
					<!-- Trigger the modal with a button -->
					<button type="button" class="btn btn-success" data-toggle="modal" data-target="#myModal">See Profile</button>
					<a href= "/logout" class="btn btn-info" role="button">Log out
					</a>

					  
					  <!-- Modal -->
					  <div class="modal fade" id="myModal" role="dialog">
					    <div class="modal-dialog">
					    
					      <!-- Modal content-->
					      <div class="modal-content" id = "myModalContent">
					        <div class="modal-header">
					          <button type="button" class="close" data-dismiss="modal">&times;</button>
					          <h4 class="modal-title">My Profile</h4>
					        </div>
					        <div class="modal-body">
					        % if fullName != '':	
					         	<p> Full name: {{fullName}}</p>
					        % end  
					          <p> Email: {{email}}</p>
					          <img id = "profilePicture" 
					          	src = "{{picture}}">	

					        </div>
					        <div class="modal-footer">
					          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
					        </div>
					      </div>
					      
					    </div>
					  </div>					  
				</div>	  
			</div> 		  
		</div>
	% end	
	
<!-- _______________________________________________-->

	<!-- Logo with input box-->
	<div class="container">
		<div class="row" id = "searchRow"> <!-- Put here to move whole body around-->
			<div class="col-md-4 col-md-offset-4 col-sm-8 col-sm-offset-2 col-xs-9 col-xs-offset-2">
				<!--<h1 id = "heading">Quest Engine</h1>-->
				<img id = "doodleHeading" src = "/images/doodle.gif">
				<img id = "logoImage" src = "/images/logo.png">
				<form  id = "queryForm" action="/" method="get">
					<input type="text"  name="keywords" id = "queryInput" autocomplete="on">
					<input type="submit" name="submit" value="Search">
				</form>					
			</div>   
		</div>
	</div>


	</body>

<!-- ___________________________________________________________________________________________________________________________  -->
								<!-- Scripts -->

	<!-- jQuery library -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

	<!-- Latest compiled Bootstrap JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

</html>

<!-- ___________________________________________________________________________________________________________________________  -->
