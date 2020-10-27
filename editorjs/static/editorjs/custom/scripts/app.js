
const editor = new EditorJS({
    holder: "editor",
    tools: {
        header: {
            class: Header,
            inlineToolBar: ["link"]
        },
        list: {
            class: List,
            inlineToolBar: true
        }
    }
});

let save = (output) => {
    let payload = {
        "title": $("#title").val(),
        "note_id": $("#note-id").val(),
        "raw_data": JSON.stringify(output)
    };
    $.ajax({
        "url": "/editorjs-notes/api/update",
        "method": "POST",
        "data": payload,
        "success": (resp, status) => {
            let feedback = $("#feedback");
            if (resp.success) {
                feedback.text(resp.message);
                $("#note-id").val(resp.data.note_id);
            }
        }
    });
};

$("#save").click(
    () => {
        editor.save().then(
            (output) => {save(output);}
        );
    }
);


// if note-id exists when the page loads, fetch its content and show
$.ajax({
    "url": "/editorjs-notes/api/fetch",
    "method": "GET",
    "data": {
        "note_id": $("#note-id").val()
    },
    "success": (resp) => {
        if (resp.success){
            $("#title").val(resp.data.title);
            // set blocks into editor
            let rawData = JSON.parse(resp.data.raw_data);
            editor.isReady.then(() => {
                editor.blocks.render(rawData);
            });
        }
    }
});
