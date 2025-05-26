from django import template
from core.models import Follow
from django.utils import timezone
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def is_followed_by(user, current_user):
    """
    Vérifie si un utilisateur est suivi par l'utilisateur courant
    """
    return Follow.objects.filter(follower=current_user, following=user).exists()

@register.filter
def time_since(value):
    """
    Retourne une chaîne de caractères indiquant le temps écoulé depuis la date donnée
    """
    if not value:
        return ''
        
    now = timezone.now()
    diff = now - value

    if diff < timedelta(minutes=1):
        return 'à l\'instant'
    elif diff < timedelta(hours=1):
        minutes = diff.seconds // 60
        return f'il y a {minutes} min'
    elif diff < timedelta(days=1):
        hours = diff.seconds // 3600
        return f'il y a {hours} h'
    elif diff < timedelta(days=7):
        days = diff.days
        return f'il y a {days} j'
    elif diff < timedelta(days=30):
        weeks = diff.days // 7
        return f'il y a {weeks} sem'
    elif diff < timedelta(days=365):
        months = diff.days // 30
        return f'il y a {months} mois'
    else:
        years = diff.days // 365
        return f'il y a {years} an{"s" if years > 1 else ""}' 