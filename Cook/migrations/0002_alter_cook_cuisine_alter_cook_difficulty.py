from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('Cook', '0001_initial')]

    operations = [
        migrations.AlterField(
            model_name='cook', name='cuisine',
            field=models.CharField(choices=[('Indian', 'Indian'), ('Chinese', 'Chinese'), ('Italian', 'Italian'), ('Mexican', 'Mexican'), ('Continental', 'Continental'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='cook', name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=50),
        ),
    ]
