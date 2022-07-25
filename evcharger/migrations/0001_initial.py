# Generated by Django 4.0.4 on 2022-07-15 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evcharger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpname', models.CharField(max_length=64, verbose_name='충전기이름')),
                ('cpnumber', models.CharField(max_length=64, verbose_name='충전기번호')),
                ('partner_id', models.CharField(max_length=128, verbose_name='파트너아이디')),
                ('public_use', models.BooleanField(default=True, verbose_name='공용')),
                ('cpstatus', models.CharField(max_length=64, verbose_name='충전상태')),
                ('connector_id_1', models.CharField(max_length=64, verbose_name='1번커넥터아이디')),
                ('connector_id_1_status', models.CharField(max_length=64, verbose_name='1번커넥터상태')),
                ('connector_id_2', models.CharField(max_length=64, verbose_name='2번커넥터아이디')),
                ('connector_id_2_status', models.CharField(max_length=64, verbose_name='2번커넥터상태')),
                ('address', models.TextField(verbose_name='주소')),
                ('manager_id', models.CharField(max_length=128, verbose_name='관리자아이디')),
                ('cpversion', models.CharField(max_length=64, verbose_name='펌웨어버전')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록일시')),
                ('last_modified_dttm', models.DateTimeField(auto_now_add=True, verbose_name='최종정보변경일시')),
                ('fw_version', models.CharField(max_length=64, verbose_name='펌웨어버전')),
            ],
            options={
                'verbose_name': '충전기',
                'verbose_name_plural': '충전기',
                'db_table': 'evsp_evcharger',
            },
        ),
    ]
