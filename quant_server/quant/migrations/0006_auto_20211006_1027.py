# Generated by Django 3.2.7 on 2021-10-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quant', '0005_auto_20211006_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kline_1d',
            name='pb_mrq',
            field=models.DecimalField(decimal_places='4', default='', max_digits='8', verbose_name='市净率'),
        ),
        migrations.AlterField(
            model_name='kline_1d',
            name='pcf_ncf_ttm',
            field=models.DecimalField(decimal_places='4', default='', max_digits='8', verbose_name='滚动市现率'),
        ),
        migrations.AlterField(
            model_name='kline_1d',
            name='pct_chg',
            field=models.DecimalField(decimal_places='4', default='', max_digits='8', verbose_name='涨跌幅(百分比)'),
        ),
        migrations.AlterField(
            model_name='kline_1d',
            name='pe_ttm',
            field=models.DecimalField(decimal_places='4', default='', max_digits='8', verbose_name='滚动市盈率'),
        ),
        migrations.AlterField(
            model_name='kline_1d',
            name='ps_ttm',
            field=models.DecimalField(decimal_places='4', default='', max_digits='8', verbose_name='滚动市销率'),
        ),
    ]
