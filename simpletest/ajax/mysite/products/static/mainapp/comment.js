$("#commentlist").ready(function() {
    $.ajax({
        url: '/products/',
        type: 'GET',
        success: getComment,
    });
});



$("#com").click(function(e) {
    var Name = $('input[name=comment]').val()
    //alert(Name)
    $.ajax({
        type: "POST",
        url: '/commentadd/',
        dataType: 'json',
        data: JSON.stringify({
            'name': Name
        }),
        success: getComment,
    });
});



function getComment(response) {
    var Json = JSON.parse(response)
    textcomment = ""
    for (var i = 0; i < Json.length; i++) {
        textcomment += "<h1>" + Json[i].fields['name'] + "</h1>"
        console.log(textcomment)
    }
 
    if (textcomment == "")
        $("#commentlist").html("No products available, add one below please")
    else
        $("#commentlist").html(textcomment)

}