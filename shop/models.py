from django.db import models
from django.db import connection
from datetime import datetime


class Telephone(models.Model):
    title = models.CharField(max_length=150, unique=True)
    brand = models.CharField(max_length=100)
    built_in_memory = models.CharField(max_length=100)
    price = models.BigIntegerField(null=False)

    diagonal_screen = models.FloatField(max_length=100)

    update_time = models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    @classmethod
    def get_all(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM shop_telephone;")
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return results

    @classmethod
    def post_new_item(cls, data):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data['created_time'] = current_time
        data['update_time'] = current_time

        with connection.cursor() as cursor:
            query = """
                    INSERT INTO shop_telephone (title, brand, built_in_memory, price, diagonal_screen, created_time, update_time) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                """
            cursor.execute(query, [data.get('title'), data.get('brand'), data.get('built_in_memory'), data.get('price'),
                                   data.get('diagonal_screen'), data['created_time'], data['update_time']])
            new_telephone_id = cursor.lastrowid

        return new_telephone_id

    @classmethod
    def get_item(cls, telephone_id):
        with connection.cursor() as cursor:
            query = """
                SELECT * FROM shop_telephone
                WHERE id = %s;
            """
            cursor.execute(query, [telephone_id])

            # Получаем имена столбцов из cursor.description
            columns = [col[0] for col in cursor.description]

            # Создаем словарь, используя имена столбцов в качестве ключей
            result = dict(zip(columns, cursor.fetchone()))

        return result

    @classmethod
    def delete_item(cls, telephone_id):
        with connection.cursor() as cursor:
            query = """
                DELETE FROM shop_telephone
                WHERE id = %s;
            """
            cursor.execute(query, [telephone_id])
