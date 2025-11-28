from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from serializer import TaskInputSerializer
from scoping import calculate_priority_score
from datetime import datetime

@api_view(['POST'])
def analyze_tasks(request):
    serializer = TaskInputSerializer(data=request.data, many=True)

    if not serializer.is_valid():
        return Response({"error": serializer.errors}, status=400)

    tasks = serializer.data
    scored_tasks = []

    for task in tasks:
        score, explanation = calculate_priority_score(task)
        scored_tasks.append({
            **task,
            "priority_score": score,
            "explanation": explanation
        })

    # Sort by score (desc)
    scored_tasks.sort(key=lambda x: x['priority_score'], reverse=True)

    return Response(scored_tasks)


@api_view(['GET'])
def suggest_tasks(request):
    # Normally fetch from DB (optional)
    return Response({"error": "No tasks stored in DB yet"})
