# from django.db import models

def update_attrs(instance, **kwargs):
    """ Updates model instance attributes and saves the instance
    :param instance: any Model instance
    :param kwargs: dict with attributes
    :return: updated instance, reloaded from database
    """
    instance_pk = instance.pk
    for key, value in kwargs.items():
        if value is None or not value:
            continue
        if hasattr(instance, key):
            setattr(instance, key, value)
        else:
            raise KeyError(
                f"Failed to update non existing attribute "
                f"{instance.__class__.__name__}.{key}"
            )
    instance.save(force_update=True)
    return instance.__class__.objects.get(pk=instance_pk)