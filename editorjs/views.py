from uuid import uuid4
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view

from quill.utils import make_response

from .models import EditorNote

def index(request):
    notes = EditorNote.objects.all()
    context = {'all': notes}
    return render(request, 'editorjs/index.html', context)

def editor(request):
    note_id = request.GET.get('note_id', '')
    try:
        note = EditorNote.objects.get(note_id=note_id)
    except:
        note = None
    return render(request, 'editorjs/editor.html', {'note': note})

def view_note(request, note_id):
    try:
        note = EditorNote.objects.get(note_id=note_id)
    except:
        note = None
    return render(request, 'editorjs/note.html', {"note": note})

@api_view(["POST"])
def update_note(request):
    data = request.POST
    try:
        note_id = data.get('note_id')
        note = EditorNote.objects.get(note_id=note_id)
        note.title = data.get('title')
        note.raw_data = data.get('raw_data')
        note.save()
        response = make_response(True, 'Update note', {'note_id': note.note_id})
        return JsonResponse(response)
    except:
        note = EditorNote.objects.create(
            title=data.get('title'),
            raw_data=data.get('raw_data'),
            note_id=uuid4()
        )
        note.save()
        response = make_response(True, 'Saved note', {'note_id': note.note_id})
        return JsonResponse(response)

@api_view(['GET'])
def fetch_note(request):
    note_id = request.GET.get('note_id', '')
    try:
        note = EditorNote.objects.get(note_id=note_id)
        data = {
            "title": note.title,
            "raw_data": note.raw_data,
            "note_id": note.note_id
        }
        response = make_response(True, "Fetched", data)
        return JsonResponse(response)
    except:
        response = make_response(False, "Failed to fetch", errors=[{"message": "Failed to fetch"}])
        return JsonResponse(response)
