$(document).ready(function() {
    $('#example').DataTable({
        "processing": true,
        "responsive": true,
        "ajax": {
            "url": "/boto3/cloudtrail/<event_name>/<days>",
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