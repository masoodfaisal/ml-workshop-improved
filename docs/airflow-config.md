# AirFlow Runtie Int Config
- airflow ui: http://app-aflow-airflow:8080
- api ep: https://api.github.com
- repo: airflow-dags/dags
- cloud: http://minio-ml-workshop:9000
- uid: minio
- storage bucket: airflow


# Runner config from ELyra
- python-runer: quay.io/ml-aml-workshop/airflow-python-runner:0.0.8
- spark-runer: quay.io/ml-aml-workshop/elyra-spark:0.0.4


# Payload to test the deployed model
https://raw.githubusercontent.com/masoodfaisal/ml-workshop/main/vegetta/payload.json
```json
{
  "data": {
      "names": [
          "gender",
          "SeniorCitizen",
          "Partner",
          "Dependents",
          "tenure",
          "PhoneService",
          "MultipleLines",
          "InternetService",
          "OnlineSecurity",
          "OnlineBackup",
          "DeviceProtection",
          "TechSupport",
          "StreamingTV",
          "StreamingMovies",
          "Contract",
          "PaperlessBilling",
          "PaymentMethod",
          "MonthlyCharges",
          "TotalCharges"
      ],
      "ndarray": [
          [
              "Female",
              0,
              "Yes",
              "Yes",
              1,
              "Yes",
              "Yes",
              "Fiber optic",
              "Yes",
              "Yes",
              "Yes",
              "No",
              "Yes",
              "Yes",
              "Month-to-month",
              "Yes",
              "Electronic check",
              100,
              80
          ]
      ]
  }
}
```
