# Generated by Django 3.1.2 on 2020-11-06 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activity', '0001_initial'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Massintentions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Thanksgiving'), (1, 'Late'), (2, 'Other')], default=0)),
                ('text', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=100.0, max_digits=10)),
                ('by', models.TextField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.activity')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='payments.transaction')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
