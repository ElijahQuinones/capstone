// Sidebar functionality
var sidebarOpen = false;
var sidebar = document.getElementById("sidebar");

function openSidebar() {
    if(!sidebarOpen) {
        sidebar.classList.add("sidebar-responsive");
        sidebarOpen = true;
    }
}

function closeSidebar() {
    if(sidebarOpen) {
        sidebar.classList.remove("sidebar-responsive")
        sidebarOpen = false;
    }
}

// Datatables.net integration
$(document).ready(function() {
    var table = $('#example').DataTable({
        "responsive": true,
        "autoWidth": true,
        "scrollX": true,
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

    // Beginning of HighCharts integration (with steps)
    // Create the chart with initial data
    var container = $('<div/>').insertBefore(table.table().container());
 
    var chart = Highcharts.chart(container[0], {
        chart: {
            type: 'pie',
        },
        title: {
            text: 'AWS CloudTrail Logs',
        },
        series: [
            {
                data: chartData(table),
            },
        ],
    });

    // On each draw, update the data in the chart
    table.on('draw', function () {
        chart.series[0].setData(chartData(table));
    });
});

function chartData(table) {
    var counts = {};
 
    // Count the number of entries for each position
    table
        .column(0, { search: 'applied' })
        .data()
        .each(function (val) {
            if (counts[val]) {
                counts[val] += 1;
            } else {
                counts[val] = 1;
            }
        });
 
    // And map it to the format Highcharts uses
    return $.map(counts, function (val, key) {
        return {
            name: key,
            y: val,
        };
    });
}
