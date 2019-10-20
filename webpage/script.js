var medicine = [];

var add = function (product, hour, min, time) {
	medicine.push({
		product: product,
		hour: hour,
		min: min,
		time:time
	
	});
};

var addList = function () {
	var name 	= 	document.getElementById("name").value;
	var hour	= 	document.getElementById("hour").value;
	var min	= 	document.getElementById("min").value;
	var select 		= 	document.getElementById("Time");
	var time 	= 	select.options[select.selectedIndex].text;
	var listItens = document.getElementById("products-row");
	
	var fragment = document.createDocumentFragment();
	add(name, hour, min,time);
	medicine.forEach(function ( index ) {
		var tr = document.createElement("tr");
		for (var i in index) {
			var td = document.createElement("td");
			td.textContent = index[i];
	  	tr.appendChild(td);
		};
		fragment.appendChild(tr);
		listItens.appendChild(fragment);
	});
	medicine = [];
}
