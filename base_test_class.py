from seleniumbase import BaseCase

class BaseTestCase(BaseCase):
    def set_properties_profile(self, profile):
        for key, value in profile.items():
            setattr(self, str(key), value)
    
    def set_testcase_visible_elements(self, visible):
        self.visibleElements = visible

    def set_testcase_absent_elements(self, notVisible):
        self.absentElements = notVisible

    def wait_for_elements_absent(self, absentElements):
        for element in absentElements:
                self.wait_for_element_absent(element)
    
    def wait_for_elements_visible(self, visibleElements):
        for element in visibleElements:
            self.wait_for_element(element)

    def wait_for_texts_visible(self, visibleElements):
        for element in visibleElements:
            self.wait_for_text(element)

    def wait_for_texts_absent(self, visibleElements):
         for element in visibleElements:
            self.wait_for_text_not_visible(element)

    def _validate(self):
        if hasattr(self, "visibleElements"):
            self.wait_for_texts_visible(self.visibleElements)
        if hasattr(self, "absentElements"):
            self.wait_for_texts_absent(self.absentElements)

    
