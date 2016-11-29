var index = 0;

$(document).ready(function(){	

	console.log("Hi this is js. Index is " + index);

//---------------------------------------------------------------
	$( "#nextButton" ).click(function() 
	{
		index = index + 1;
		console.log("next: index is now " + index);

		$.ajax({
            url: "/prevNext",
            type: "POST",
            data: { index: index},
            dataType: "json",
            success: function (data) 
            {
            	console.log("data returned from server is ", data);
            	if(data.length <= 0)
            	{   
  					console.log("data is empty so reduce index back again.");
  					index = index - 1;
  					console.log("Index is now: " + index);
  					return;
            	}

            	//Data not empty
            	else
            	{
            		console.log("data is not empty!!!!");
            		//remove all past entries
            		$( "#results" ).empty();
            		for (var item in data)
					{
						console.log("item is ", data[item]);
						$("#results").append('<tr><td><p>'+data[item]+'</p></td></tr>');
	            	}
	            	return;
	            }	
            }	
        });
	});

//---------------------------------------------------------------

	$( "#previousButton" ).click(function() 
	{
		if((index-1)<0)
		{
			console.log("Index will become negative so return.")
			return;
		}

		index = index - 1;
		console.log("prev: index is now " + index);

		$.ajax({
            url: "/prevNext",
            type: "POST",
            data: { index: index},
            dataType: "json",
            success: function (data) 
            {
            	console.log("data is ", data);

            	//remove all past entries
        		$( "#results" ).empty();

        		for (var item in data)
				{
					console.log("item is ", data[item]);
					$("#results").append('<tr> <td><p>'+data[item]+'</p></td></tr>');
            	}
            	return;
            }
        });
	});
});

