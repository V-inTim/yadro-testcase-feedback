from rest_framework import serializers

from .models import Feedback, FeedbackType


class FeedbackTypeSerializer(serializers.ModelSerializer):
    """Сериалайзер для типа обратной связи."""

    class Meta:
        model = FeedbackType
        fields = ['id', 'name']


class FeedbackSerializer(serializers.ModelSerializer):
    """Сериалайзер для обратной связи."""

    feedback_type = serializers.PrimaryKeyRelatedField(
        queryset=FeedbackType.objects.all(),
        required=True,
    )
    file = serializers.FileField(write_only=True, required=False)
    text = serializers.CharField(required=True)

    class Meta:
        model = Feedback
        fields = ['id', 'feedback_type', 'file', 'text']
        read_only_fields = ['id']

    def validate_file(self, value):
        """Проверка размера файла."""
        max_size = 1024 * 1024
        if value.size > max_size:
            raise serializers.ValidationError("Файлы только до 1 МБ")
        return value
