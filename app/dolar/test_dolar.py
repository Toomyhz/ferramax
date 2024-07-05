from app.dolar.getDolar import getDolar

def testGetDolar():
    test_date = "2024-01-02"
    assert getDolar(test_date) == '877.12'