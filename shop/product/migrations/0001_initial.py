from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=38, unique=True, verbose_name='Категорія')),
                ('slug', models.SlugField(editable=False, max_length=38)),
                ('class_category', models.IntegerField(verbose_name='Клас')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
            ],
            options={
                'db_table': 'Category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва товару')),
                ('slug', models.SlugField(editable=False, max_length=150)),
                ('manufacturer', models.CharField(max_length=38, null=True, verbose_name='Виробник')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис товару')),
                ('price', models.FloatField(null=True, verbose_name='Ціна')),
                ('availability', models.PositiveIntegerField(default=0, null=True, verbose_name='Наявність')),
                ('currency', models.CharField(default='UAH', max_length=4, verbose_name='Валюта')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='product.categorymodel', verbose_name='Категорія')),
            ],
            options={

                'db_table': 'Product',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductImagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Фото')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('locate', models.ImageField(upload_to='images/product/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodimg', to='product.productmodel', verbose_name='Товар')),
            ],
            options={
                'db_table': 'ProductImages',
            },
        ),
        migrations.CreateModel(
            name='CategoryImagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Фото')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('locate', models.ImageField(upload_to='images/category/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catimg', to='product.categorymodel', verbose_name='Категорія')),
            ],
            options={
                'db_table': 'CategoryImages',
            },
        ),
    ]
