from django.shortcuts import render, redirect
from tensorflow.keras.models import load_model
import numpy as np
import os
from .improved_model import hybrid_predict

# Create your views here.
def handler(request):
    result = None
    method = None
    confidence = None
    
    if request.method == 'POST':
        sequence = request.POST.get('Name', '')
        if sequence.strip():
            try:
                processed_seq = preprocessing(sequence)
                prediction, confidence, method = hybrid_predict(processed_seq.flatten().tolist())
                result = f"{prediction:.2f}"
            except Exception as e:
                result = f"Error: {str(e)}"
        else:
            result = "Please enter a sequence"
    
    context = {
        'response': result,
        'method': method,
        'confidence': confidence
    }
    return render(request, "index.html", context)

def preprocessing(s):
    try:
        # Handle different input formats
        s_ = s.strip('[]').split(',')
        s_ = [float(x.strip()) for x in s_ if x.strip()]
        if len(s_) < 2:
            raise ValueError(f"Expected at least 2 numbers, got {len(s_)}")
        
        # Use the last 7 numbers for prediction
        if len(s_) >= 7:
            s_final = s_[-7:]
        else:
            # If less than 7, pad with the first number
            padding_needed = 7 - len(s_)
            s_final = [s_[0]] * padding_needed + s_
        
        s_new = np.array(s_final)
        s_new = s_new.reshape((1, 7, 1))
        return s_new
    except Exception as e:
        raise ValueError(f"Invalid sequence format: {str(e)}. Use format: [90, 100, 110, 120, 130, 140, 150]")