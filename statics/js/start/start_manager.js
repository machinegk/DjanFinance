new Chart(document.getElementById("expense-chart"),
    {
        "type": "doughnut",
        "data": {
            "labels": labels1,
            "datasets": [{
                "label": "Expenses",
                "data": data1,
                "backgroundColor":
                backgroundColor1
            }]
        },
        "options": {
            legend: {labels: {fontSize: 20}},
            title: {
                display: true,
                fontSize: 30,
                text: "Expenses"
            },
            elements: {
                center: {
                    text: sum1,
                    color: 'red', // Default is #000000
                    fontStyle: 'Arial', // Default is Arial
                    sidePadding: 20 // Default is 20 (as a percentage)
                },


            }
        }
    });
new Chart(document.getElementById("income-chart"),
    {
        "type": "doughnut",
        "data": {
            "labels": labels2,
            "datasets": [{
                "label": "Income",
                "data": data2,
                "backgroundColor":
                backgroundColor2
            }]
        },
        "options": {
            legend: {labels: {fontSize: 20}},
            title: {
                display: true,
                fontSize: 30,
                text: "Income"
            },
            elements: {
                center: {
                    text: sum2,
                    color: 'green', // Default is #000000
                    fontStyle: 'Arial', // Default is Arial
                    sidePadding: 20 // Default is 20 (as a percentage)
                },


            }
        }
    });