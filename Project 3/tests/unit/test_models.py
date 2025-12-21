import pytest
from app import create_app
from app.models import Fruit, FruitMetrics, db
from datetime import date


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture
def fruit_data():
    """Sample fruit data for testing — now includes expiration_date."""
    return [
        Fruit(name="Apple", quantity=10, variety="Honeycrisp", season="Fall",
              expiration_date=date(2026, 1, 1)),
        Fruit(name="Apple", quantity=5, variety="Granny Smith", season="Fall",
              expiration_date=date(2026, 1, 1)),
        Fruit(name="Banana", quantity=20, variety="Cavendish", season="Summer",
              expiration_date=date(2025, 12, 31)),
        Fruit(name="Orange", quantity=15, variety="Navel", season="Winter",
              expiration_date=date(2026, 2, 1)),
    ]


def test_createFruit_withValidData_createsFruitWithCorrectAttributes(app):
    """
    Test the creation of a Fruit instance with valid parameters.
    Verifies that all attributes are set correctly.
    """
    with app.app_context():
        fruit = Fruit(
            name="Apple",
            quantity=10,
            variety="Honeycrisp",
            season="Fall",
            expiration_date=date(2026, 1, 1)
        )
        assert fruit.name == "Apple"
        assert fruit.quantity == 10
        assert fruit.variety == "Honeycrisp"
        assert fruit.season == "Fall"
        assert fruit.expiration_date == date(2026, 1, 1)


def test_createFruit_withInvalidName_raisesAssertionError(app):
    """
    Test the creation of a Fruit instance with an invalid name.
    Verifies that an AssertionError is raised when the name is empty or too short.
    """
    with app.app_context():
        with pytest.raises(AssertionError, match="Name is required"):
            Fruit(name="", quantity=10, expiration_date=date(2026, 1, 1))
        with pytest.raises(AssertionError, match="Name must be more than 2 characters"):
            Fruit(name="A", quantity=10, expiration_date=date(2026, 1, 1))


def test_createFruit_withNegativeQuantity_raisesAssertionError(app):
    """
    Test the creation of a Fruit instance with a negative quantity.
    Verifies that an AssertionError is raised.
    """
    with app.app_context():
        with pytest.raises(AssertionError, match="Quantity must be non-negative"):
            Fruit(name="Apple", quantity=-5, expiration_date=date(2026, 1, 1))


def test_createFruit_withNonIntegerQuantity_raisesAssertionError(app):
    """
    Test the creation of a Fruit instance with a non-integer quantity.
    Verifies that an AssertionError is raised.
    """
    with app.app_context():
        with pytest.raises(AssertionError, match="Quantity must be an integer"):
            Fruit(name="Apple", quantity=10.5, expiration_date=date(2026, 1, 1))
        with pytest.raises(AssertionError, match="Quantity must be an integer"):
            Fruit(name="Apple", quantity="10", expiration_date=date(2026, 1, 1))


def test_fruit_serialize_returnsCorrectDict(app):
    """
    Test the serialize method returns a dictionary with all fields.
    """
    with app.app_context():
        fruit = Fruit(
            name="Apple",
            quantity=10,
            variety="Honeycrisp",
            season="Fall",
            expiration_date=date(2026, 1, 1)
        )
        serialized = fruit.serialize()
        assert serialized == {
            'id': None,
            'name': "Apple",
            'quantity': 10,
            'variety': "Honeycrisp",
            'season': "Fall",
            'expiration_date': '2026-01-01'
        }


def test_fruit_search_withNoParams_returnsAll(app, fruit_data):
    """
    Test search with no parameters returns all fruits.
    """
    with app.app_context():
        for f in fruit_data:
            db.session.add(f)
        db.session.commit()
        results = Fruit.search()
        assert len(results) == 4


def test_fruit_search_withNameFilter_returnsMatching(app, fruit_data):
    """
    Test search filters by name (case-insensitive).
    """
    with app.app_context():
        for f in fruit_data:
            db.session.add(f)
        db.session.commit()
        results = Fruit.search(name="apple")
        assert len(results) == 2
        assert all(r.name.lower() == "apple" for r in results)


def test_fruit_search_withMinMaxQuantity(app, fruit_data):
    """
    Test search filters by minimum and maximum quantity.
    """
    with app.app_context():
        for f in fruit_data:
            db.session.add(f)
        db.session.commit()
        results = Fruit.search(min_quantity=10, max_quantity=15)
        assert len(results) == 2
        assert all(10 <= r.quantity <= 15 for r in results)


def test_calculateTotalFruits_withFruitsList_returnsCorrectCount(fruit_data):
    """
    Test total_fruits returns the correct number of fruits.
    """
    assert FruitMetrics.total_fruits(fruit_data) == 4


def test_calculateAverageQuantity_withFruitsList_returnsCorrectAverage(fruit_data):
    """
    Test average_quantity computes the correct average.
    """
    avg = FruitMetrics.average_quantity(fruit_data)
    assert avg == 12.5


def test_calculateAverageQuantity_withEmptyList_returnsZero():
    """
    Test average_quantity handles empty list correctly.
    """
    assert FruitMetrics.average_quantity([]) == 0


def test_identifyMostCommonFruit_withFruitsList_returnsMostFrequent(fruit_data):
    """
    Test most_common_fruit identifies the fruit with highest frequency.
    """
    most_common = FruitMetrics.most_common_fruit(fruit_data)
    assert most_common == "Apple"


def test_identifyMostCommonFruit_withEmptyList_returnsNone():
    """
    Test most_common_fruit handles empty list correctly.
    """
    assert FruitMetrics.most_common_fruit([]) is None


# NEW TESTS FOR EXTRA CREDIT (expiration_date feature)

def test_fruit_with_expiration_date_stores_correctly(app):
    """Test that expiration_date is stored and serialized correctly."""
    with app.app_context():
        fruit = Fruit(
            name="Apple",
            quantity=10,
            variety="Honeycrisp",
            season="Fall",
            expiration_date=date(2025, 12, 31)
        )
        assert fruit.expiration_date == date(2025, 12, 31)
        serialized = fruit.serialize()
        assert serialized['expiration_date'] == '2025-12-31'


def test_invalid_expiration_date_raises_error(app):
    """Test validation for expiration_date."""
    with app.app_context():
        with pytest.raises(AssertionError, match="Expiration must be a valid date object"):
            Fruit(name="Apple", quantity=10, expiration_date="2025-12-31")


def test_search_expired_only_returns_expired_fruits(app):
    """Test search with expired_only=True."""
    with app.app_context():
        expired = Fruit(
            name="Banana",
            quantity=5,
            expiration_date=date(2025, 1, 1)  # expired as of 2025-12-20
        )
        fresh = Fruit(
            name="Apple",
            quantity=10,
            expiration_date=date(2026, 1, 1)  # not expired
        )
        db.session.add_all([expired, fresh])
        db.session.commit()

        results = Fruit.search(expired_only=True)
        assert len(results) == 1
        assert results[0].name == "Banana"