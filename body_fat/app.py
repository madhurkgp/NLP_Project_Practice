from flask import Flask, request, render_template
import pickle
import os

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'bodyfatmodel_new.pkl')
with open(model_path, 'rb') as file1:
    rf = pickle.load(file1)


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        my_dict = request.form

        # Validate input
        try:
            density = float(my_dict['density'])
            abdomen = float(my_dict['abdomen'])
            chest = float(my_dict['chest'])
            weight = float(my_dict['weight'])
            hip = float(my_dict['hip'])
        except ValueError:
            return render_template('show_clean.html', string='Error: Please enter valid numeric values!')
        
        input_features = [[density, abdomen, chest, weight, hip]]
        prediction = rf.predict(input_features)[0].round(2)
        string = f'Percentage of Body Fat Estimated is: {prediction}%'

        return render_template('show_clean.html', string=string)

    return render_template('home_clean.html')


if __name__ == "__main__":
    app.run(debug=True)
