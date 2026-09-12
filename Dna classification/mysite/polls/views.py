from django.shortcuts import render, redirect
import pandas as pd
from .sustain import model
import pickle


# Create your views here.
def handler(request):
    response = None
    if request.method == 'POST':
        genome = request.POST['Name'].strip()  # Remove whitespace
        if len(genome) != 57:
            # Handle incorrect sequence length
            return render(request, "index.html", {
                'response': 'invalid_length',
                'sequence_length': len(genome),
                'entered_sequence': genome
            })
        
        genome_list = list(genome)
        df_test = pd.DataFrame(genome_list)
        result = predicting(df_test.transpose())
        if result[0] == 1:
            response = True
        else:
            response = False
    return render(request, "index.html", {'response': response})

def predicting(data):
    try:
        # Loading Neural Network from disk.
        encoder = pickle.load(open("polls/EColi-encoder.pickle", 'rb'))
        data_test = encoder.transform(data).toarray()
        result = model.predict(data_test)
        return result
    except AttributeError as e:
        if '_infrequent_enabled' in str(e):
            # Handle sklearn version compatibility issue
            # Try to create a new encoder with current sklearn version
            from sklearn.preprocessing import OneHotEncoder
            import numpy as np
            
            # Load the old encoder to get categories
            old_encoder = pickle.load(open("polls/EColi-encoder.pickle", 'rb'))
            categories = old_encoder.categories_
            
            # Create new encoder with current sklearn version
            new_encoder = OneHotEncoder(categories=categories, handle_unknown='ignore')
            
            # Create proper dummy data that matches the expected shape
            # Each feature (column) should have its own category array
            dummy_data = []
            for i, cat_array in enumerate(categories):
                # Take first category from each feature
                dummy_data.append([cat_array[0]])
            
            dummy_data = np.array(dummy_data).T  # Transpose to get correct shape
            new_encoder.fit(dummy_data)
            
            # Transform the actual data
            data_test = new_encoder.transform(data).toarray()
            result = model.predict(data_test)
            return result
        else:
            raise e