# Generated by Django 2.0.10 on 2019-01-13 15:08

from django.db import migrations, models


def clear_evaluation_names(apps, _schema_editor):
    Evaluation = apps.get_model('evaluation', 'Evaluation')
    for evaluation in Evaluation.objects.all():
        if evaluation.course.evaluations.count() == 1:
            evaluation.name_de = ""
            evaluation.name_en = ""
            evaluation.save()


def name_evaluations(apps, _schema_editor):
    Evaluation = apps.get_model('evaluation', 'Evaluation')
    Course = apps.get_model('evaluation', 'Course')
    for course in Course.objects.all():
        if course.evaluations.count() == 1:
            evaluation = Evaluation.objects.get(pk=course.evaluations.first().pk)
            evaluation.name_de = course.name_de
            evaluation.name_en = course.name_en
            evaluation.save()
        else:
            for i in range(0, course.evaluations.count()):
                evaluation = Evaluation.objects.get(pk=course.evaluations.all()[i].pk)
                evaluation.name_de = "{} ({})".format(course.name_de, i)
                evaluation.name_en = "{} ({})".format(course.name_en, i)
                evaluation.save()


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0099_multiple_evaluations_per_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='name_de',
            field=models.CharField(blank=True, default='', max_length=1024, verbose_name='name (german)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='name_en',
            field=models.CharField(blank=True, default='', max_length=1024, verbose_name='name (english)'),
            preserve_default=False,
        ),
        migrations.RunPython(
            clear_evaluation_names,
            reverse_code=name_evaluations
        ),
    ]