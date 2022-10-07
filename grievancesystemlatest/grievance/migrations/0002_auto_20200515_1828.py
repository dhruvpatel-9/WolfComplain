# Generated by Django 3.0.3 on 2020-05-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='designation',
            field=models.CharField(choices=[('Principal', 'Principal'), ('HOD', 'HOD'), ('Security Head', 'Security Head'), ('Canteen Owner', 'Canteen Owner'), ('Senior Librarian', 'Senior Librarian'), ('Vice-Principal', 'Vice-Principal')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='complain',
            name='related_to',
            field=models.CharField(choices=[('Management', 'Management'), ('Library', 'Library'), ('Faculty', 'Faculty'), ('Security', 'Security')], default='', max_length=20, verbose_name='Complain Related to'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Viewed', 'Viewed'), ('Solved', 'Solved')], default='Pending', max_length=10),
        ),
    ]