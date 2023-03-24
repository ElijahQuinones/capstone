$(document).ready(function () {
    $('#example').DataTable({
        ajax: './data.json',
        columns: [
            { Records: 'eventVersion' },
            {
                Records: {
                    _: 'userIdentity.type',
                    sort: 'userIdentity.principleId',
                    sort: 'userIdentity.arn',
                    sort: 'userIdentity.accessKeyId',
                    sort: 'userIdentity.accountId',
                    sort: 'userIdentity.userName',
                },
            },
            { Records: 'eventTime' },
            { Records: 'eventSource' },
            { Records: 'eventName' },
            { Records: 'awsRegion' },
            { Records: 'sourceIPAddress' },
            { Records: 'userAgent' },
        ],
    });
});
