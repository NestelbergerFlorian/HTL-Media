import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=30)),
                ('image_file', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('main_Tag', models.CharField(choices=[('1', '3AHIT')], max_length=20)),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.user')),
            ],
        ),
    ]
