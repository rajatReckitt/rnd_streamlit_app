GCLOUD DEPLOY IN CLOUD RUN 

gcloud run deploy --image gcr.io/project_name/rnd_streamlit_test --region=europe-west2 --platform managed --project=project_name --allow-unauthenticated 

gcloud builds submit --tag gcr.io/[PROJECT_ID]/[IMAGE_NAME]:[TAG]
