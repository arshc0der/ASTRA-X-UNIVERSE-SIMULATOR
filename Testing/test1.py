def mission_loop():
    # 1. GET DATA
    # The system now handles the complex dictionary math for you
    alt_km = rocket.get_altitude()
    vel = rocket.get_velocity()
    
    # 2. FLIGHT PLAN
    
    # PHASE A: LIFTOFF (Vertical Climb)
    if alt_km < 50:
        rocket.set_pitch(90) # Straight up
        rocket.set_thrust(1.0) # Full Power
        
    # PHASE B: GRAVITY TURN (Tilt to start orbiting)
    elif alt_km < 150:
        rocket.set_pitch(60) # Tilt 60 degrees
        rocket.set_thrust(1.0)
        
    # PHASE C: ORBITAL INSERTION (Go sideways fast)
    elif alt_km < 500:
        rocket.set_pitch(20) # Low angle
        rocket.set_thrust(1.0)
        
    # PHASE D: ESCAPE BURN (Leave Earth)
    # Escape velocity is roughly 11,200 m/s
    elif vel < 11500:
        rocket.set_pitch(0) # Horizontal burn
        rocket.set_thrust(1.0)
        
        # Log progress every 1000 m/s
        if int(vel) % 1000 == 0:
            rocket.log(f"ACCELERATING TO ESCAPE VELOCITY: {vel:.0f} m/s")
            
    # PHASE E: CRUISE (Coast to Mars/Void)
    else:
        rocket.set_thrust(0.0) # Engine off
        rocket.log("EARTH ESCAPE ACHIEVED. ENTERING HELIOCENTRIC ORBIT.")