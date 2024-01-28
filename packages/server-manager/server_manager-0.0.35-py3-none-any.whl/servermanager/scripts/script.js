$(document).on('ajaxError', function(event, jqxhr, settings, thrownError) {
    console.log("Error");
    console.log(jqxhr);
    console.log(settings);
    console.log(thrownError);
});

const draw = (data, settings) => {
    if(settings.show.systime)
    {
        $('#systime').html(data.systime);
    }
    if(settings.show.uptime)
    {
        $('#uptime').html(data.uptime);
    }
    if(settings.show.cpu)
    {
        $('#clock').html(data.average_clock_speed + 'GHz');
        for (let i = 0; i < data.round_clock_speeds.length; i++) {
            $(`#clock${i}`).html(data.round_clock_speeds[i] + " GHz ");
            $(`#${i}`).html(data.cpu_core_usage[i] + "%");
        }
        $('#graph').attr('src', preceeder + '/graphs/cpu_usage_1?t=' + new Date().getTime());
        //updateImage(preceeder + '/graphs/cpu_usage_1?t=' + new Date().getTime(), '#graph');
    }

    if(settings.show.memory)
    {
        $('#used_mem').html(data.used_memory);
        $('#used_swap').html(data.used_swap);
        $('#used_mem_precent').html(data.used_memory_percent + " %");
        $('#used_swap_precent').html(data.used_swap_percent + " %");
        $('#graph_mem').attr('src', preceeder + '/graphs/memory_usage_1?t=' + new Date().getTime());
    }
}

const itteration = (settings) => {
    console.log("New Interval");
    $.ajax({
        url: `${preceeder}/ddata`,
        method: 'GET'
    }).done((response) => {
        var data = JSON.parse(response);
        draw(data, settings);
    })
}

$(document).ready(function() {
    //console.log(config);
    var settings = JSON.parse(config);
    itteration(settings);

    setInterval(() => {
        itteration(settings);
    }, settings.interval.interval_hw);
});

