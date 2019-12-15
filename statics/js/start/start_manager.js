function getRandomRgb() {
  let num = Math.round(0xffffff * Math.random());
  let r = num >> 16;
  let g = num >> 8 & 255;
  let b = num & 255;
  return 'rgb(' + r + ', ' + g + ', ' + b + ')';
}


function addData(chart, label, amount) {
    if (amount) {
        if (!(chart.data.labels.includes(label))) {
            chart.data.labels.push(label)
            chart.data.datasets[0].data.push(parseInt(amount));
            chart.data.datasets[0].backgroundColor.push(getRandomRgb())
            chart.options.elements.center.text += parseInt(amount);
        }else {
            let index = chart.data.labels.indexOf(label);
            chart.data.datasets[0].data[index] += parseInt(amount);
            chart.options.elements.center.text += parseInt(amount);
        }
        chart.update();
    }
}

function expense_form_submit() {
    $("#expense_form").on('submit', function (event) {
        let $btn = $(document.activeElement);
        event.preventDefault();
        let formData = new FormData(this);
        formData.append($btn.attr("name"), '');
        let page_url = $('form').attr('action');

        let category = formData.get('expense_category');
        let amount = formData.get('amount');
        addData(Chart1, category, amount);


        $.ajax({
            url: page_url,
            data: formData,
            type: "POST",
            async: true,
            success: (data) => {
                $('.modal').modal('hide');
            },
            cache: false,
            contentType: false,
            processData: false,
        })
    });

}

function income_form_submit() {
    $("#income_form").on('submit', function (event) {
        let $btn = $(document.activeElement);
        event.preventDefault();
        let formData = new FormData(this);
        formData.append($btn.attr("name"), '');
        let page_url = $('form').attr('action');

        let category = formData.get('income_category');
        let amount = formData.get('amount');
        addData(Chart2, category, amount);

        $.ajax({
            url: page_url,
            data: formData,
            type: "POST",
            async: true,
            success: (data) => {
                $('.modal').modal('hide');
            },
            cache: false,
            contentType: false,
            processData: false,
        })
    });

}

$(function () {
    expense_form_submit();
    income_form_submit();
})










