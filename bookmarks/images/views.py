from django.shortcuts import render, redirect
from images.forms import ImageCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST)
        # cd = form.cleaned_data
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image added successfully')
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm(request.GET)
    return render(request, 'images/image/create.html', {'form': form, 'section': 'images'})
