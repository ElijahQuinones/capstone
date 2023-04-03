$(document).ready(function() {
    $('#example').DataTable({
        "responsive": true,
        "ajax": {
            "url": "data.json",
            "dataSrc": "Records"
        },
        "columns": [
            { "data": "userIdentity.userName" },
            { "data": "userIdentity.accountId" },
            { "data": "eventTime" },
            { "data": "eventName" },
            { "data": "awsRegion" },
            { "data": "sourceIPAddress" }
        ]
    });
});