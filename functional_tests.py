 self.assertTrue(
        any(row.text == '1: Buy peacock feathers' for row in rows),
        "New to-do item did not appear in table"
    )