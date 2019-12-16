new Chart(document.getElementById("daily_chart"),{"type":"line",
    "data":{"labels": time_list,
        "datasets":[{"label":"Expenses",
            "data":expenses_list,
            "fill":false,
            "borderColor":"rgb(75, 192, 192)",
            "lineTension":0.1}
            ]},
    "options":{ legend: { labels: { fontSize: 20 } }}});