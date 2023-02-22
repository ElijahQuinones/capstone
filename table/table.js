$(document).ready( function () {
    $('#table').DataTable();
        'ajax' ; '/table.json'
        'columns' ; [
            {'data' : 'a'},
            {'data' : 'b'},
            {'data' : 'c'},
            {'data' : 'd'}
        ]
} );