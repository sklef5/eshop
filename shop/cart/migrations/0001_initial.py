from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Кількість')),
                ('active', models.BooleanField(default=True, verbose_name='Активна')),
            ],
            options={
                'db_table': 'CartItemModel',
            },
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.CharField(blank=True, max_length=250)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'CartModel',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='OrderItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='Ціна')),
                ('quantity', models.PositiveIntegerField(verbose_name='Кількість')),
            ],
            options={
                'db_table': 'OrderItemModel',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('нове', 'новий'), ('в обр', 'у обробці'), ('скас', 'скасовано'), ('оброб', 'оброблено')], default='нове', max_length=6, verbose_name='Статус заказу')),
            ],
            options={
                'db_table': 'OrderModel',
            },
        ),
        migrations.CreateModel(
            name='OrderReturnModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_up', models.DateField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordersret', to='cart.ordermodel', verbose_name='Замовлення')),
            ],
            options={
                'db_table': 'OrderReturnModel',
            },
        ),
    ]
