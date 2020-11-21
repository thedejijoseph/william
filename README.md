## William

I'm working on a blogging app and need to experiment with, beforehand, frontend text editing libraries.

Experimenting with:

+   QuillJS [/quill-notes](/quill-notes)
+   Editor.js [/editorjs-notes](/editorjs-notes)
+   TinyMCE [/tiny-notes](/tiny-notes)

## Notes

`Important!` Sanitization needs to be done for all editors, frontend and backend.

Experiments so far has shown interoperability for data export and import format. How data will be exported, cleaned*, saved, displayed and re-imported into the editor to continue writing.

Features needed:

| Editor   | Editor Format |  Export format |   Images   | Code highlighting | Load time |
|----------|:-------------:|:--------------:|:----------:|:-----------------:|:---------:|
| Quill JS | Single page   | Annotated JSON | Not tested |     Not tested    |           |
| EditorJS | Block-based   |                | Not tested |     Not tested    |           |
| TinyMCE  |               |                |            |                   | Very slow |

___

### Quill

+ Simple to set up and use, not without customization.
+ Editor is a single "sheet", not "block-based" like Editor.js.
+ Export format is reusable: annotated JSON.

### Editor.js

+ Disntictively customisable. If I was looking for what to customise to my exact specifications, Editor.js will be it. The writing (input) and display (output) process both.
+ Asynchronous events. Those could really come in handy in an SPA.

### TinyMCE
+ Um, shitty load time, too-tight connection to the for-profit company (I saw some detached, open-source stuff; tied to Django though)  

