new Chart(document.getElementById("center-chart"),
    {"type":"doughnut",
        "data":{"labels":["Home","Other","Car"],
            "datasets":[{"label":"Expenses",
                "data":[300,50,100],
                "backgroundColor":
                    ["rgb(0,16,255)","rgb(235,1,0)","rgb(255,239,13)"]}]},

        "options":{ legend: { labels: { fontSize: 20 } },
                elements: {
				    center: {
				        text: '1255',
                        color: '#9cadff', // Default is #000000
                        fontStyle: 'Arial', // Default is Arial
                        sidePadding: 20 // Default is 20 (as a percentage)
                                },


        }}});