from django.shortcuts import render, redirect
from . import final
import traceback

# Create your views here.
def sentiment(request):
    res = ""
    
    if request.method == 'POST':
        if 'pred_button' in request.POST:
            text_data = request.POST.get('text_data', '')
            
            if text_data and text_data.strip():
                try:
                    res = final.pre(str(text_data))
                except Exception as e:
                    print(f"Error in analysis: {e}")
                    res = f"Error occurred during analysis: {str(e)}"
            else:
                res = "Please enter some text to analyze."
        else:
            return redirect('homepage')
    
    return render(request, "first.html", {'result': res})