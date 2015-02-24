class Object(dict):
    def __init__(self,o):
        ""
        self.fig=o
        self['shape']=o.id
        self.iden_attr()

    def iden_attr(self):
        ""

    def find_angle(self):
        ""

    def find_size(self):
        ""
    def find_location(self):
        ""

    def find_fill(self):
        ""


class Feature():

    def extract_features(f1,f2):
        lraw1=get_shapes(f1)
        lraw2=get_shapes(f2)

        for o in lraw1:
            compare_affine(o)



    def compare_affine(self,o):

        f1=

        return


    def get_shapes(self):

        return shapes