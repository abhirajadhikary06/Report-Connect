import os, random
from django.shortcuts import render, redirect, get_object_or_404
from .forms import HarassmentReportForm, CommentForm
from geopy.geocoders import Nominatim
import json
from scipy.stats import gaussian_kde
import numpy as np 
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import HarassmentReport, Upvote, Comment
from django.contrib import messages

        
def landing_page(request):
    return render(request, 'landing.html')
        
def predict_crime_hotspot():
    # Get all reports with latitude & longitude
    reports = HarassmentReport.objects.exclude(latitude=None, longitude=None)

    if reports.count() < 3:  # Ensure enough data points for KDE
        return None  # Not enough data to predict

    # Convert data into numpy array
    locations = np.array([[report.latitude, report.longitude] for report in reports]).T  # Transpose for KDE

    # Apply Kernel Density Estimation (KDE)
    kde = gaussian_kde(locations)

    # Evaluate density at all reported locations
    densities = kde(locations)

    # Get indices of the top 20 highest densities
    sorted_indices = np.unique(np.argsort(densities)[::-1])[:20]  # Sort in descending order and pick top 20

    # Get the top 20 hotspot locations
    hotspots = []
    for index in sorted_indices:
        hotspot_lat, hotspot_lng = locations[:, index]
        hotspots.append({'lat': hotspot_lat, 'lng': hotspot_lng, 'title': f"Hotspot {index+1}", 'description': "Predicted crime hotspot"})
    
    return hotspots

def home(request):
    # Get all reports from the database
    reports = HarassmentReport.objects.all()

    # Calculate date ranges
    now = timezone.now()
    one_day_ago = now - timedelta(days=1)
    seven_days_ago = now - timedelta(days=7)
    fourteen_days_ago = now - timedelta(days=14)

    # Apply time filter if provided
    time_filter = request.GET.get('time_filter')
    if time_filter == 'current_day':
        reports = reports.filter(timestamp__gte=one_day_ago)
    elif time_filter == 'last_7_days':
        reports = reports.filter(timestamp__gte=seven_days_ago, timestamp__lt=one_day_ago)

    # Convert reports to a format suitable for JavaScript
    reports_data = [
        {
            'lat': report.latitude,
            'lng': report.longitude,
            'location': report.location,
            'type': report.harassment_type,
            'timestamp': report.timestamp.isoformat(),  # Include timestamp for debugging
        } for report in reports
    ]

    # Get predicted hotspot
    predicted_hotspot = predict_crime_hotspot()
    context = {
        'reports': json.dumps(reports_data),
        'hotspot': json.dumps(predicted_hotspot) if predicted_hotspot else None,
        'time_filter': time_filter,  # Pass the selected filter back to the template
    }
    return render(request, 'home.html', context)


def reports_list(request):
    # Retrieve all reports
    reports = HarassmentReport.objects.all().order_by('-timestamp')

    # Apply filters
    type_filter = request.GET.get('type')
    location_filter = request.GET.get('location')
    if type_filter:
        reports = reports.filter(harassment_type=type_filter)
    if location_filter:
        reports = reports.filter(location__icontains=location_filter)

    # Handle comment submission
    if request.method == "POST":
        report_id = request.POST.get('report_id')
        report = get_object_or_404(HarassmentReport, id=report_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.report = report
            comment.save()

    context = {
        'reports': reports,  # Pass the filtered reports to the template
        'comment_form': CommentForm(),  # Pass an empty form for rendering
    }
    return render(request, 'reports.html', context)

def report_submission(request):
    if request.method == "POST":
        form = HarassmentReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_submission')  # Redirect to the same page to prevent form resubmission
    else:
        form = HarassmentReportForm()
    return render(request, 'report_submission.html', {'form': form})


def add_comment(request, report_id):
    report = get_object_or_404(HarassmentReport, id=report_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.report = report
            comment.save()
            messages.success(request, "Comment added successfully!")
            return redirect('report_detail', report_id=report.id)  # Redirect to clear form
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'report': report})