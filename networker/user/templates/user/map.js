	function initialize() {

		// center the map on the middle of USA
		var center_usa = {lat: 39.5, lng: -98.35};

		// initialization for basic display of map
		var mapCanvas = document.getElementById('map');
		var mapOptions = {
			center: center_usa,
			zoom: 4,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		};
		var map = new google.maps.Map(mapCanvas, mapOptions);

		// gets JSON to display markers
		$.getJSON("/static/ajax/user_address.json", function(data) {
			$.each(data, function (key, value) {
				var address_coordinates = new google.maps.LatLng(value.fields.latitude_api, value.fields.longitude_api);
				var marker = new google.maps.Marker({
					position: address_coordinates,
					map: map,
					title: value.fields.first_name + ' ' + value.fields.last_name
				});

				// info window
				var contentString = 
					'<div>' +
						'<img src="/static/' + value.fields.profile_image + '" alt="' + value.fields.first_name + ' ' + value.fields.last_name + ' Profile Image" class="map_image">' +
			      		'<h1>' + value.fields.first_name + ' ' + value.fields.last_name +
			     		'</h1>' +
			      		'<div>' +
			      			'<p>' + value.fields.city_town + ', ' + value.fields.state_province + 
			      			'</p>' +
			      		'</div>'+
			      	'</div>';

				var infowindow = new google.maps.InfoWindow({
					content: contentString,
    				maxWidth: 200
				});

				marker.addListener('click', function() {
					infowindow.close();
					infowindow.open(map, marker);
				})
			})
		});
	});

	google.maps.event.addDomListener(window, 'load', initialize);



