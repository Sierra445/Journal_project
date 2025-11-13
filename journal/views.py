from django.shortcuts import render, redirect
from .models import JournalEntry
from .forms import JournalEntryForm

def home(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JournalEntryForm()

    entries = JournalEntry.objects.order_by('-date_created')
    return render(request, 'journal/home.html', {'form': form, 'entries': entries})

def book_a_session(request):
    if request.method == 'POST':
        form = SessionBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'journal/session_success.html')
    else:
        form = SessionBookingForm()
    return render(request, 'journal/book_a_session.html', {'form': form})
