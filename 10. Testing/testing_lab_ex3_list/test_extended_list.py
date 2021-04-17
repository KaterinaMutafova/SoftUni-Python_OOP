from unittest import TestCase, main

from testing_lab_ex3_list.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.new_list = IntegerList([])

    def test_add(self):
        self.new_list.add(42)
        self.assertEqual(42, self.new_list.get_data())

    def test_get_data(self):
        self.new_list.add(42)
        self.new_list.add(43)
        self.assertEqual([42, 43], self.new_list.get_data())

    def test_list_is_set(self):
        self.assertEqual([42], self.new_list.add(42))
        with self.assertRaises(ValueError) as exc:
            self.new_list.add("a")
        self.assertEqual("Element is not Integer", str(exc.exception))
        self.assertEqual([42, 43], self.new_list.add(43))

    def test_remove_by_index(self):
        self.new_list.add(42)
        self.new_list.add(43)
        el = self.new_list.remove_index(0)
        self.assertEqual(42, el)

    def test_remove_by_index_raises_index_error(self):
        self.assertRaises(IndexError, self.new_list.remove_index, 0)

    def test_init_takes_only_ints(self):
        list_1 = IntegerList("a", 42, "b")
        self.assertEqual([42], list_1.get_data())

    def test_get_to_return_specific_element(self):
        self.new_list.add(42)
        self.assertEqual(42, self.new_list.get(0))
        with self.assertRaises(IndexError) as exc:
            self.new_list.get(3)
        self.assertEqual("Index is out of range", str(exc.exception))

    def test_to_insert_in_index(self):
        self.new_list.add(42)
        self.new_list.add(43)
        self.new_list.insert(0, 44)
        self.assertEqual([44, 42, 43], self.new_list.get_data())

    def test_to_insert_element_in_index_raises_index_error(self):
        with self.assertRaises(IndexError) as exc:
            self.new_list.insert(3, 0)
        self.assertEqual("Index is out of range", str(exc.exception))

    def test_to_insert_element_which_is_not_int_raises_value_error(self):
        self.new_list.add(42)
        with self.assertRaises(ValueError) as exc:
            self.new_list.insert(0, "a")
        self.assertEqual("Element is not Integer", str(exc.exception))

    def test_get_biggest(self):
        self.new_list.add(42)
        self.new_list.add(43)
        self.new_list.add(44)
        self.assertEqual(44, self.new_list.get_biggest())

    def test_get_index(self):
        self.new_list.add(42)
        self.new_list.add(43)
        self.new_list.add(44)
        self.assertEqual(0, self.new_list.get_index(42))
        self.assertEqual(1, self.new_list.get_index(43))



if __name__ == '__main__':
    main()

