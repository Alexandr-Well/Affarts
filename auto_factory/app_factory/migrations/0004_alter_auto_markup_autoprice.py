# Generated by Django 4.1 on 2022-08-11 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_factory', '0003_alter_detail_detail_type_alter_detail_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='markup',
            field=models.FloatField(default=0, verbose_name='Наценка %'),
        ),
        migrations.CreateModel(
            name='AutoPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Crated at')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Цена')),
                ('auto_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_factory.auto')),
            ],
        ),
    ]
