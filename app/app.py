from flask import Flask, render_template
import pandas as pd
from sklearn.externals import joblib

# initialize app
app = Flask(__name__)

# load classifier model
# with open('../model_output/model.sav', 'rb') as f:
    # model = joblib.load(f)

# load default features
feats = pd.read_csv('default_feats.csv')

# load input feature options
with open('input_options.sav', 'rb') as f:
    input_options = joblib.load(f)
# separate numerical limits form input_options
suff_lim = input_options['Sufficiency Rating']
del input_options['Sufficiency Rating']

@app.route('/')
def features():

    return render_template(
        'content.html',
        input_options=input_options,
        suff_lim=suff_lim
        )

if __name__ == '__main__':
    app.run(debug=True)
