# Generated by Django 4.1.5 on 2023-01-15 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_remove_tag_order_id_saleorderline_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleorderline',
            name='tags',
        ),
        migrations.AddField(
            model_name='saleorder',
            name='tags',
            field=models.ManyToManyField(related_name='tag_sale_order', to='forms.tag'),
        ),
    ]