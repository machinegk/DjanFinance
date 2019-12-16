new Chart(document.getElementById("general_chart"),
    {"type":"bar","data":{"labels":time_list,
            "datasets":[{"label":"INCOME",
                "data":income_list,
                "fill":false,
                "backgroundColor":"rgb(157,255,139)",
                "borderColor":"rgb(255, 99, 132)",
                "borderWidth":1},
            {"label":"EXPENSES",
                "data":expenses_list,
                "fill":false,
                "backgroundColor":"rgba(255, 99, 132, 0.2)",
                "borderColor":"rgb(255, 99, 132)",
                "borderWidth":1}]},
        "options":{"scales":
                {"yAxes":[{"ticks":{"beginAtZero":true}}]}}});

