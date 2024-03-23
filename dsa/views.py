from django.shortcuts import render
from .models import *
from django.urls import path
import re
import os
from django.conf import settings
from collections import Counter
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        # file_path = os.path.join(settings.BASE_DIR, 'uploads/article.txt')
        file_path = os.path.join(settings.BASE_DIR, 'uploads/article.txt')
        # message = form.cleaned_data['message']
        # message = request.POST.get('message', '')
        # uploaded_file = request.FILES.get('file')

        # if form.is_valid():
        # message = form.cleaned_data.get('message', '')
        message = request.POST.get('message')
        uploaded_file = request.FILES.get('file')
        file_path = os.path.join(settings.BASE_DIR, 'uploads/article.txt')
        if message:
            # message = form.cleaned_data['message']
            with open(os.path.join(settings.BASE_DIR, 'uploads/article.txt'), 'w') as file:
                file.write(message + '\n')
        elif uploaded_file:
            file_content = uploaded_file.read().decode('utf-8')
            with open(os.path.join(settings.BASE_DIR, 'uploads/article.txt'), 'w') as file:
                file.write(file_content)
    else:
        form = MessageForm() # Path to your text file

    # Read the text file and count word occurrences
    file_path = os.path.join(settings.BASE_DIR, 'uploads/article.txt')
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
    name = Name.objects.all()

    # Output the top 100 frequent words
    # for word, count in top_words:
    #     print(f"{word}: {count}")
    context = {"topwords": top_words, "name": name}
    return render(request, "index.html",  context)




def preprocess(word):
    # Remove non-alphabetic characters and convert to lowercase
    return re.sub(r'[^a-zA-Z]', '', word).lower()

# def main():
#     file_path = "article.txt"  # Path to your text file

#     # Read the text file and count word occurrences
#     word_count = Counter()
#     with open(file_path, 'r') as file:
#         for line in file:
#             words = line.split()
#             for word in words:
#                 word = preprocess(word)
#                 if word:
#                     word_count[word] += 1

#     # Find the 100 most common words
#     top_words = word_count.most_common(100)

#     # Output the top 100 frequent words
#     for word, count in top_words:
#         print(f"{word}: {count}")

if __name__ == "__index__":
    index()
