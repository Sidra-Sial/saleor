# Generated by Django 2.2.9 on 2020-01-29 06:52

from django.db import migrations, models, transaction
from django.db.utils import IntegrityError
from django.utils.text import slugify


def create_unique_slug_for_warehouses(apps, schema_editor):
    Warehouse = apps.get_model("warehouse", "Warehouse")

    for warehouse in Warehouse.objects.filter(slug__isnull=True):
        slug = slugify(warehouse.name)
        extension = 1
        slug_value = slug
        while True:
            try:
                with transaction.atomic():
                    warehouse.slug = slug_value
                    warehouse.save(update_fields=["slug"])
                break
            except IntegrityError:
                extension += 1
                slug_value = f"{slug}-{extension}"


class Migration(migrations.Migration):

    dependencies = [
        ("warehouse", "0002_auto_20200123_0036"),
    ]

    operations = [
        migrations.AddField(
            model_name="warehouse",
            name="slug",
            field=models.SlugField(null=True, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.RunPython(
            create_unique_slug_for_warehouses, migrations.RunPython.noop
        ),
        migrations.AlterField(
            model_name="warehouse",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
