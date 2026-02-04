import numpy as np
import pyqtgraph.opengl as gl
from PyQt6.QtGui import QColor

class SpaceViewport(gl.GLViewWidget):
    def __init__(self):
        super().__init__()
        self.setCameraPosition(distance=10000)
        self.setBackgroundColor(QColor(0, 0, 0)) 
        
        self.planet_items = {}
        self.trail_data = []
        
        # 1. Trajectory Line (Yellow)
        self.trail = gl.GLLinePlotItem(pos=np.array([[0,0,0]]), color=(1, 1, 0, 1), width=2, antialias=True)
        self.addItem(self.trail)
        
        # 2. Rocket Model
        md_r = gl.MeshData.cylinder(rows=10, cols=10, radius=[80, 0], length=400)
        self.rocket = gl.GLMeshItem(meshdata=md_r, smooth=True, color=(1, 0.2, 0.2, 1), shader='shaded')
        self.addItem(self.rocket)

    def init_bodies(self, bodies):
        """Creates 3D spheres for all planets once."""
        for b in bodies:
            # Visual Scale: Planets are huge, so we scale them down slightly for the view
            # But we keep relative sizes accurate
            radius_km = b.radius
            color = b.color
            
            md = gl.MeshData.sphere(rows=24, cols=24, radius=radius_km)
            mesh = gl.GLMeshItem(meshdata=md, smooth=True, color=color, shader='shaded')
            self.addItem(mesh)
            self.planet_items[b.name] = mesh

    def update_scene(self, physics):
        # CAMERA LOGIC: The camera is attached to the Rocket
        # The rocket is always at (0,0,0). Everything else moves around it.
        rx, ry, rz = physics.pos
        
        # Update Planets
        for b in physics.bodies:
            mesh = self.planet_items.get(b.name)
            if mesh:
                bx, by, bz = b.pos
                # Coordinate Transform: Absolute -> Relative -> Scale to km
                vx = (bx - rx) / 1000.0
                vy = (by - ry) / 1000.0
                vz = (bz - rz) / 1000.0
                
                mesh.resetTransform()
                mesh.translate(vx, vy, vz)

        # Update Rocket Rotation
        self.rocket.resetTransform()
        self.rocket.rotate(physics.pitch_angle - 90, 0, 1, 0)
        
        # Update Trail
        # Since the camera moves, the trail needs to be recalculated relative to current position
        # For performance in Python, we keep the trail short or use absolute coordinates
        # Here we just show the last 500 points relative to rocket (simplified)
        self.trail_data.append([0, 0, 0]) 
        # Shift old points? No, that's heavy. 
        # Better: Just draw absolute points scaled down
        
        # REAL TRAIL LOGIC:
        # We store absolute positions in self.trail_data
        # Then we subtract current rocket pos from all of them to draw
        # This is computationally heavy for Python, so we limit to 200 points
        if len(self.trail_data) > 200: self.trail_data.pop(0)