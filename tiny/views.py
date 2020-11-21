
from uuid import uuid4

from django.http import request
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view

from .models import TinyNote


def make_response(
    success: bool,
    message: str,
    data: dict = None,
    errors: list = None):

    if success:
        if not data:
            raise Exception("Successful response must have a payload")
        return {
            'success': True,
            'message': message,
            'data': data
        }
    if not success:
        if not errors:
            raise Exception("Failed response must have a list of errors")
        return {
            'success': False,
            'message': message,
            'errors': errors
        }


def index(request):
    all = TinyNote.objects.all()
    return render(request, 'tiny-notes/index.html', {'all': all})

def editor(request):
    note_id = request.GET.get('note-id', 'new-note')
    # content from existing notes are not properly loaded into tinymce editor
    # we'd have to wait for editor to finish loading. don't wanna do it, i'm bored
    # and won't be picking tinymce anyways..
    return render(request, 'tiny-notes/editor.html', {"note_id": note_id})

def view_note(request, note_id):
    return render(request, 'tiny-notes/note.html', {'note_id': note_id})

@api_view(['POST'])
def get_note(request):
    pass

@api_view(['POST'])
def save_note(request):
    try:
        note_id = request.POST['note-id']
        if note_id == "new-note":
            note = TinyNote.objects.create(
                title=request.POST['title'],
                content=request.POST['content'],
                public_id=uuid4()
            )
            note.save()
            resp = make_response(
                success=True,
                message='Saved successfully',
                data={"note_id": note.public_id}
            )
            return JsonResponse(resp)
        print(">>>", note_id)
        note = TinyNote.objects.get(public_id=note_id)
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        resp = make_response(
            success=True,
            message='Updated successfully',
            data={"note_id": note.public_id}
        )
        return JsonResponse(resp)
    except:
        raise
        resp = make_response(
            success=False,
            message='Some error has occurred',
            errors=[{"message": "Some error has occurred"}]
        )
        return JsonResponse(resp)

@api_view(['POST'])
def load_note(request):
    try:
        note_id = request.POST['note-id']
        note = TinyNote.objects.get(public_id=note_id)
        resp = make_response(True, 'Note loaded successfully', {
            "note_id": note.public_id,
            "title": note.title,
            "content": note.content
        })
        return JsonResponse(resp)
    except:
        resp = make_response(
            success=False, 
            message='Some error has occured', 
            errors=[{"message": "Some error has occured"}]
            )
        return JsonResponse(resp)
