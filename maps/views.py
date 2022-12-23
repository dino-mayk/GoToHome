from django.contrib import messages
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect, render
from djeym.models import Placemark

from gotohome.settings import EMAIL_HOST_USER
from users.models import CustomUser


def map(request):
    if not request.user.is_authenticated or not request.user.is_shelter:
        messages.info(request,
                      'Только приюты могут пользоваться этой картой')
        return redirect('homepage:home')

    template_name = 'maps/shelter_maps.html'

    return render(request, template_name)



# SIMPLE EXAMPLE.
# 1. Notify administrator of a new custom marker.
# 2. Notify user about successful moderation of his marker.
# Mail server for testings: $ python -m smtpd -n -c DebuggingServer localhost:1025
@receiver(post_save, sender=Placemark)
def notify_email(instance, **kwargs):
    """Notify by email of a new custom marker."""

    """
    # May come in handy. (Может пригодится.)
    title = instance.header  # (html)
    description = instance.body  # (html)
    image_url = instance.user_image.url
    """
    print(instance.header, kwargs)
    # Notify administrator of a new custom marker.
    if instance.is_user_marker and not instance.is_sended_admin_email:
        subject = 'Text subject'
        message = 'Text message - Url: ' + \
            'http(s)://your.domain/admin/djeym/placemark/{}/change/'.format(instance.pk)
        from_email = EMAIL_HOST_USER  # or corporate email
        staff_users = list(i['email'] for i in CustomUser.objects.filter(is_staff=True).values('email').distinct())
        print(staff_users)
        recipient_list = staff_users  # Your work email
        send_mail(subject, message, from_email,
                  recipient_list, fail_silently=False)

        # Required
        instance.is_sended_admin_email = True
        instance.save()
    # Notify user about successful moderation of his marker.
    elif instance.active and instance.is_user_marker and not instance.is_sended_user_email:
        subject = 'Text subject'
        message = 'Text message'
        from_email = EMAIL_HOST_USER  # Your work email
        recipient_list = [instance.user_email]
        send_mail(subject, message, from_email,
                  recipient_list, fail_silently=False)
        # Required
        instance.is_sended_user_email = True
        instance.save()