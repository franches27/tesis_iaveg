function getParroquia() {
		$.getJSON('/location/parroquias/'+$('#municipio').val(), function(json, textStatus) {
		$('#parroquia').empty();
		$('#parroquia').append($('<option>'))
		$.each(json, function(index, val) {
			$('#parroquia').append($('<option>', {value: val.id, text: val.name}));
		
		});
	});
	
}
$(window).load(function() {
	getHousing();
	$('#municipio').change(function(event) {
		getParroquia();
	});
});

function getHousing() {
	
	var url = window.location.pathname;
	var p=url.split("/");
	var slug=p.pop();
	$.getJSON('/proyectos_viviendas/vivienda/'+slug, function(json, textStatus) {
		$.each(json, function(index, val) {
			$('h1#formt').append(''+val.name);
			$('#InputName').val(val.name);
			$('#InputNv').val(val.housing);
			$('input#numviv').val(val.housing);
			$('#ingeniero').val(val.engineer_id.id)	;

		});
	});

	//debugger
}
