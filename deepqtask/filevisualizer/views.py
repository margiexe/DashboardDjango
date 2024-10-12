import os
import plotly.graph_objs as go
import plotly.offline as pyo
from django.shortcuts import render
from django.http import HttpResponse
from .file_utils import read_csv

def visualize_data(request):
    file_path = 'media/SPI_index_labelled.csv'
    
    data = read_csv(file_path)

    print(data[:1])

    print("Total data points:", len(data))

    x_data = []
    y_data = []
    cnt = 0
    for row in data:
        try:
            x_data.append(row['iso3c'])
            y_data.append(row['SPI.INDEX.PIL5'])
            cnt += 1
            if cnt==100:
                break
        except ValueError as e:
            print(f"Error converting data: {e}")
            continue

    if not x_data or not y_data:
        return HttpResponse("Error: No valid data points after processing")

    print("Processed data points:", len(x_data))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines+markers', name='Line Graph'))
    
    fig.update_layout(
        title='SPI Index Line Graph (Limited Data)',
        xaxis_title='iso3c',
        yaxis_title='SPI Index PIL 5',
        xaxis=dict(tickangle=45)
    )
    
    graph_html = pyo.plot(fig, output_type='div', include_plotlyjs=True)
    
    print("Generated graph HTML length:", len(graph_html))

    return render(request, 'filevisualizer/data.html', {'graph_html': graph_html})