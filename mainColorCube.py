#### Grundversion: Würfel mit Farben in OpenGL ####
#### Ohne Interaktion #############################
import glfw
from OpenGL.GL import *
from glfwUtils import GlfwUtils
from openGLUtils import OpenGLUtils
from geometry import Geometry
from matrix import Matrix
from math import pi
from OpenGL.raw.GL.VERSION.GL_2_0 import glUseProgram


def main():
    WIDTH, HEIGHT = 2560, 2560

    #### Shader aus Datei laden
    # vertex shader code einlesen
    vsCode = open("vs_simple.txt", 'r').read()

    # fragment shader code einlesen
    fsCode = open("fs_simple.txt", 'r').read()

    # Ausgabefenster initialisieren
    window = GlfwUtils().initWindow(WIDTH, HEIGHT)

    # glfw callback functions
    def window_resize(window, width, height):
        glViewport(0, 0, width, height)
        projection = Matrix.makePerspective(45, WIDTH / HEIGHT, 0.1, 100)
        glUniformMatrix4fv(proj_loc, 1, GL_TRUE, projection)

    # set the callback function for window resize
    glfw.set_window_size_callback(window, window_resize)

    #### Anwendung initialisieren
    programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
    glUseProgram(programRef)

    #### Geometrie/Objekte laden

    # für mac osx vao initialisieren
    # vaoRef = glGenVertexArrays(1)
    # glBindVertexArray(vaoRef)
    #

    geometrie = Geometry()
    # Wuerfel erstellen
    cube_vertices, cube_indices = geometrie.cubeObject1()

    # Pyramide erstellen
    pyramid_vertices, pyramid_indices = geometrie.pyramidObject1()

    # Vertex Buffer Object
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    # glBufferData(GL_ARRAY_BUFFER, cube_vertices.nbytes, cube_vertices, GL_STATIC_DRAW)
    # glBufferData(GL_ARRAY_BUFFER, pyramid_vertices.nbytes, pyramid_vertices, GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

    # Element Buffer Object
    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    # glBufferData(GL_ELEMENT_ARRAY_BUFFER, cube_indices.nbytes, cube_indices, GL_STATIC_DRAW)
    # glBufferData(GL_ELEMENT_ARRAY_BUFFER, pyramid_indices, pyramid_indices, GL_STATIC_DRAW)

    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    #### OpenGl Parameter setzen
    glClearColor(0.5, 0.5, 0.5, 1)
    glEnable(GL_DEPTH_TEST)

    #### Transformations-Pipeline einrichten
    projection = Matrix.makePerspective(45, WIDTH / HEIGHT, 0.1, 100)
    model = Matrix.makeIdentity()

    # Drehung des Objekts
    # model = Matrix.multiply(model, Matrix.makeRotationX(pi / 4))
    # model = Matrix.multiply(model, Matrix.makeRotationY(pi / 3))

    # Pyramide
    # Spitze nach oben zeigt
    model = Matrix.multiply(model, Matrix.makeRotationX(-1.0))
    model = Matrix.multiply(model, Matrix.makeRotationZ(2.0))

    # eye, target, up: Look_at_Matrix
    view = Matrix.makeLook_at(Matrix.Vec3(0, 0, 5), Matrix.Vec3(0, 0, 0), Matrix.Vec3(0, 1, 0))
    ################################ Augpunkt, eye = e    # target = t          u = up-vector

    # shader-Verbindung einrichten
    model_loc = glGetUniformLocation(programRef, "model")
    proj_loc = glGetUniformLocation(programRef, "projection")
    view_loc = glGetUniformLocation(programRef, "view")

    glUniformMatrix4fv(proj_loc, 1, GL_TRUE, projection)
    glUniformMatrix4fv(model_loc, 1, GL_TRUE, model)
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

    #### Anwendung (application loop) starten
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #########################################################

        # Wuerfel
        # Wuerfel darstellen
        glBufferData(GL_ARRAY_BUFFER, cube_vertices.nbytes, cube_vertices, GL_STATIC_DRAW)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, cube_indices.nbytes, cube_indices, GL_STATIC_DRAW)
        glDrawElements(GL_TRIANGLES, len(cube_indices), GL_UNSIGNED_INT, None)

        # Wuerfel drehen permanent um die X-Achse
        # model = Matrix.multiply(model, Matrix.makeRotationX(pi / 5000))
        # glUniformMatrix4fv(model_loc, 1, GL_TRUE, model)

        #########################################################

        # Pyramide darstellen
        glBufferData(GL_ARRAY_BUFFER, pyramid_vertices.nbytes, pyramid_vertices, GL_STATIC_DRAW)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, pyramid_indices.nbytes, pyramid_indices, GL_STATIC_DRAW)

        glDrawElements(GL_TRIANGLES, len(pyramid_indices), GL_UNSIGNED_INT, None)

        # Pyramid Drehen bzw. rotieren
        model = Matrix.multiply(model, Matrix.makeRotationZ(pi / 500))
        glUniformMatrix4fv(model_loc, 1, GL_TRUE, model)

        #########################################################

        glfw.swap_buffers(window)
    # terminate glfw, free up allocated resources
    glfw.terminate()


if __name__ == '__main__':
    main()
