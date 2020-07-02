# Generated by Django 3.0.7 on 2020-07-01 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_RecordMoney', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accounts', models.CharField(max_length=10, verbose_name='交易账户')),
            ],
        ),
        migrations.CreateModel(
            name='FirstLevelAccountTitles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_level_account_titles', models.CharField(max_length=10, verbose_name='一级科目')),
            ],
        ),
        migrations.CreateModel(
            name='SecondLevelAccountTitles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_level_account_titles', models.CharField(max_length=10, verbose_name='二级科目')),
                ('first_level_account_titles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_RecordMoney.FirstLevelAccountTitles')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdLevelAccountTitles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('third_level_account_titles', models.CharField(max_length=10, verbose_name='三级科目')),
                ('first_level_account_titles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_RecordMoney.FirstLevelAccountTitles')),
                ('second_level_account_titles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_RecordMoney.SecondLevelAccountTitles')),
            ],
        ),
        migrations.CreateModel(
            name='RecordMoney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trading_date', models.DateField(verbose_name='交易日期')),
                ('trading_week', models.IntegerField(verbose_name='周')),
                ('trading_period', models.IntegerField(verbose_name='所属期间')),
                ('trader', models.CharField(max_length=20, verbose_name='交易商家')),
                ('summary', models.CharField(max_length=255, verbose_name='摘要')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='金额(元)')),
                ('record_time', models.DateTimeField(auto_now_add=True, verbose_name='记录时间')),
                ('trading_FLAT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_RecordMoney.FirstLevelAccountTitles', verbose_name='一级科目')),
                ('trading_SLAT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_RecordMoney.SecondLevelAccountTitles', verbose_name='二级科目')),
                ('trading_TLAT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_RecordMoney.ThirdLevelAccountTitles', verbose_name='三级科目')),
                ('trading_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_RecordMoney.Accounts', verbose_name='交易账户')),
            ],
        ),
    ]
