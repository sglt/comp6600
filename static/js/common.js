// Construct a jquery object representing a two-rows table
function generateTable(firstRowElements, secondRowElements, firstRowEnabled, secondRowEnabled) {
    var i;
    var firstRow = $('<div class="btn-group"></div>');
    for (i in firstRowElements) {
        firstRow.append($("<div class='btn btn-primary'" + (firstRowEnabled ? "" : " disabled") + ">" + firstRowElements[i] + "</div>"));
    }
    
    var secondRow = $('<div class="btn-group"></div>');
    for (i in secondRowElements) {
        secondRow.append($("<div class='btn btn-inverse'" + (secondRowEnabled ? "" : " disabled") + ">" + secondRowElements[i] + "</div>"));
    }
    
    var table = $('<div></div>');
    table.append(firstRow);
    table.append($('<br/>'));
    table.append(secondRow);
    
    return table;
}

function generateBlock(table, title, styleclass) {
    var html = $('<div></div>');
    html.append($('<div class="block_title"><span class="label ' + styleclass + '">' + title + '</span></div>'));
    html.append(table);
    return html;
}
var ee;
$(document).ready(function(){
    $('#btngroup_choosesize > .btn').click(function(e) {
        $('#modal_choosesize').modal("hide");
        init(parseInt(e.currentTarget.innerText));
        ee=e;
    });
    $('#modal_choosesize').modal({backdrop: 'static', keyboard: false});
});