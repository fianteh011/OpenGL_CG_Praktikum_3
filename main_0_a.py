import glfw
import numpy as np
from glfwUtils import GlfwUtils
from OpenGL.GL import *
from openGLUtils import OpenGLUtils

TEST = True


def main2():
    # Fenstersystem glfw initialisieren
    def window_resize(window, width, height):
        glViewport(0, 0, width, height)

    window = GlfwUtils().initWindow(1600, 1200)

    glfw.set_window_size_callback(window, window_resize)

    # Systeminfo zur OpenGL-version
    if TEST:
        OpenGLUtils.printSystemInfo()

    # vertex-shader code einlesen
    vsCode = open("vsCode0.txt", 'r').read()
    # fragment-shade code einlesen
    # referenz auf fragment shader
    fsCode = open("fs_simple.txt", 'r').read()
    # shader compile und OpenGL initialisiren
    programRef = OpenGLUtils().initializeProgram(vsCode, fsCode)

    # referenz auf das initialisierte Programm, ausgelagert auf GPU-Einheit laufen soll
    glUseProgram(programRef)

    # Geometrie einrichten / Darstellung einrichten -> OpenGl Buffer anlegen
    # (direkt oder siehe Klasse Geometry)

    # direkte Variante: Geometrie/Material erzeugen und einbinden
    # Ecpunkte des Dreiecks in der (x,y) - Ebene


            #
    vertices = [-0.5, -0.5, 0.0,
                0.5, -0.5, 0.0,
                0.0, 0.5, 0.0]
    vertices = np.array(vertices, dtype=np.float32)  # in einem numpy array stecken mit float 32

    vert_anz = np.floor_divide(len(vertices), 3)  # vertex anzahl

    VBO = glGenBuffers(1)
    # Zustandsautomat, durch das Binden dieses Buffers, wird der entsprechende Zustand verarbeitet
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    # Transportiert das ganze auf die Grafikkarte zur Verarbeitung mit der GPU
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # Check that name is a string with a null byte at the end of it
    position = glGetAttribLocation(programRef, "a_position")  # wird als a_position angesprochen
    glEnableVertexAttribArray(position)
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

    # ObjektBuffer für Farben
    # R G B
    # In diesem Fall ist hier ROT
    f_array = [1.0, 0.0, 0.0,
               1.0, 1.0, 0.0,
               1.0, 0.0, 0.0]
    color_v = np.array(f_array, dtype=np.float32)
    CBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, CBO)
    glBufferData(GL_ARRAY_BUFFER, color_v.nbytes, color_v, GL_STATIC_DRAW)

    color = glGetAttribLocation(programRef, "a_color")
    glEnableVertexAttribArray(color)
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
    # GL_False stellt sicher, dass es nicht weiter abgeschnitten werden und fangen von Position 0 an

    # elementare Render- settings: Hintergrundfarbe,
    # Tiefenputterauswertung initialisieren
    glClearColor(0.8, 0.8, 0.8, 1)
    # 3D arbeiten, wird ein tiefen Test zugeschaltet
    glEnable(GL_DEPTH_TEST)

    # Programm-Loop
    while not glfw.window_should_close(window):
        glfw.poll_events()  # holt Nutzer aktion u.ä. ab , was außerhalb noch abläuft
        # Buffer fuer color geleert
        # tiefen buffer fuer den tiefen Test
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        ### Hier OpenGL-Routin tn zur Objektmanipulation und zum Zeichen einfügen

        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(window)

    # fenstersystem glfw beenden, allkierte Ressourcen freigeben
    glfw.terminate()


if __name__ == '__main__':
    main2()
