from rest_framework import serializers

from api.models import Curso, Nota, Rol, Invitation

from .user import UserSerializer

from django.utils import timezone

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
        read_only_field = (
            'is_teacher',
            'is_studen'

        )

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        read_only_field = (
            "curso"
        )

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'
        read_only_field = (
            "nota"
        )

class EstudianteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Rol
        fields = (
            'user',
            'is_studen',
            'is_teacher',
            'is_active'
        )
        read_only_field = (
            'user',
            'is_teacher',
            'is_studen'
        )

class AddStudenSerializer(serializers.Serializer):

    invitation_code = serializers.CharField(min_length=8)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate_user(self, data):
        curso = self.context['curso']
        user = data
        q = Rol.objects.filter(curso=curso, user=user)
        if q.exists():
            raise serializers.ValidationError('User is already student of this curso')
        return data

    def validate_invitation_code(self, data):
         
        try:
            invitation = Invitation.objects.get(
                code=data,
                curso=self.context['curso'],
                used=False
            )
        except Invitation.DoesNotExist:
            raise serializers.ValidationError('Invalid invitation code.')
        self.context['invitation'] = invitation
        return data
    
    def create(self, data):
        """Create new curso member."""
        curso = self.context['curso']
        invitation = self.context['invitation']
        user = data['user']

        now = timezone.now()

        # studen creation
        member = Rol.objects.create(
            user=user,
            profile=user.profile,
            curso=curso,
            invited_by=invitation.issued_by
        )

        # Update Invitation
        invitation.used_by = user
        invitation.used = True
        invitation.used_at = now
        invitation.save()

        # Update issuer data
        issuer = Rol.objects.get(user=invitation.issued_by, curso=curso)
        issuer.remaining_invitations -= 1
        issuer.save()

        return member
