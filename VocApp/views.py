from django.shortcuts import render,redirect
from voiceDB.forms import VocabDB_Form, Bulk_form
from voiceDB.models import VocabDB
from .settings import MEDIA_URL
from django.core.files.base import ContentFile
from .utils import preprocess_text, count_most_repeated_words, count_most_repeated_phrases
from django.urls import reverse
from django.forms import formset_factory

from gtts import gTTS
import os

### Utils ###

def ttt(text):
    # text to title of audio file
    return None


# Views

def index_voc(request):

    audio_data = VocabDB.objects.all()
    return render(request, 'home.html', {'audio_data': audio_data})

###### Add individual vocabulary ########
def addVocab(request):

    if request.method == 'POST':
        print(request.POST)
        form = VocabDB_Form(request.POST)
        print(form)


        if form.is_valid():
            #### Creating Audio files #####
            text = form.cleaned_data['French']
            myobj = gTTS(text= text, lang = 'fr', slow = False )
            audio_url= '.' + MEDIA_URL + 'audio_files/' + text.lower() + '.mp3'
            myobj.save(audio_url)
            
                
            ## save to database

            instance = VocabDB(French=form.cleaned_data['French'],Spanish=form.cleaned_data['Spanish'],Example=form.cleaned_data['Example'], learning_rate= 0, audio_file=audio_url)
            instance.save()

            return redirect('indexVoc')
    else:
        form = VocabDB_Form()
        instance = ""

    return render(request, 'AddVocab.html', {'form': form, 'instance': instance})


###### Add vocabulary with bulk request ############
def bulk(request):
    
    if request.method == 'POST':
        
        if 'form1' in request.POST:
            
            form1 = Bulk_form(request.POST)
            print(request.POST)
            print(form1)

            if form1.is_valid():
                
                text = form1.cleaned_data['text']

                most_common_words = count_most_repeated_words(text)
                most_common_phrases = count_most_repeated_phrases(text, 5)

                VocFormSet = formset_factory(VocabDB_Form, extra=0)
                form2 = VocFormSet(initial=[{'French': word} for word, count in most_common_words])
                

                return render(request, 'bulk.html', {'form1': form1, 'form2': form2})
        else:
            VocFormSet = formset_factory(VocabDB_Form)
            form2 = VocFormSet(request.POST)
            # print(request.POST)
            # print(form2)
            if form2.is_valid():
                # Save each form's data as a new model instance
                for eform in form2:
                    # print(eform)
                    text = eform.cleaned_data['French']
                    myobj = gTTS(text= text, lang = 'fr', slow = False )
                    audio_url= '.' + MEDIA_URL + 'audio_files/' + text.lower() + '.mp3'
                    myobj.save(audio_url)
                    instance = VocabDB(French=eform.cleaned_data['French'],Spanish=eform.cleaned_data['Spanish'],Example=eform.cleaned_data['Example'], learning_rate= 0, audio_file=audio_url)
                    instance.save()
                    
                return redirect('indexVoc')
    
    print("else")
    form1 = Bulk_form()
    
    print(request.method)
    
    return render(request, 'bulk.html', {'form1': form1, 'form2': None})

# def bulkPOST(request):
#     form = VocFormSet(request.POST)
#     print(request.POST)
#     print(form)
#     if form.is_valid():
#         # Save each form's data as a new model instance
#         for eform in form:
#             print(eform)
#             eform.save()
#         return redirect('indexVoc')
    
#     return render(request, 'bulkPOST.html', {'form': form})