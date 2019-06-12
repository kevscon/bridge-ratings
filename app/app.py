from flask import Flask, render_template, request
import pandas as pd
import json
from sklearn.externals import joblib

# initialize app
app = Flask(__name__)

# load classifier model
with open('../model_output/model.sav', 'rb') as f:
    model = joblib.load(f)

# load feature options for app input
with open('input_options.json', 'r') as f:
    input_options = json.load(f)
# separate numerical limits from input_options
suff_lim = input_options['Sufficiency Rating']
del input_options['Sufficiency Rating']

# load blank input series
input_series = pd.read_json('input_series.json', typ='series')
# load numerical default values
num_feat = pd.read_json('num_def.json', typ='series')


cat_items = [
    'FUNCTIONAL_CLASS_026',
    'HISTORY_037',
    'OPEN_CLOSED_POSTED_041',
    'SERVICE_UND_042B',
    'STRUCTURE_KIND_043A',
    'SUPERSTRUCTURE_COND_059',
    'DECK_STRUCTURE_TYPE_107',
    'SURFACE_TYPE_108A',
    'MEMBRANE_TYPE_108B',
    'DECK_PROTECTION_108C'
]

@app.route('/')
def features():

    return render_template(
        'content.html',
        input_options=input_options,
        suff_lim=suff_lim
        )

@app.route('/', methods=['POST'])
def post_it():

    # load categorical default values
    cat_feat = pd.read_json('cat_def.json', typ='series')

    # create categorical input list
    cat_inputs = []
    # read categorical input from app and store in dictionary
    for feature in input_options.keys():
        # retrieve value for each feature on app
        cat_inputs.append(request.form[feature])
    # convert categorical string input to code values
    cat_input = pd.Series([input_options[i][j] for i, j in zip(list(input_options.keys()), cat_inputs)], index=cat_items)
    # override default categorical values with app input
    cat_feat[cat_input.index] = cat_input
    # encode categorical values
    cat_feat = pd.Series(1, index=pd.get_dummies(pd.DataFrame(cat_feat).T).columns)
    # override blank input series
    input_series[cat_feat.index] = cat_feat

    # read numerical input from app
    num_input = request.form['suf_rt']
    # override default numerical values with app input
    num_feat['SUFFICIENCY_RATING_feat_yr'] = num_input
    # override blank input series
    input_series[num_feat.index] = num_feat

    # output
    # with open('feat_out.json', 'w') as outfile:
    #     json.dump(cat_feat, outfile)

    prediction = model.predict([input_series])[0]


    return render_template(
        'output.html',
        prediction=prediction
        )



if __name__ == '__main__':
    app.run(debug=True)
