var first, second;
function init(size) {
    first=new Array(size);
    second=new Array(size);
    for (var i = 0; i < size; ++i) {
        first[i] = size;
        second[i] = size;
    }
    var table = generateTable(first, second, true, false)
    table.children().first().find(".btn").click(table_click_handler(first, second));
    $('#battle_field').append(generateBlock(table, "Human", "info"));
}

function table_click_handler() {
    return function(e) {
        select($(e.currentTarget));
        $(e.currentTarget).parent().children('.btn').off().attr("disabled", true);
        $.ajax("/ajax/hvcnext", {
            type: "post",
            data: JSON.stringify(move($(e.currentTarget).index())),
            contentType:"application/json; charset=utf-8",
            dataType:"json",
            success: next_handler,
        });
    };
}

function move(selectedIndex) {
    var cat = first.concat(second.reverse());
    var num_pebbles = cat[selectedIndex];
    cat[selectedIndex] = 0;
    for(var i = selectedIndex + 1; num_pebbles > 0; ++i, --num_pebbles) {
        cat[i % cat.length] += 1;
    }
    first = cat.slice(0, cat.length / 2);
    second = cat.slice(cat.length / 2, cat.length).reverse();
    return [first, second]
}


function next_handler(response) {
    var tableComputer = generateTable(first, second, false, false);
    select(tableComputer.children().last().find(".btn")[response.selected_index])
    $('#battle_field').prepend(generateBlock(tableComputer, "Computer", "important"));
    first = response.current[0];
    second = response.current[1];
    var tableHuman = generateTable(first, second, true, false);
    tableHuman.children().first().find(".btn").click(table_click_handler(first, second));
    $('#battle_field').prepend(generateBlock(tableHuman, "Human", "info"));
}