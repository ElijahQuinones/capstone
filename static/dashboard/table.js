$(document).ready(function() {
    $('#example').DataTable({
        "responsive": true,
        "ajax": {
            "url": "/boto3/cloudtrail/ConsoleLogin/50",
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