# create a naan class that takes whether the user has the ingredients to make each product
class NaanFactory:

    # define a method that makes do if water and flour is True
    def make_dough(self, water, flour):
        if water and flour:
            return True
        else:
            return False

    # Define a method that makes naan if dough is True
    def make_naan(self, dough):
        if dough:
            return True
        else:
            return False

    # Define a method that makes naan from water and flour
    def run_factory(self, water, flour):
        # returns true if naan is made. This depends if make dough returns True
        return self.make_naan(self.make_dough(water, flour))