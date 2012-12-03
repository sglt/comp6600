var human, computer, steps = 1;

function init(size) {
    human=new Array(size);
    computer=new Array(size);
    for (var i = 0; i < size; ++i) {
        human[i] = size;
        computer[i] = size;
    }
}

function ask_computer() {
        $('#battle_field').prepend(generateBlock($("<div id='spinner_wrapper'></div>").append(new Spinner().spin().el), "Computer", "default", steps));
        var data_to_send = {
            "human": human,
            "computer": computer, 
            "agent": $("#choose_computer_title").text(),
        };
        $.ajax("/ajax/hvcnext", {
            type: "post",
            data: JSON.stringify(data_to_send),
            contentType:"application/json; charset=utf-8",
            dataType:"json",
            success: next_handler,
        });
}

function table_click_handler() {
    return function(e) {
        select($(e.currentTarget));
        $(e.currentTarget).parent().children('.btn').off().attr("disabled", true);
        move($(e.currentTarget).index());
        ask_computer();
    };
}

function move(selectedIndex) {
    console.log(computer)
    console.log(human)
    var cat = computer.concat(human.reverse());
    var mapped_selectedIndex = computer.length + (human.length - selectedIndex - 1);
    var num_pebbles = cat[mapped_selectedIndex];
    cat[mapped_selectedIndex] = 0;
    for(var i = mapped_selectedIndex + 1; num_pebbles > 0; ++i, --num_pebbles) {
        cat[i % cat.length] += 1;
    }
    computer = cat.slice(0, cat.length / 2);
    human = cat.slice(cat.length / 2, cat.length).reverse();
}


function next_handler(response) {
    console.log(response);
    var tableComputer = generateTable(computer, human, false, false);
    select(tableComputer.children().first().find(".btn")[response.selected_index])
    $('#battle_field').children().first().remove();
    $('#battle_field').prepend(generateBlock(tableComputer, "Computer", "important", steps++));
    human = response.current["human"];
    computer = response.current["computer"];
    var tableHuman = generateTable(computer, human, false, true);
    tableHuman.children().last().find(".btn").click(table_click_handler());
    var block = generateBlock(tableHuman, "Human", "info", steps++).hide();
    $('#battle_field').prepend(block);
    block.show('slow');
}

$(document).ready(function(){
    $('#choose_computer_menu a').click(function(e){
        $('#choose_computer_title').text($(e.currentTarget).text());
    });
    $('#btn_start').click(function(e){
         ask_computer();
         e.currentTarget.off();
    });
})