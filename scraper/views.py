from django.shortcuts import render
import csv
from django.http import HttpResponse
from .models import ScrapedData

def scrape_data(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        html = ScrapedData.objects.get(url=url).html
        data = html.strip()

        # Save the data to a CSV file
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'
        writer = csv.writer(response)
        writer.writerow(data)

        return response
    
def home(request):
    if request.method == 'POST':
        # Handle the form submission and scrape the data
        pass
    return render(request, 'scraper/home.html')
