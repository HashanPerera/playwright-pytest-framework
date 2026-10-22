def test_check_broken_image(broken_link_image):
    broken_link_image.navigate()
    broken_link_image.check_broken_image()

def test_check_visible_image(broken_link_image):
    broken_link_image.navigate()
    broken_link_image.check_unbroken_image()