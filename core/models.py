from django.forms import ModelForm


class AbstractModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        abstract = True

def update_attrs(instance, **kwargs):
    instance_pk = instance.pk

    for key, value in kwargs.items():
        if value is None or not value:
            continue
        if hasattr(instance, key):
            setattr(
                instance,
                key,
                value,
            )

    instance.save(
        force_update=True,
    )

    return instance.__class__.objects.get(
        pk=instance_pk,
    )
