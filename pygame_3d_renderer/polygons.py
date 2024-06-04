from pygame import Vector3

vertices_cube = {"A": Vector3(0, 0, 0), "B": Vector3(1, 0, 0),
                 "C": Vector3(0, 0, 1), "D": Vector3(1, 0, 1),
                 "E": Vector3(0, 1, 0), "F": Vector3(1, 1, 0),
                 "G": Vector3(0, 1, 1), "H": Vector3(1, 1, 1)}
edges_cube = {"AB", "AC", "BD", "CD", "EF", "EG", "FH", "GH", "AE", "BF", "CG", "DH"}
faces_cube = {"ABCD", "ABEF", "CDGH", "EFGH", "ACEG", "BDFH"}

vertices_pyramide = {"A": Vector3(0, 0, 0), "B": Vector3(1, 0, 0),
                     "C": Vector3(0, 0, 1), "D": Vector3(1, 0, 1),
                     "E": Vector3(0.5, 1, 0.5)}
edges_pyramide = {"AB", "AC", "BD", "CD", "AE", "BE", "CE", "DE"}
faces_pyramide = {"ABCD", "ABE", "ACE", "DBE", "DCE"}

vertices_plan = {"A": Vector3(0, 0, 0), "B": Vector3(1, 0, 0),
                 "C": Vector3(0, 0, 1), "D": Vector3(1, 0, 1)}
edges_plan = {"AB", "AC", "BD", "CD"}
faces_plan = {"ABCD"}

polygons = {"cube": {"vertices": vertices_cube, "edges": edges_cube, "faces": faces_cube},
            "pyramide": {"vertices": vertices_pyramide, "edges": edges_pyramide, "faces": faces_pyramide},
            "plan": {"vertices": vertices_plan, "edges": edges_plan, "faces": faces_plan}}
