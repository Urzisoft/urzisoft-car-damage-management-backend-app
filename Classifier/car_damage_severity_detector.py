import os

from django.core.cache import cache
import cv2
import joblib


def car_damage_severity_detector(image_source):
    classifier_classes = {0: 'minor', 1: 'moderate', 2: 'severe'}
    model_cache_key = 'model_cache'
    model = cache.get(model_cache_key)
    model_rel_path = 'Classifier/model_cache/cache.pkl'

    print(model)

    if model is None:
        model_path = os.path.realpath(model_rel_path)
        model = joblib.load(model_path)
        cache.set(model_cache_key, model, None)

    img = cv2.imread(image_source, 0)
    img_resized = cv2.resize(img, (450, 450))
    img_resized = img_resized.reshape(1, -1) / 255
    path = model.predict(img_resized)

    return classifier_classes[path[0]]
