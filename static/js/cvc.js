var first, second, steps = 1;

function init(size) {
    first=new Array(size);
    second=new Array(size);
    for (var i = 0; i < size; ++i) {
        first[i] = size;
        second[i] = size;
    }
    next();
}

function whos_turn() {
    return (steps % 2 == 1 ? "A" : "B");
}
var badge_styles = ["important", "info"];
var alias = {"A": "Artificial Stupidity", "B": "Artificial Intelligence", }

function game_over_or(action) {
    //if(steps >= 5) return;
    if(first_is_winning()) {
            var table = generateTable(first, second, false, false);
            $('#battle_field').prepend(generateBlock(table, alias["A"] + " Wins!", "success", steps++));
    } else if(second_is_winning()) {
        var table = generateTable(first, second, false, false);
        $('#battle_field').prepend(generateBlock(table, alias["B"] + " Wins!", "warning", steps++));
    } else {
        action();
    }
}

function second_is_winning() {
    for(var i in first) {
        if(first[i] != 0) {
            return false;
        }
    }
    return true;
}

function first_is_winning() {
    for(var i in second) {
        if(second[i] !=0) {
            return false;
        }
    }
    return true;
}

function next(response) {
    if(response) {
        console.log(response);
        $('#battle_field').children().first().remove();
        var table = generateTable(first, second, false, false);
        console.log(steps);
        console.log($(table.children()[(steps - 1) % 2]));
        select($(table.children(".btn-group")[(steps - 1) % 2]).find(".btn")[response.selected_index]);
        var block = generateBlock(table, alias[whos_turn()], badge_styles[(steps - 1) % 2], steps).hide();
        steps++;
        $('#battle_field').prepend(block);
        block.show('slow');
        first = response.current.A;
        second = response.current.B;
    }
    game_over_or(function() {
        $('#battle_field').prepend(generateBlock($("<div id='spinner_wrapper'></div>").append(new Spinner().spin().el), whos_turn(), "default", steps));
        var data_to_send = {
            "A": first,
            "B": second, 
            "whos_turn": whos_turn(),
        };
        $.ajax("/ajax/cvcnext", {
            type: "post",
            data: JSON.stringify(data_to_send),
            contentType:"application/json; charset=utf-8",
            dataType:"json",
            success: next,
        });
    });

}