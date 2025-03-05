#Atharva created this file

from django.http import HttpResponse
from django.shortcuts import render
import string


def home(request):
    # Renders the home page (index.html)
    return render(request, 'index.html')


def analyze(request):
    # Get the text input from the user
    user_text = request.POST.get('text', 'default')

    # Get the selected text processing options
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    capall = request.POST.get('capall', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Store processed text
    processed_text = user_text

    # Dictionary to store the purpose and result
    parameters = {}

    # Remove Punctuations
    if removepunc == 'on':
        processed_text = ''.join(char for char in processed_text if char not in string.punctuation)
        parameters['purpose'] = 'Removing Punctuations'
        parameters['string'] = processed_text

    # Capitalize the first letter
    if capfirst == 'on':
        processed_text = processed_text.capitalize()
        parameters['purpose'] = 'Capitalizing First Letter'
        parameters['string'] = processed_text

    # Capitalize all letters
    if capall == 'on':
        processed_text = processed_text.upper()
        parameters['purpose'] = 'Capitalizing All Letters'
        parameters['string'] = processed_text

    # Remove new lines
    if newlineremove == 'on':
        processed_text = processed_text.replace("\n", "").replace("\r", "")
        parameters['purpose'] = 'Removing New Lines'
        parameters['string'] = processed_text

    # Remove extra spaces
    if spaceremove == 'on':
        processed_text = ' '.join(processed_text.split())  # Removes extra spaces
        parameters['purpose'] = 'Removing Extra Spaces'
        parameters['string'] = processed_text

    # Count characters
    if charcount == 'on':
        char_count = len(processed_text)
        parameters['purpose'] = 'Counting Number of Characters'
        parameters['string'] = char_count

    # If no options are selected, return an error message
    if all(option == 'off' for option in [removepunc, capfirst, capall, newlineremove, spaceremove, charcount]):
        return HttpResponse("Error: No Utility Selected")

    # Render the result on analyze.html
    return render(request, 'analyze.html', parameters)
