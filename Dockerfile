FROM python:3.11.7-slim-bullseye
RUN apt-get update && apt-get install -y git-lfs
RUN git lfs install
WORKDIR /ml_star_vs_quasar
COPY ./app/server.py /ml_star_vs_quasar/
COPY ./app/model.py /ml_star_vs_quasar/
COPY ./app/requirements.txt /ml_star_vs_quasar/
COPY ./models/scaling.pkl /ml_star_vs_quasar/
COPY ./models/model_random_forest_classifier.pkl /ml_star_vs_quasar/
COPY ./app/templates /ml_star_vs_quasar/templates/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "./server.py"]
EXPOSE 5001