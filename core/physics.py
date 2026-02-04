import numpy as np

class CelestialBody:
    def __init__(self, name, mass, radius, color, dist_from_sun_au, orbital_vel_km_s):
        self.name = name
        self.mass = mass
        self.radius = radius # km
        self.color = color
        
        # Astronomical Unit (AU) to Meters
        AU = 149.6e6 * 1000.0
        self.pos = np.array([dist_from_sun_au * AU, 0.0, 0.0], dtype=np.float64)
        
        # Velocity (m/s)
        self.vel = np.array([0.0, orbital_vel_km_s * 1000.0, 0.0], dtype=np.float64)

class PhysicsEngine:
    def __init__(self):
        self.G = 6.67430e-11
        
        # --- THE FULL SOLAR SYSTEM ---
        # Data: Mass (kg), Radius (km), Color (RGBA), Dist (AU), Vel (km/s)
        self.bodies = [
            CelestialBody("Sun", 1.989e30, 696340, (1, 1, 0, 1), 0, 0),
            CelestialBody("Mercury", 3.285e23, 2439, (0.5, 0.5, 0.5, 1), 0.39, 47.87),
            CelestialBody("Venus", 4.867e24, 6051, (0.9, 0.8, 0.6, 1), 0.72, 35.02),
            CelestialBody("Earth", 5.972e24, 6371, (0, 0.4, 1, 1), 1.00, 29.78),
            CelestialBody("Mars", 6.39e23, 3389, (1, 0.2, 0, 1), 1.52, 24.07),
            CelestialBody("Jupiter", 1.898e27, 69911, (0.9, 0.7, 0.5, 1), 5.20, 13.07),
            CelestialBody("Saturn", 5.683e26, 58232, (0.8, 0.7, 0.4, 1), 9.58, 9.69),
            CelestialBody("Uranus", 8.681e25, 25362, (0.4, 0.9, 1, 1), 19.22, 6.81),
            CelestialBody("Neptune", 1.024e26, 24622, (0.2, 0.2, 1, 1), 30.05, 5.43)
        ]
        
        # Add Moon manually relative to Earth
        earth = self.bodies[3]
        moon_pos = earth.pos + np.array([384400000.0, 0, 0])
        moon_vel = earth.vel + np.array([0, 1022.0, 0])
        moon = CelestialBody("Moon", 7.348e22, 1737, (0.8, 0.8, 0.8, 1), 0, 0)
        moon.pos = moon_pos
        moon.vel = moon_vel
        self.bodies.append(moon)
        
        self.rocket_mass = 50000.0
        self.fuel = 100.0
        self.max_thrust = 7600000.0
        
        self.reset()

    def configure(self, config):
        self.rocket_mass = config.get('mass', 50000.0)
        self.fuel = config.get('fuel', 100.0)
        self.max_thrust = config.get('thrust', 7600000.0)

    def reset(self):
        earth = self.bodies[3]
        # Launch Pad: Slightly off surface to avoid immediate collision
        self.pos = earth.pos + np.array([earth.radius * 1000.0 + 50, 0, 0])
        self.vel = np.copy(earth.vel)
        
        self.thrust_level = 0.0
        self.pitch_angle = 90.0
        self.status = "READY"

    def step(self, dt):
        if self.status in ["CRASHED", "LANDED"]: return self.status

        # 1. Gravity Summation
        total_gravity = np.array([0.0, 0.0, 0.0])
        nearest_body = None
        min_dist = float('inf')

        for body in self.bodies:
            r_vec = body.pos - self.pos
            r_mag = np.linalg.norm(r_vec)
            
            if r_mag < min_dist:
                min_dist = r_mag
                nearest_body = body

            force = (self.G * body.mass) / (r_mag**2)
            total_gravity += (r_vec / r_mag) * force
            
            # Update Planet Position (Simplified Orbit)
            if body.name != "Sun":
                # Very simple Euler update for planets
                r_sun = self.bodies[0].pos - body.pos
                d_sun = np.linalg.norm(r_sun)
                f_sun = (self.G * self.bodies[0].mass) / (d_sun**2)
                acc_sun = (r_sun / d_sun) * f_sun
                body.vel += acc_sun * dt
                body.pos += body.vel * dt

        # 2. Collision Check
        surface_dist = min_dist - (nearest_body.radius * 1000.0)
        if surface_dist <= 1.0:
            rel_speed = np.linalg.norm(self.vel - nearest_body.vel)
            if rel_speed > 20.0:
                self.status = "CRASHED"
            else:
                self.status = "LANDED"
            return self.status

        # 3. Thrust Calculations
        acc_thrust = np.array([0.0, 0.0, 0.0])
        if self.fuel > 0 and self.thrust_level > 0:
            # Local Coordinate System for Steering
            radial = (self.pos - nearest_body.pos) / min_dist
            tangent = np.array([-radial[1], radial[0], 0])
            
            # Pitch Logic
            rads = np.radians(self.pitch_angle)
            direction = (radial * np.sin(rads)) + (tangent * np.cos(rads))
            
            force = direction * (self.thrust_level * self.max_thrust)
            acc_thrust = force / self.rocket_mass
            self.fuel -= self.thrust_level * 0.1 * dt

        # 4. Integrate
        self.vel += (total_gravity + acc_thrust) * dt
        self.pos += self.vel * dt
        
        return "FLYING"

    def get_telemetry(self):
        # Find nearest for reference
        nearest = min(self.bodies, key=lambda b: np.linalg.norm(self.pos - b.pos))
        dist = np.linalg.norm(self.pos - nearest.pos) - (nearest.radius * 1000)
        speed = np.linalg.norm(self.vel - nearest.vel)
        return {
            "alt": dist, 
            "vel": speed, 
            "fuel": self.fuel, 
            "nearest": nearest.name,
            "x": self.pos[0],
            "y": self.pos[1]
        }