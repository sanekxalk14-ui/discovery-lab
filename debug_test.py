import sys
import os

# Добавляем путь к src в sys.path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

try:
    # Проверяем импорт функции
    from shop.pricing import final_price_cents
    print("✓ Импорт shop.pricing прошёл успешно")

    # Проверяем расчёт
    result = final_price_cents(1000, 10, 20)
    print(f"✓ Базовый расчёт: 1000 центов, 10 % скидка, 20 % налог → {result} центов")

    # Импортируем тестовый класс
    from tests.unit.pricing_spec import TestFinalPrice
    print("✓ Импорт тестов прошёл успешно")

    # Создаём экземпляр теста и запускаем метод
    test_instance = TestFinalPrice('test_basic_scenario')
    test_instance.test_basic_scenario()
    print("✓ Тест test_basic_scenario выполнен без ошибок")
except Exception as e:
    print(f"✗ Ошибка: {e}")