from django.shortcuts import render

# Create your views here.
from langdetect import detect
from .NNModel import predict_sentence
from django.http import HttpResponse
from .models import Prediction
from django.template import loader

#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    prediction = {}
    if request.POST:
        text = request.POST['text']
        google_d = detect(text)
        model_d = predict_sentence(text)
        prediction = {
            'model_d': model_d,
            'google_d': google_d,
            'text': text }

        p = Prediction.create(text, model_d, google_d)
        p.save()

    list = Prediction.objects.order_by('-date')[:5]
    template = loader.get_template('predict/index.html')
    context = {
        'predictions_list': list,
        'prediction': prediction,
    }
    return HttpResponse(template.render(context, request))