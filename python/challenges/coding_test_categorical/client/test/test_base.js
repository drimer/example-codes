describe('creating IDs', function(){
    it('ID with white spaces', function(){
	var id = Id('white chair');
	expect(id).toEqual('white-chair');
    });
});
