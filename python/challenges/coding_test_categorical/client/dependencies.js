function ensure_requirement(resource){
    try {
	eval(resource);
    } catch (Exception) {
	$('#warnings').text(
	    'Error loading angular. Pease make sure it is reachable from the current host'
	);
    }
}


(function (){
    ensure_requirement('angular');
    ensure_requirement('bootstrap');
})();
