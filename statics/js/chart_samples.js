Chart.defaults.global.animation.duration = 2000;

	Chart.pluginService.register({
		beforeDraw: function (chart) {
			if (chart.config.options.elements.center) {
        //Get ctx from string
        var ctx = chart.chart.ctx;

				//Get options from the center object in options
        var centerConfig = chart.config.options.elements.center;
      	var fontStyle = centerConfig.fontStyle || 'Arial';
				var txt = centerConfig.text;
        var color = centerConfig.color || '#000';
        var sidePadding = centerConfig.sidePadding || 20;
        var sidePaddingCalculated = (sidePadding/100) * (chart.innerRadius * 2)
        //Start with a base font of 30px
        ctx.font = "30px " + fontStyle;

				//Get the width of the string and also the width of the element minus 10 to give it 5px side padding
        var stringWidth = ctx.measureText(txt).width;
        var elementWidth = (chart.innerRadius * 2) - sidePaddingCalculated;

        // Find out how much the font can grow in width.
        var widthRatio = elementWidth / stringWidth;
        var newFontSize = Math.floor(30 * widthRatio);
        var elementHeight = (chart.innerRadius * 2);

        // Pick a new font size so it will not be larger than the height of label.
        var fontSizeToUse = Math.min(newFontSize, elementHeight);

				//Set font settings to draw it correctly.
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        var centerX = ((chart.chartArea.left + chart.chartArea.right) / 2);
        var centerY = ((chart.chartArea.top + chart.chartArea.bottom) / 2);
        ctx.font = fontSizeToUse+"px " + fontStyle;
        ctx.fillStyle = color;

        //Draw text in center
        ctx.fillText(txt, centerX, centerY);
			}
		}
	});

new Chart(document.getElementById("chartjs-4"),
    {"type":"doughnut",
        "data":{"labels":["Home","Other","Car"],
            "datasets":[{"label":"Expenses",
                "data":[300,50,100],
                "backgroundColor":
                    ["rgb(255, 99, 132)","rgb(54, 162, 235)","rgb(255, 205, 86)"]}]},
    "options":{ legend: { labels: { fontSize: 20 } },
                elements: {
				    center: {
				        text: '1255$',
                        color: '#9cadff', // Default is #000000
                        fontStyle: 'Arial', // Default is Arial
                        sidePadding: 20 // Default is 20 (as a percentage)
                                }

        }}});

new Chart(document.getElementById("chartjs-0"),{"type":"line",
    "data":{"labels":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
        "datasets":[{"label":"Card",
            "data":[20,30,50, 150, 30, 25,150],
            "fill":false,
            "borderColor":"rgb(75, 192, 192)",
            "lineTension":0.1},
            {"label":"Cash",
            "data":[455, 300, 500, 100, 200],
            "fill":false,
            "borderColor":"rgb(119,192,71)",
            "lineTension":0.1}
            ]},
    "options":{ legend: { labels: { fontSize: 20 } }}});

new Chart(document.getElementById("chartjs-1"),
    {"type":"bar","data":{"labels":["January","February","March","April","May","June","July"],
            "datasets":[{"label":"INCOME",
                "data":[5000,4250,6350,5500,6000,4000,5900],
                "fill":false,
                "backgroundColor":"rgb(157,255,139)",
                "borderColor":"rgb(255, 99, 132)",
                "borderWidth":1},
            {"label":"EXPENSES",
                "data":[ 4200 ,3760,5400,6000,4250,4500,3200],
                "fill":false,
                "backgroundColor":"rgba(255, 99, 132, 0.2)",
                "borderColor":"rgb(255, 99, 132)",
                "borderWidth":1}]},
        "options":{"scales":
                {"yAxes":[{"ticks":{"beginAtZero":true}}]}}});

