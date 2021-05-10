from OpenGL.GL import *
import numpy as np
from PIL import Image


class Geometry:

    def cubeObject1(self):
        vertices = [-0.5, -0.5, 0.5, 1.0, 0.0, 0.0,
                    0.5, -0.5, 0.5, 0.0, 1.0, 0.0,
                    0.5, 0.5, 0.5, 0.0, 0.0, 1.0,
                    -0.5, 0.5, 0.5, 1.0, 1.0, 0.0,

                    -0.5, -0.5, -0.5, 1.0, 0.0, 1.0,
                    0.5, -0.5, -0.5, 0.0, 1.0, 1.0,
                    0.5, 0.5, -0.5, 1.0, 1.0, 0.0,
                    -0.5, 0.5, -0.5, 1.0, 1.0, 1.0]

        indices = [0, 1, 2, 2, 3, 0,
                   4, 5, 6, 6, 7, 4,
                   4, 5, 1, 1, 0, 4,
                   6, 7, 3, 3, 2, 6,
                   5, 6, 2, 2, 1, 5,
                   7, 4, 0, 0, 3, 7]

        vertices = np.array(vertices, dtype=np.float32)
        indices = np.array(indices, dtype=np.uint32)

        return vertices, indices

    ######### Pyramide ergänzen

    def pyramidObject1(self):
        vertices = [
            # VerA: links vorne
            -0.5, -0.5, -0.5, 1.0, 0.0, 1.0,
            # VerB: rechts vorne
            0.5, -0.5, -0.5, 0.0, 1.0, 1.0,
            # verC: links hinten
            -0.5, 0.5, -0.5, 1.0, 1.0, 0.0,
            # VerD: rechts hinten
            0.5, 0.5, -0.5, 1.0, 1.0, 1.0,
            # VerE: Spitze
            0.0, 0.0, 1.0, 1.0, 1.0, 0.0
        ]

        indices = [
            0, 1, 2, 2, 3, 1,  # Flaeche hinten
            0, 1, 4,  # Flaeche vorne
            2, 3, 4,  # Flaeche hinten
            1, 3, 4,  # Flaehce rechts
            0, 2, 4  # flaeche linmks

        ]

        vertices = np.array(vertices, dtype=np.float32)
        indices = np.array(indices, dtype=np.uint32)

        return vertices, indices

########
