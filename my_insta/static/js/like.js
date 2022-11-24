window.addEventListener('load', function() {


    $('#btn-to-like').on('click', function (evt) {
        const pk = $('button[data-pk]').data('pk')
        evt.preventDefault()


        $('#form-to-like').remove()
        likeForm = $('#form-to-like[data-pk]')
        likeForm.hide()

        disForm = $('#form-to-dislike[data-pk]')
        disForm.show()


        let url = 'http://localhost:8000/posts/';
        $.ajax({
            type: 'POST',
            url : url + `${pk}/like/`,
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action:'post',
            },
            success: function(data) {

                alert(`Лайк  ${pk} добавлен!`)
            }
        })
    })



    $('#btn-to-dislike').on('click', function (evt) {
        const pk = $('button[data-pk]').data('pk')
        evt.preventDefault()


        $('#form-to-dislike').remove()
        dislikeForm = $('#form-to-dislike[data-pk]')
        dislikeForm.hide()

        likeForm = $('#form-to-like[data-pk]')
        console.log(likeForm)
        likeForm.show()


        let url = 'http://localhost:8000/posts/';
        $.ajax({
            type: 'POST',
            url : url + `${pk}/like/`,
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action:'post',
            },
            success: function(data) {

                alert(`Лайк  ${pk} удалён!`)
            }
        })
    })



    $('#btn-to-like-2').on('click', function (evt) {
        const pk = $('button[data-pk]').data('pk')
        evt.preventDefault()


        $('#form-to-like').remove()
        likeForm = $('#form-to-like-2[data-pk]')
        likeForm.hide()

        disForm = $('#form-to-dislike[data-pk]')
        console.log(disForm)
        disForm.show()


        let url = 'http://localhost:8000/posts/';
        $.ajax({
            type: 'POST',
            url : url + `${pk}/like/`,
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action:'post',
            },
            success: function(data) {

                alert(`Лайк  ${pk} добавлен!`)
            }
        })
    })



})