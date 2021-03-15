class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = int((1 / 4) * photos_count)
        return PhotoAlbum(pages)

    def add_photo(self, label: str):
        for idx, page in enumerate(self.photos):
            if len(page) < 4:
                    page.append(label)
                    # page_index = page + 1
                    # slot_index = self.photos[page].index(label) + 1
                    return f"{label} photo added successfully on page " \
                           f"{idx + 1} slot {len(page)}"
        return "No more free spots"

    def display(self):
        result = []
        for page in self.photos:
            if len(page) > 0:
                result.append('-' * 11)
                result.append(('[] ' * len(page)).rstrip(' '))
            else:
                result.append('-' * 11)
                result.append('')
        result.append('-' * 11)

        return '\n'.join(result) + '\n'




# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
#
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
# print(album.photos)
#
# print(album.display())




import unittest


class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free spots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------\n")


if __name__ == "__main__":
    unittest.main()


