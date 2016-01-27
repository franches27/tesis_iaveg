window.$ = require('jquery');
$.fn.datatable = require('datatables');

$(document).ready(function() {
	$('input , textarea')
		.on('change', function(event) {
			var $input = document.getElementById($(this).attr('id'));
			if($input.validity.valid){
				$(this)
					.parent()
					.find('.form-validate-input,textarea,input')
					.removeClass('danger')
					.parent()
					.find('.form-validate-icon')
					.remove();
				$(this)
					.parent()	
					.append('<span class="icon-checkmark2 form-validate-icon validity" tittle="'+
						$input.validationMessage+'"><span>');
			}else{
				$(this)
				.parent()
				.find('.form-validate-icon')
				.remove();
				$(this)
				.parent()
				.append('<span class="icon-warning form-validate-icon" tittle="'+'"><span>')
				.find('.form-validate-input,textarea,input')
				.addClass('danger');	
				validation_message(this,$input.validationMessage);
			}
		})
		.on('invalid', function(event) {
			event.preventDefault();
			var $input = document.getElementById($(this).attr('id'));
			$(this)
			.parent()
			.find('.form-validate-icon')
			.remove();
			$(this)
			.parent()
			.append('<span class="icon-warning form-validate-icon" tittle="'+
				$input.validationMessage +'"><span>')
			.find('.form-validate-input,textarea,input')
			.addClass('danger');
			validation_message(this,$input.validationMessage);
		});
	$('#mytest')
		.on('submit', function(event) {
			$(this)
				.find('.form-validate-input,textarea,input')
				.removeClass('danger')
				.parent()
				.find('.form-validate-icon')
				.remove();
			$(this)
				.parent()	
				.append('<span class="icon-checkmark2 form-validate-icon validity"><span>');
		});
});
function validation_message(elem, message){
	$(elem).parent().find('.form-validate-icon').on('mouseover',function(){
		$('.form-validate-message').remove();
		$(this).parent().append('<div class="form-validate-message">'+message+'</div>');
	});
	$(elem).parent().find('.form-validate-icon').on('mouseout',function(){
		setTimeout(function(){$('.form-validate-message').remove();},1000);
	});

}