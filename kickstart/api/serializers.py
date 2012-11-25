from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.ModelSerializer):

    permissions = serializers.ManySlugRelatedField(
        slug_field='codename',
        queryset=Permission.objects.all()
    )

    users = serializers.ManyPrimaryKeyRelatedField('user_set')
    url = serializers.HyperlinkedIdentityField(view_name='group-detail')

    class Meta(object):
        model = Group
        #fields = ('url', 'name', 'permissions')