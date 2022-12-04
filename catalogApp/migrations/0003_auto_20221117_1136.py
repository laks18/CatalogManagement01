# Generated by Django 3.2.11 on 2022-11-17 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogApp', '0002_order_penalty'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_master',
            name='qty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product_master',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pending for verification'), (2, 'Approved/Delivered'), (3, 'Cancel'), (4, 'Return'), (5, 'Penalty')], default=1),
        ),
    ]
