<!-- Landing home page -->

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Quest results</title>

		<!-- Custom CSS-->
		<link rel="stylesheet" type="text/css" href="/css/results.css">
	
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
		<div class="container">
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

	<!--  If loggedin, show profile in modal -->
	% if loggedIn == 1:
		<div class="container">
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
					        	<img id = "profilePicture" src = "{{picture}}">	
					        </div>
<!-- _______________________________________________-->

					        <!-- History summary of the user's searches. Todo: May move this to modal section-->
							<h3 style = "text-align:center"> Results for top 20 most searched keywords</h3>
							<table id = "history" style = "text-align:center">
								<tr>
									<td><b>Word <br> </b></td>
									<td><b>Count</b></td>
								</tr>
								% for i, (a, b) in enumerate(top20List):
								<tr>
									<td> {{a}} <br></td>
									<td>{{b}} </td>
								</tr>
								% end
							</table>						
						
							<h3 style = "text-align:center"> Results for 10 most recent keywords</h3>
							<table id = "history" style = "text-align:center">
								<tr>
									<td><b> Word <br></b></td>
									<td><b>Rank</b></td>
								</tr>
								% for i, val in enumerate(mostRecentlySearched):
								<tr>
									<td>{{val}}</td>
									<td>{{i+1}}</td>
								</tr>
								% end
							</table>
<!-- _______________________________________________-->
							
							<br>

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

	<!-- Query form in the result page to search again-->
	<div class="container" style = "margin-top:2%;">
		<div class="row" id = ""> <!-- Put here to move whole body around-->
			<div class="col-md-7 col-md-offset-2 col-sm-8 col-xs-8 col-xs-offset-2">				
				<form action="http://localhost:8080" method="get" style="width: 200%">
					<input type="text"  id = "QueryInput" name="keywords" id = "queryInput">
					<input type="submit" name="submit" value="Search">
				</form>					
			</div>   
		</div>
	</div>

<!-- _______________________________________________-->


	<h1> Search for "{{keywords}}" </h1>
	<!-- Results for search in the form if urls. Todo: fix CSS here-->		

		<!-- Printing result URLs on a table-->
		
			<table id = "results" style = "margin: 0 auto;" position = "fixed">
				<!-- Commented out for lab3 - unsure if needed or not
				<tr>
					<td><b>Word <br> </b></td>
					<td><b>Count</b></td>
				</tr>
				% for word in seen:
				<tr>
					<td> {{word}}</td>
					<td>{{currentWordList[word]}}</td>
				</tr>
				% end
				-->			
				% for url in urlList:			
					<tr>
						<td><p>{{url}}</p></td>
					</tr>
				% end
			</table>
				


	<div class = "container" style = "text-align:center; margin-bottom:5%;">
		<!-- Previous and next buttons to go to previous and next pages-->
		<button type="button" id = "previousButton"> See previous 5 URLs</button>
		<button type="button" id = "nextButton"> See next 5 URLs </button>
	</div>
	
<!-- _______________________________________________-->

	<!-- Commented out for lab3
		<h2> Number of keywords are {{len(keywordList)}}</h2>
	-->
<!-- __________________________________________________________________________________________  -->
		<br>

<!-- ____________________________________________________________________________________________________________________  -->

	</body>
	<!-- jQuery library -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>

	<!-- Custom JS-->
	<script src="/javascript/results.js"></script>

	<!-- Latest compiled Bootstrap JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

</html>

