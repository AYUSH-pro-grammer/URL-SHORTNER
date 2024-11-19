from django.http import HttpResponseRedirect, HttpResponse


from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.http import JsonResponse
import random
import string
from urlShort.models import Urls

# Function to generate a random string
def generate_random_string(length=4):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# View to handle URL shortening
def index(request):
    if request.method == 'POST':
        url = request.POST.get('url') 
        decoded = generate_random_string()  

        new_urls = Urls(url=url, decoded=decoded)
        new_urls.save()

        return render(request, 'index.html', {'decode': decoded})

    return render(request, 'index.html')

def redirect_to_original(request, decode):
    try:
        url_entry = get_object_or_404(Urls, decoded=decode)
        original_url = url_entry.url 

        print(original_url)
        html = f"""<!DOCTYPE html>




<html>
    <head>
        <script>
            // Automatically open the URL in a new tab
            window.onload = function() {{
                window.open("https://{original_url}");
            }};
        </script>
    </head>
    <body>
        <p>The URL is opening in a new tab. If not, click <a href="{original_url}" target="_blank">here</a>.</p>
    </body>
</html>
"""
        return HttpResponse(html)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

