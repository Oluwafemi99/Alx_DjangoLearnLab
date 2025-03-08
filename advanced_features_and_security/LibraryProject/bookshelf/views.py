from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import ExampleForm
# Create your views here.


@permission_required("bookshelf.can_edit", raise_exception=True)
def book_list(request):
    all_books = Book.objects.all()
    response = render(request, "bookshelf/book_list.html", {"all_books": all_books})
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://trustedscripts.example.com; style-src 'self' https://trustedstyles.example.com"
    return response


def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
            return redirect('success_url')  # Replace 'success_url' with your success URL
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/example_form.html', {'form': form})
