import os
PROJECT = 'buoyant-yew-223720' # REPLACE WITH YOUR PROJECT ID
BUCKET = 'buoyant-yew-223720' # REPLACE WITH YOUR BUCKET NAME
REGION = 'europe-west4' # REPLACE WITH YOUR BUCKET REGION e.g. us-central1
MODEL_TYPE='cnn'  # 'linear', 'dnn', 'dnn_dropout', or 'cnn'

# do not change these
os.environ['PROJECT'] = PROJECT
os.environ['BUCKET'] = BUCKET
os.environ['REGION'] = REGION
os.environ['MODEL_TYPE'] = MODEL_TYPE
os.environ['TFVERSION'] = '1.8'  # Tensorflow version



