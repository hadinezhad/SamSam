    $(document).on("click", ".dalert", function(e) {
            e.preventDefault();
            href = $(this).attr('href');
            return bootbox.confirm({
    message: "<br> آیا مطمئنید که می خواهید ادامه دهید ",
    buttons: {
        cancel: {
            label: '<i class="fa fa-times"></i> خیر'
        },
        confirm: {
            label: '<i class="fa fa-check"></i> بله'
        }
    },
    callback: function (result) {
        if (result) {
      window.location = href
    }
    }
});
        });

// onclick="popitup(this)"
function popitup(obj) {
    url=obj.getAttribute("href")
    newwindow=window.open(url,'{{title}}','height=200,width=150');
    if (window.focus) {newwindow.focus()}
    return false;
}

$('testmodal').click(function(){   //bind handlers
   var url = $(this).attr('href');
   showDialog(url);

   return false;
});

$("#targetDiv").dialog({  //create dialog, but keep it closed
   autoOpen: false,
   height: 300,
   width: 350,
   modal: true
});

function showDialog(url){  //load content and open dialog
    $("#targetDiv").load(url);
    $("#targetDiv").dialog("open");
}
