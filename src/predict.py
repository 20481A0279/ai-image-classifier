import sys
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def predict_image(img_path, model_path='model.h5'):
    """
    Predict whether an image is AI-generated or real.
    """
    model = load_model(model_path)
    
    # Load and preprocess image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    
    # Make prediction
    prediction = model.predict(img_array)[0][0]
    
    if prediction > 0.5:
        result = "🤖 AI-Generated"
    else:
        result = "📸 Real Photograph"
    
    print(f"Prediction: {result} (Confidence: {prediction:.4f})")
    return result

if _name_ == "_main_":
    if len(sys.argv) > 1:
        predict_image(sys.argv[1])
    else:
        print("Usage: python src/predict.py <path_to_image>")
        print("Example: python src/predict.py test_image.jpg")
