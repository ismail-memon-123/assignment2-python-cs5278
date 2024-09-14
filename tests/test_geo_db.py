from cs5278_assignment_2.live3.geo_db_factory import GeoDBFactory


class TestGeoDB:
    @staticmethod
    def test_simple_insert():
        bits_of_precision = 16
        db = GeoDBFactory.new_database(bits_of_precision)

        db.insert(0, 0)

        for i in range(bits_of_precision):
            assert db.contains(0, 0, i)

    @staticmethod
    def test_simple_delete():
        bits_of_precision = 16
        db = GeoDBFactory.new_database(bits_of_precision)

        db.insert(0, 0)
        db.delete(0, 0)

        for i in range(bits_of_precision):
            assert not db.contains(0, 0, i)

    @staticmethod
    def test_zero_bits():
        db = GeoDBFactory.new_database(16)

        db.insert(0, 0)
        db.insert(90, 180)
        db.insert(-90, -180)
        db.insert(-90, 180)
        db.insert(90, -180)

        assert 5 == len(db.nearby(0, 0, 0))

    @staticmethod
    def test_zero_bits_delete():
        db = GeoDBFactory.new_database(16)
        db.insert(0, 0)
        db.insert(90, 180)
        db.insert(-90, -180)
        db.insert(-90, 180)
        db.insert(90, -180)

        db.delete_all(0, 0, 0)

        assert not len(db.nearby(0, 0, 0))

    @staticmethod
    def test_insert_delete_series():
        db = GeoDBFactory.new_database(16)

        db.insert(0, 0)
        db.insert(90, 180)
        db.insert(-90, -180)
        db.insert(-90, 180)
        db.insert(90, -180)

        assert db.contains(0, 0, 16)
        assert db.contains(90, 180, 16)
        assert db.contains(-90, -180, 16)
        assert db.contains(-90, 180, 16)
        assert db.contains(90, -180, 16)
        assert db.contains(90.5, -180.5, 16)
        assert not db.contains(1, -1, 16)
        assert not db.contains(45, -45, 16)

        db.delete(90, -180)

        assert not db.contains(90, -180, 16)

        db.delete_all(1, 1, 1)

        assert db.contains(-90, -180, 16)
        assert not db.contains(90, 180, 16)

        db.insert(90, 180)

        assert db.contains(90, 180, 16)
