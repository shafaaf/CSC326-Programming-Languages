var index = 0;

$(document).ready(function(){	

	console.log("Hi");

	$( "#nextButton" ).click(function() 
	{
		index = index + 1;
		console.log("next: index is " + index);

		$.ajax({
            url: "/getUrlsUsingIndex",
            type: "POST",
            data: { index: index},
            dataType: "json",
            success: function (data) 
            {
            	console.log("data is ", data);
            }
        });
	});

	$( "#previousButton" ).click(function() 
	{
		index = index - 1;
		console.log("prev: index is " + index);

		$.ajax({
            url: "/getUrlsUsingIndex",
            type: "POST",
            data: { index: index},
            dataType: "json",
            success: function (data) 
            {
            	console.log("data is ", data);
            }
        });
/*
		$.post("/getUrlsUsingIndex",
	    { index: index},
	    function(data, status){
	        console.log("Data: " + data);
	    });
*/

	});
});

