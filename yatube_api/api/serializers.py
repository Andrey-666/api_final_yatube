from rest_framework import serializers
from rest_framework.serializers import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Follow, Comment, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('following', 'user',)

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('following', 'user',),
                message=('Вы уже подписаны!')
            )
        ]

    def validate(self, data):
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на себя!'
            )
        return data
