from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from googletrans import Translator
from django.db.models import Q


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer

    @action(detail=False, methods=['get'])
    def translated(self, request):
        language = request.query_params.get('language', 'en')
        sender_id = request.query_params.get('sender_id')
        receiver_id = request.query_params.get('receiver_id')
        messages = Message.objects.filter(Q(sender__id=sender_id, receiver__id=receiver_id) | Q(
            receiver__id=sender_id, sender__id=receiver_id)).order_by('-timestamp')[:10]  # Get the latest 10 messages
        translator = Translator()
        translated_messages = []
        for message in messages:
            translated_content = translator.translate(
                message.content, dest=language).text
            translated_messages.append({
                'sender': message.sender.username,
                'receiver': message.receiver.username,
                'content': translated_content,
                'language': language,
                'timestamp': message.timestamp
            })
        return Response(translated_messages)
