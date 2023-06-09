# Generated by Django 3.2.5 on 2023-03-01 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_cart', to='marketplace.product')),
            ],
        ),
    ]
