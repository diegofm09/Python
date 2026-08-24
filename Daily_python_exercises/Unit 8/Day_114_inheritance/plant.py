class Plant:

    photosynthesis = True

    def __init__(self, num_leaves, color, seeds):
        self.num_leaves = num_leaves
        self.color = color
        self.seeds = seeds

    def do_photosynthesis(self):
        print("Photosynthesis done")
