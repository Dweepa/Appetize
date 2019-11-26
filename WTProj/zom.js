function check(place){
	const sleep = (milliseconds) => {
  		return new Promise(resolve => setTimeout(resolve, milliseconds))
		}

	req = new XMLHttpRequest();
	req.open('GET',"https://developers.zomato.com/api/v2.1/cities?q="+place,true);
	req.setRequestHeader("user-key","f1d0d3a92fd05d129a037d26a992ca67");
	req.send();

	req.onload = function(){
	res = JSON.parse(this.responseText);
	city_id = res["location_suggestions"]["0"]["id"];
	console.log(city_id);

	req2 = new XMLHttpRequest();
	req2.open('GET',"https://developers.zomato.com/api/v2.1/search?entity_id="+city_id+"&entity_type=city",true);
	req2.setRequestHeader("user-key","f1d0d3a92fd05d129a037d26a992ca67");
	req2.send();

	req2.onload = async function(){
		res2 = JSON.parse(this.responseText);
		disp(res2["restaurants"]);
		console.log(res2);
		await sleep(5000);
		first(res2["restaurants"])
	}
	}

	function disp(results){
		resultArea.innerHTML = "";
		var i;
		for(i=0;i<20;i++){	
		const newResult = rTemp.content.cloneNode(true);

		var x = results[i]["restaurant"]
    	newResult.querySelector('.result-title').innerText = x["name"];
    	newResult.querySelector('.result-rating').innerText = x["user_rating"]["aggregate_rating"];   	
    	newResult.querySelector('.result-cuisine').innerText = x["cuisines"];
    	newResult.querySelector('.result-neighborhood').innerText = x["location"]["locality"];
    	newResult.querySelector('.result-address').innerText = x["location"]["address"];
    	newResult.querySelector('.result-price').innerText = '₹'.repeat(x["price_range"]);
    	newResult.querySelector('.result-thumbnail').src = "loading.gif";
    	newResult.querySelector('.result-thumbnail').id = "pic"+i;
    	//newResult.querySelector('.result-thumbnail').src = x["thumb"];
    	newResult.querySelector('.result-website').href = x["url"];    	
    	newResult.querySelector('.result-comment').href = "http://localhost:3000/?rest="+x["name"];
    	resultArea.appendChild(newResult);
    	window.scrollTo(0,1000);
  		}
	}

	async function first(res){
		var i;	
		for(i=0;i<10;i++)
		{
			var x = res[i]["restaurant"];
			var picid = "pic"+i;
			var el = document.getElementById(picid);
			el.src = x["thumb"];
		}
		await sleep(5000);
		second(res);
	}

	function second(res){
		var i;	
		for(i=10;i<20;i++)
		{
			var x = res[i]["restaurant"];
			var picid = "pic"+i;
			var el = document.getElementById(picid);
			el.src = x["thumb"];
		}
}
}


