import traceback
import numpy as np

class MissionRuntime:
    def __init__(self, physics_engine, logger_func):
        self.physics = physics_engine
        self.log = logger_func
        self.context = {}
        self.is_active = False

    def compile_script(self, script_text):
        # --- API EXPOSED TO USER ---
        class RocketAPI:
            def set_thrust(s, val):
                # 0.0 to 1.0
                self.physics.thrust_level = max(0.0, min(1.0, float(val)))
            
            def set_pitch(s, deg):
                # 90 = Vertical, 0 = Horizontal
                self.physics.pitch_angle = float(deg)

            def get_altitude(s):
                # The Physics engine now returns a DICTIONARY
                # We need to access ['alt'] instead of unpacking a tuple
                data = self.physics.get_telemetry()
                return data['alt'] / 1000.0 # Return in km
            
            def get_velocity(s):
                data = self.physics.get_telemetry()
                return data['vel'] # Return in m/s

            def log(s, msg):
                self.log(f"USER: {msg}")

        self.context = {
            'rocket': RocketAPI(),
            'print': lambda m: self.log(f"PRINT: {m}"),
            'math': __import__('math')
        }

        try:
            exec(script_text, self.context)
            if 'mission_loop' not in self.context:
                raise Exception("Script must define 'def mission_loop():'")
            self.is_active = True
            return True
        except Exception as e:
            self.log(f"SYNTAX ERROR: {e}")
            traceback.print_exc()
            return False

    def execute_step(self):
        if self.is_active and 'mission_loop' in self.context:
            try:
                self.context['mission_loop']()
            except Exception as e:
                self.log(f"RUNTIME ERROR: {e}")
                self.is_active = False