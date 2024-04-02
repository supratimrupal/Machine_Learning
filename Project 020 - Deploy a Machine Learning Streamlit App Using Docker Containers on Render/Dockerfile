FROM python:3.9
COPY . multiple_disease_prediction_web_app/
WORKDIR multiple_disease_prediction_web_app/
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD streamlit run multiple_disease_prediction_web_app.py
