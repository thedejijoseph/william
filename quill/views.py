
from uuid import uuid4

from django.core import exceptions
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view

from .models import QuillNote
from .utils import *

def index(request):
    if request.method == 'GET':
        return render(
            request,
            'quill/index.html',
            {'all': QuillNote.objects.all()}
        )

def editor(request):
    if request.method == 'GET':
        note_id = request.GET.get('note_id', "")
        try:
            QuillNote.objects.get(note_id=note_id)
            valid_note = True
        except:
            valid_note = False
        context = {
            'note_id': note_id,
            'valid_note': valid_note
        }
        return render(request, 'quill/editor.html', context)

def view_note(request, note_id):
    if request.method == 'GET':
        try:
            note = QuillNote.objects.get(note_id=note_id)
            delta = note.quill_delta
            from django.utils.safestring import mark_safe
            safe_delta = mark_safe(delta)
            print(delta, '\n\n', (safe_delta))
            return render(request, 'quill/note.html', context={'note': note, "safe": safe_delta})
        except:
            # raise
            return HttpResponse('Invalid Note ID')

@api_view(['POST'])
def update_note(request):
    payload = request.POST
    try:
        note = QuillNote.objects.get(note_id=payload.get('note_id'))
        note.title = payload.get('title')
        note.quill_delta = payload.get('quill_delta')
        note.raw_text = payload.get('raw_text')
        note.save()
        response = make_response(True, 'Updated note', {'note_id': note.note_id})
        return JsonResponse(response)
    except exceptions.ValidationError:
        note = QuillNote.objects.create(
            title=payload.get('title'),
            quill_delta=payload.get('quill_delta'),
            raw_text=payload.get('raw_text'),
            note_id=uuid4()
        )
        note.save()
        response = make_response(True, 'Saved note', {'note_id': note.note_id})
        return JsonResponse(response)
    except:
        raise

@api_view(['GET'])
def fetch_note(request):
    try:
        note_id = request.GET.get('note_id')
        note = QuillNote.objects.get(note_id=note_id)
        data = {
            'title': note.title,
            'quill_delta': note.quill_delta,
            'raw_text': note.raw_text,
            'note_id': note.note_id
        }
        response = make_response(True, 'Here is your note', data)
        return JsonResponse(response)
    except:
        raise