def update_attrs(instance, **kwargs):
    instance_pk = instance.pk
    for key, value in kwargs.items():
        if value is None or not value:
            continue
        if hasattr(instance, key):
            setattr(instance, key, value)
        # else:
        #     raise KeyError(
        #         f"Failed to update non existing attribute "
        #         f"{instance.__class__.__name__}.{key}"
        #     )
    instance.save(force_update=True)
    return instance.__class__.objects.get(pk=instance_pk)
