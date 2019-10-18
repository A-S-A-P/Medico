var medicine = [];

var add = function (product, quantity, price, category) {
	medicine.push({
		product: product,
		quantity: quantity,
		price: price,
		category: category
	});
};

var addList = function () {
	var name 	= 	document.getElementById("name").value;
	var dose	= 	document.getElementById("dose").value;
	var other 		= 	document.getElementById("other").value;
	var select 		= 	document.getElementById("Time");
	var time 	= 	select.options[select.selectedIndex].text;
	var listItens = document.getElementById("products-row");
	
	var fragment = document.createDocumentFragment();
	add(name, time, dose, other);
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
