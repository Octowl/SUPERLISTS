from unittest import skip
from .base import FuntionalTest


class ItemValidationTest(FuntionalTest):

    def test_cannot_add_empty_list_items(self):

        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits enter on an empty input box

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # She tries again with some text for the item, which now works

        # She's an idiot so she tries to submit a second blank item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')
