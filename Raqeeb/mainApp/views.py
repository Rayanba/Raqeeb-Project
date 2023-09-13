from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

def main(request):
    return render(request, 'MainApp/index.html')


def dashboard(request):
    return render(request, 'MainApp/dashboard.html')


# def report(request, first=None, second=None):
#     first_person = first
#     second_person = second
#     context = {
#         'first_person': first_person,
#         'second_person': second_person
#     }
#     return render(request, 'MainApp/report.html', context)

# def upload(request):
#     if request.method == 'POST' and request.FILES['videoFile']:
#         first_person = request.POST.get('firstPerson')
#         second_person = request.POST.get('secondPerson')
#         video_file = request.FILES.get('videoFile')
#         destination_path = os.path.join(
#             r'C:\Users\Rayan\Desktop\Raqeeb\predictionApp\Detiction\TrafficLaneDetector\temp\vidForPred',
#             video_file.name)
#         with open(destination_path, 'wb+') as destination_file:
#             for chunk in video_file.chunks():
#                 destination_file.write(chunk)
#         print(video_file.name)
#         vidName = video_file.name
#
#         predition = predict(vidName)
#         print(predition)
#         print(hi('Rayan'))
#         context = {
#             'first_person': first_person,
#             'second_person': second_person,
#
#         }
#
#         return render(request, 'MainApp/report.html', context)
#         # return redirect('report', first=first_person, second=second_person )
#     else:
#         return render(request, 'MainApp/form.html')
#
#
# def report(request):
#     return render(request, 'MainApp/report.html')


def upload(request):
    if request.method == 'POST':
        first_person = request.POST.get('firstPerson')
        second_person = request.POST.get('secondPerson')
        # video = request.FILES.get('videoFile')
        file_name = request.POST.get('file')
        df2 = pd.read_csv(fr"C:\Users\Rayan\Desktop\Raqeeb\mainApp\videos\{file_name}")
        list = ['offset', 'xmin', 'ymin', 'xmax', 'ymax', 'car_direction', 'car_curv', 'x_lane_Two_firstPoint',
                'y_lane_Two_firstPoint', 'x_lane_Two_midPoint', 'y_lane_Two_midPoint', 'x_lane_Two_lastPoint',
                'y_lane_Two_lastPoint', 'x_lane_Three_firstPoint', 'y_lane_Three_firstPoint', 'x_lane_Three_midPoint',
                'y_lane_Three_midPoint', 'x_lane_Three_lastPoint', 'y_lane_Three_lastPoint']
        # label_encoder = LabelEncoder()
        print(df2)
        # for i in list:
        #     df2[i] = label_encoder.fit_transform(df2[i])
        # print(df2)
        model = pickle.load(open(r"C:\Users\Rayan\Desktop\Raqeeb\mainApp\new_model.pkl", 'rb'))
        predection = model.predict(df2.tail(1))
        first_person_rate = 0
        second_person_rate = 0
        gif = 0
        print(predection)
        if predection[0] == 0:
            first_person_rate = 100
            second_person_rate = 0
            gif = 0
        elif predection[0] == 1:
            first_person_rate = 25
            second_person_rate = 75
            gif = 1
        elif predection[0] == 2:
            first_person_rate = 25
            second_person_rate = 75
            gif = 2
        context = {
            'first_person': first_person,
            'second_person': second_person,
            'first_person_rate': first_person_rate,
            'second_person_rate': second_person_rate,
            'gif': gif
        }

        return render(request, 'MainApp/report.html', context)
        # return redirect('report', first=first_person, second=second_person )
    else:
        folder_path = r'C:\Users\Rayan\Desktop\Raqeeb\mainApp\videos'
        file_names = os.listdir(folder_path)
        context = {
            'file_names': file_names,
        }
        # Replace with your folder path
        return render(request, 'MainApp/form.html', context)