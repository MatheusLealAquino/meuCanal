$(function() {
    $('[data-toggle="tooltip"]').tooltip();
});
$(function() {
    $('[data-toggle="popover"]').popover();
});

var vid = document.querySelector("#myVideo");
vid.onended = function() {
	document.querySelector("#collapseOne").classList.add("show");	
};


