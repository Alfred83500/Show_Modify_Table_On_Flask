#Simple CSV Based CRUD Web app


#Package
from flask import Flask
from flask import render_template
from flask import request
import csv
import pandas as pd
from google.cloud import storage


# create web app's instance
app = Flask('__name__')




project_id = "silver-nova-360910"
bucket = 'vegastore'
exportBucket = storage.Client(project=project_id).get_bucket(bucket)
chunk = pd.read_csv(f'gs://vegastore/Stock/mainData.csv', sep=',', encoding = 'ANSI')
chunk = chunk.applymap(lambda s: s.upper() if type(s) == str else s)
chunk["edit"] = pd.NA
chunk = chunk.sort_values(by='Ref_PRD', ascending=False).head(30)




@app.route('/')
def home():
    return render_template('home.html',column_names=chunk.columns.values, row_data=list(chunk.values.tolist()),
                           link_column="edit", zip=zip)

@app.route('/create')
def create():
    return render_template('create.html')

#read data from CSV
@app.route('/update')
def read():
    #read data
    # with open("mainData.csv") as f:
    #     reader = csv.DictReader(f)
    return render_template("update.html", column_names=chunk.columns.values, row_data=list(chunk.values.tolist()),
                           link_column="edit", zip=zip)






# @app.route('/form')
# def my_form():
#     return render_template('form.html')

# @app.route('/form', methods=['POST'])
# def my_form_post():
#     text = request.form(['text'])
#     processed_text = text.upper()
#     return processed_text


# run HTTP server
if __name__ == '__main__':
    app.run(debug=True, threaded=True) 