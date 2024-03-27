from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *
from django.urls import path
import re
import os
from django.conf import settings
from collections import Counter
# Create your views here.

def index(request):
    message = request.POST.get('message')
    
    check = True
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        uploaded_file = 'media/uploads/text.txt'
        if message:
            check = True
            with open('media/uploads/article.txt', 'w') as file:
                file.write(message + '\n')
        if form:
            check = False
            if form.is_valid():
                
                new_file = form.cleaned_data['text']
                if new_file:
                    new_file.name = 'text.txt'
                    upload_dir = 'media/'
                    if Textmod.objects.exists():
                        existing_textmod = Textmod.objects.first()
                        existing_file_path = os.path.join(upload_dir, str(existing_textmod.text))
                        try:
                            os.remove(existing_file_path)
                        except PermissionError as e:
                            return render(request, 'error.html', {'error_message': 'Permission denied to delete existing file.'})
                        existing_textmod.text = new_file
                        existing_textmod.save()
                        with open('media/uploads/text.txt', 'r') as source_file:
                            source_content = source_file.read()
                        
                        with open('media/uploads/article.txt', 'w') as destination_file:
                            destination_file.write(source_content)
                        
                    else:
                        Textmod.objects.create(text=new_file)
                
            else:
                context = {'form': form}
    else:
        
        form = MessageForm() # Path to your text file
        print("why")
    
    
    # Read the text file and count word occurrences
    # if check:
    #     file_path = 'media/uploads/article.txt'
    # else:
    #     file_path = 'media/uploads/text.txt'
    file_path = 'media/uploads/article.txt'
    word_count = Counter()
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = preprocess(word)
                if word:
                    word_count[word] += 1

    # Find the 100 most common words
    top_words = word_count.most_common(100)
    # with open('filename.txt', 'w') as file:
    #     pass 
    # name = Name.objects.all()

    # Output the top 100 frequent words
    # for word, count in top_words:
    #     print(f"{word}: {count}")
    context = {"topwords": top_words, 'form':form }
    return render(request, "index.html",  context)




def preprocess(word):
    # Remove non-alphabetic characters and convert to lowercase
    return re.sub(r'[^a-zA-Z]', '', word).lower()



if __name__ == "__index__":
    index()
