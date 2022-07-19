$(document).ready(function() {
    $("#tableID").each(function() {
        var $this = $(this);
        var newTransposedRow = [];
        $this.find("tr").each(function() {
            var i = 0;
            $(this).find("td").each(function() {
                i++;
                if (newTransposedRow[i] === undefined) { newTransposedRow[i] = $("<tr></tr>"); }
                newTransposedRow[i].append($(this));
            });
        });
        $this.find("tr").remove();
        $.each(newTransposedRow, function() {
            $this.append(this);
        });
    });
});