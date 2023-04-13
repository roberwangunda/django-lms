# Generated by Django 4.1.6 on 2023-04-11 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("course", "__first__"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TakenCourse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "assignment",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "mid_exam",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "quiz",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "attendance",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "final_exam",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "total",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "grade",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("A+", "A+"),
                            ("A", "A"),
                            ("A-", "A-"),
                            ("B+", "B+"),
                            ("B", "B"),
                            ("B-", "B-"),
                            ("C+", "C+"),
                            ("C", "C"),
                            ("C-", "C-"),
                            ("D", "D"),
                            ("F", "F"),
                            ("NG", "NG"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "point",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "comment",
                    models.CharField(
                        blank=True,
                        choices=[("PASS", "PASS"), ("FAIL", "FAIL")],
                        max_length=200,
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taken_courses",
                        to="course.course",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Result",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gpa", models.FloatField(null=True)),
                ("cgpa", models.FloatField(null=True)),
                (
                    "term",
                    models.CharField(
                        choices=[
                            ("First", "First"),
                            ("Second", "Second"),
                            ("Third", "Third"),
                        ],
                        max_length=100,
                    ),
                ),
                ("session", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("Bachloar", "Bachloar Degree"),
                            ("Master", "Master Degree"),
                        ],
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.student",
                    ),
                ),
            ],
        ),
    ]
