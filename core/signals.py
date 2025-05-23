from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# ici on crée un profile à chaque nouvel utilisateur
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print(f"Création du profil pour {instance.username}")
        Profile.objects.create(user=instance)  # create profile

# ici on sauvegarde le profile dans la base
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()