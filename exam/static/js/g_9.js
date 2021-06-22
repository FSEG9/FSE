$(function() {
    "use strict";
    $(document).on('click', '.done-btn', function () {
        var $item = $(this).parent().parent().parent();
        var $this = $(this);

        if ($item.data('chosen')) {
            $.ajax({
                type: 'PATCH',
                url: $this.data('href'),
                success: function (data) {
                    $item.data('chosen', false);
                    M.toast({html: data.message});
                }
            })
        } else {
            $.ajax({
                type: 'PATCH',
                url: $this.data('href'),
                success: function (data) {
                    $item.data('chosen', true);
                    M.toast({html: data.message});
                }
            })
        }
    });

    $(document).on('click', '.Mydelete', function () {
        var $item = $(this).parent().parent().parent();
        var $this = $(this);

            $.ajax({
                type: 'PATCH',
                url: $this.data('href'),
                success: function (data) {
                    $item.data('chosen', false);
                    M.toast({html: data.message});
                }
            })

    });
})
