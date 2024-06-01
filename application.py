from flask import Flask,request,render_template,jsonify
from src.pipelines.prediction import Customdata,Predictpipeline
from src.logger import logging
from src.exception import CustomException

application = Flask(__name__)
app = application


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict_datapoint():
    if request.method =='GET':
        logging.info('got get')
        return render_template('form_1.html')
    
    else:
        data = Customdata(
            gender = request.form.get('gender'),
            race_ethnicity = request.form.get('race_ethnicity'),
            parental_level_of_education = request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = float(request.form.get('reading_score')),
            writing_score = float(request.form.get('writing_score'))
        )
       

        convert_data = data.intodf()
        result = Predictpipeline().predictdata(convert_data)

        return render_template('form_1.html',final_result = result)


if __name__=='__main__':
    app.run(host = "0.0.0.0",port=5590)