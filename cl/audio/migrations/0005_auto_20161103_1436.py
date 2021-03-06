# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_auto_20161028_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='stt_google_response',
            field=models.TextField(help_text='The JSON response object returned by Google Speech.', verbose_name='Speech to text Google response', blank=True),
        ),
        migrations.AlterField(
            model_name='audio',
            name='stt_status',
            field=models.SmallIntegerField(default=0, help_text='The status of the Speech to Text for this item?', verbose_name='Speech to text status', choices=[(0, 'Speech to Text Needed'), (1, 'Speech to Text Complete'), (2, 'Speech to Text Failed')]),
        ),
    ]
