from django.shortcuts import render, redirect
from .models import Name
import json
from django import forms


class InputForm(forms.Form):
    name0 = forms.CharField(label='name0', max_length=50)


def handle_index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            # Take data from the initial form
            name_input = form.cleaned_data['name0']
            # Convert to json type
            data = json.dumps(name_input, ensure_ascii=False)
            # Create object
            Name.objects.create(data=data, name='name0')

            # Loop take data from other form
            for count in range(1, len(request.POST) - 1):
                query = f'name{count}'
                input_value = request.POST[query]
                # Check for empty field
                if input_value:
                    data = json.dumps(input_value, ensure_ascii=False)
                    field = json.dumps(query)
                    Name.objects.create(data=data, name=field)
                count += 1
        return redirect('/show/')
    else:
        form = InputForm()
    return render(request, 'app/index.html', {'form': form})


def handle_view(request):
    # Take data from the db
    query = Name.objects.all().values('id', 'name', 'data')
    json_data = list(query)
    return render(request, 'app/view.html', {'json_list': json_data})
