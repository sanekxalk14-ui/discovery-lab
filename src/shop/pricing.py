def final_price_cents(
    base_cents: int, discount_percent: int = 0, tax_percent: int = 0
) -> int:
    """
    Контракт:
    - base_cents: int, >= 0
    - discount_percent: int, 0..100
    - tax_percent: int, 0..100
    Логика:
    - discount применяется к base
    - затем добавляется tax
    - результат округляется до целых центов (int)
    """
    if base_cents < 0:
        raise ValueError("Base price cannot be negative")
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount must be between 0 and 100")
    if not (0 <= tax_percent <= 100):
        raise ValueError("Tax must be between 0 and 100")

    # Применяем скидку
    discounted = base_cents * (100 - discount_percent) // 100
    # Добавляем налог
    final = discounted * (100 + tax_percent) // 100

    return final