$(document).on('ajaxError', function(event, jqxhr, settings, thrownError) {
    console.log("Error");
    console.log(jqxhr);
    console.log(settings);
    console.log(thrownError);
});

const draw = (data) => {
    $('#tb').html("");
    for (let i = 0; i < data["PID"].length; i++) {
        let appendable = `<tr id="${data["PID"][i]}" class="open-modal border-b transition-colors hover:bg-slate-600 data-[state=selected]:bg-muted">`;
        for (let j = 0; j < Object.keys(data).length; j++) {
            appendable += `<td class="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0 font-medium">${data[Object.keys(data)[j]][i]}</td>`
        }
        appendable += `</tr>`
        $('#tb').append(appendable);
    }
}

$(document).ready(function() {
    console.log("Ready");

    $(document).on('click', '.open-modal', function (event) {
        $('#modal').removeClass('hidden');
        $('#pid').html(event.currentTarget.id);
    });
  
    $('#closeModal').click(function () {
        $('#modal').addClass('hidden');
    });

    $('#Kill').click(function () {
        console.log(JSON.stringify({
            pid: $('#pid').html()
        }));
        $.ajax({
            url: `${preceeder}/kill`,
            method: 'POST',
            data: `"pid":${$('#pid').html()}`,
            dataType: 'text'
        }).done((response) => {
            $('#modal').addClass('hidden');
            $('#tb').html("");
            $.ajax({
                url: `${preceeder}/processes`,
                method: 'GET'
            }).done((response) => {
                data = JSON.parse(response);
                draw(data);
            })
        });
    });

    $.ajax({
        url: `${preceeder}/processes`,
        method: 'GET'
    }).done((response) => {
        data = JSON.parse(response);
        draw(data);

        console.log("Done");
        setInterval(() => {
            $.ajax({
                url: `${preceeder}/processes`,
                method: 'GET'
            }).done((response) => {
                data = JSON.parse(response);
                draw(data);
    
                console.log("Done");
            });
        }, config.interval.interval_proc);
    });
});
