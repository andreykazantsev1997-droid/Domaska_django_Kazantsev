from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = "Очищает базу данных и загружает данные из фикстур"

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Deleting old data..."))

        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.WARNING("Loading new data..."))

        try:
            call_command("loaddata", "category_data.json")
            call_command("loaddata", "product_data.json")

            self.stdout.write(self.style.SUCCESS("DB successfully refilled"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error loading: {e}"))
