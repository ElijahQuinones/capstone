$(document).ready(function() {
    $('#example').DataTable({
        "processing": true,
        "responsive": true,
        "ajax": {
            "url": "/boto3/cloudtrail/ConsoleLogin/7",
            "dataType": "json",
            "dataSrc": "Events"
        },
        "columns": [
            // { "data": "userIdentity.userName" },
            // { "data": "userIdentity.accountId" },
            // { "data": "eventTime" },
            { "data": "EventId" },
            { "data": "EventName" },
            { "data": "EventSource" },
            { "data": "Username" },
            { "data": "EventTime" },

        ]
    });
});