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