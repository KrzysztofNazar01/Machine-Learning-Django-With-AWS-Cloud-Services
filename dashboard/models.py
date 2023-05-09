import random

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib
import requests
import json
import re


class Data(models.Model):
    # name = models.CharField(max_length=100, null=True)
    # age = models.PositiveIntegerField(
    #     validators=[MinValueValidator(13), MaxValueValidator(19)], null=True)
    # height = models.PositiveIntegerField(null=True)
    # sex = models.PositiveIntegerField(choices=GENDER, null=True)
    # predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    id = models.IntegerField(primary_key=True)
    diagnosis = models.CharField(max_length=10)
    radius_mean = models.CharField(max_length=10)
    texture_mean = models.CharField(max_length=10)
    perimeter_mean = models.CharField(max_length=10)
    area_mean = models.CharField(max_length=10)
    smoothness_mean = models.CharField(max_length=10)
    compactness_mean = models.CharField(max_length=10)
    concavity_mean = models.CharField(max_length=10)
    concave_points_mean = models.CharField(max_length=10)
    points_mean = models.CharField(max_length=10)
    symmetry_mean = models.CharField(max_length=10)
    fractal_dimension_mean = models.CharField(max_length=10)
    radius_se = models.CharField(max_length=10)
    texture_se = models.CharField(max_length=10)
    perimeter_se = models.CharField(max_length=10)
    area_se = models.CharField(max_length=10)
    smoothness_se = models.CharField(max_length=10)
    compactness_se = models.CharField(max_length=10)
    concavity_se = models.CharField(max_length=10)
    concave_points_se = models.CharField(max_length=10)
    points_se = models.CharField(max_length=10)
    symmetry_se = models.CharField(max_length=10)
    fractal_dimension_se = models.CharField(max_length=10)
    radius_worst = models.CharField(max_length=10)
    texture_worst = models.CharField(max_length=10)
    perimeter_worst = models.CharField(max_length=10)
    area_worst = models.CharField(max_length=10)
    smoothness_worst = models.CharField(max_length=10)
    compactness_worst = models.CharField(max_length=10)
    concavity_worst = models.CharField(max_length=10)
    concave_points_worst = models.CharField(max_length=10)
    points_worst = models.CharField(max_length=10)
    symmetry_worst = models.CharField(max_length=10)
    fractal_dimension_worst = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        data_for_prediction = {
            "data":
                str(self.radius_mean) + ", " +
                str(self.texture_mean) + ", " +
                str(self.perimeter_mean) + ", " +
                str(self.area_mean) + ", " +
                str(self.smoothness_mean) + ", " +
                str(self.compactness_mean) + ", " +
                str(self.concavity_mean) + ", " +
                str(self.concave_points_mean) + ", " +
                str(self.symmetry_mean) + ", " +
                str(self.fractal_dimension_mean) + ", " +
                str(self.radius_se) + ", " +
                str(self.texture_se) + ", " +
                str(self.perimeter_se) + ", " +
                str(self.area_se) + ", " +
                str(self.smoothness_se) + ", " +
                str(self.compactness_se) + ", " +
                str(self.concavity_se) + ", " +
                str(self.concave_points_se) + ", " +
                str(self.symmetry_se) + ", " +
                str(self.fractal_dimension_se) + ", " +
                str(self.radius_worst) + ", " +
                str(self.texture_worst) + ", " +
                str(self.perimeter_worst) + ", " +
                str(self.area_worst) + ", " +
                str(self.smoothness_worst) + ", " +
                str(self.compactness_worst) + ", " +
                str(self.concavity_worst) + ", " +
                str(self.concave_points_worst) + ", " +
                str(self.symmetry_worst) + ", " +
                str(self.fractal_dimension_worst)
        }

        print(data_for_prediction)
        print(type(data_for_prediction))

        api_name = "api-ml-model"
        url_connect = "https://w7oa7rjyn0.execute-api.us-west-2.amazonaws.com/PROD/{}".format(api_name)
        request_result = requests.post(url_connect, data=json.dumps(data_for_prediction))

        self.diagnosis = str(request_result.content.decode("utf-8"))[1:2]
        print("request_result: " + str(request_result.content))
        self.id = random.randint(0, 10000)
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.id)
