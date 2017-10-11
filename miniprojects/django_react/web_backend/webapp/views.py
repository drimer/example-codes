# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class RemindersView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        reminders = [
            {
                'id': 1,
                'title': 'Buy cinema tickets',
                'text': 'For the Avengers, tomorrow at 8m.',
            },
            {
                'id': 2,
                'title': 'Do groceries',
                'text': 'Bread, milk and eggs.',
            },
            {
                'id': 3,
                'title': 'Renew passport',
                'text': "Don't forget to bring photo.",
            },
            {
                'id': 4,
                'title': 'Do ReactJS tutorial',
                'text': "It's in their official website.",
            },
            {
                'id': 5,
                'title': 'Prepare surprise party for my girlfriend',
                'text': 'Need to buy candles.',
            },
        ]

        return JsonResponse(reminders, safe=False)
