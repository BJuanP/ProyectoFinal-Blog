from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from apps.articulos.models import Articulo
from apps.comentarios.models import Comentario


class Command(BaseCommand):
    help = 'Crea los grupos de usuario Miembro y Moderador con sus permisos asignados.'

    def handle(self, *args, **kwargs):
        # Grupo: Miembro
        miembro_group, _ = Group.objects.get_or_create(name='Miembro')
        permisos_miembro = Permission.objects.filter(
            content_type=ContentType.objects.get_for_model(Comentario),
            codename__in=[
                'add_comentario',
                'view_comentario'
            ]
        )
        miembro_group.permissions.set(permisos_miembro)

        # Grupo: Moderador
        moderador_group, _ = Group.objects.get_or_create(name='Moderador')
        permisos_moderador = Permission.objects.filter(
            content_type__in=ContentType.objects.get_for_models(Articulo, Comentario).values()
        )
        moderador_group.permissions.set(permisos_moderador)

        self.stdout.write(self.style.SUCCESS('✅ Grupos creados y permisos asignados.'))

