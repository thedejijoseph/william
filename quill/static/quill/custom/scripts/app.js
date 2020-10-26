
// initialize quill js

var quill = new Quill('#editor', {
theme: 'snow'
});

save = function(){
    let payload = {
        title: $('#note-title').val(),
        note_id: $('#note-id').val(),
        quill_delta: JSON.stringify(quill.getContents()),
        raw_text: quill.root.innerHTML
    }

    $.ajax({
        url: '/quill-notes/api/update',
        method: 'POST',
        data: payload,
        success: function(resp, status){
            let feedback = $('#feedback')
            if (resp.success){
                feedback.html(resp.message)
                $('#note-id').val(resp.data.note_id)
            }
            else{
                feedback.html(resp.errors[0].message)
            }
        }
    })
}

if ($('#valid').val() == 'true'){
    $.ajax({
        method: 'GET',
        url: '/quill-notes/api/fetch',
        data: {note_id: $('#note-id').val()},
        success: function(resp){
            $('#note-title').val(resp.data.title)
            quill.setContents(JSON.parse(resp.data.quill_delta))
        }
    })
}

$('#save-btn').click(save)
