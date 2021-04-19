from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upperfield', models.CharField(max_length=50, verbose_name='верхнее поле')),
                ('lowerfield', models.TextField(verbose_name='нижнее поле')),
            ],
        ),
        migrations.AlterModelOptions(
            name='messages',
            options={'verbose_name': 'Коментарий', 'verbose_name_plural': 'Коментарии'},
        ),
    ]
