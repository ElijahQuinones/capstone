// Sidebar functionality
var sidebarOpen = false;
var sidebar = document.getElementById("sidebar");
function refresh(){
    window.location.reload();
}
function openSidebar() {
    if(!sidebarOpen) {
        sidebar.classList.add("sidebar-responsive");
        sidebarOpen = true;
    }
}
function hide(){
    document.getElementById("chart").style.display ="none";
    document.getElementById("refresh").style.display ="none";
}
function closeSidebar() {
    if(sidebarOpen) {
        sidebar.classList.remove("sidebar-responsive")
        sidebarOpen = false;
    }
}
var counter = 1;
const dropdown = document.getElementById("operations");
let selectedValue = dropdown.value;
let usedValue = null;
dropdown.addEventListener('change',function() {
    selectedValue = dropdown.value;
    console.log(counter)
    console.log("selcted value" + selectedValue);
    
// Datatables.net integration
    
    var table = $('#example').DataTable({
        "responsive": true,
        "autoWidth": true,
        "scrollX": true,
        "ajax": {
            "url": "/boto3/cloudtrail/"+selectedValue+"/90",
            "dataType": "json",
            "dataSrc": "Events"
        },
        "columns": [
            { "data": "Username" },
            { "data": "EventId" },
            { "data": "EventSource" },
            { "data": "EventTime" },

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
    document.getElementById("chart").style.display ="block";
    document.getElementById("refresh").style.display ="block";
    document.getElementById('enventForm').hidden = true;
    document.getElementById("refresh").hidden = false;
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
