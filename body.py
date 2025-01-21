class Body:
  def __init__(
    self,
    name,
    mass,
    sma=None,
    eccentricity=None,
    soi=None,
    parent_body=None
  ):
    """
    Initialize a celestial body.
    
    Args:
      name<str>: Name of the celestial body.
      mass<float>: Mass of the celestial body (kg)
      radius<float>: Radius of the body (m)
      sma<float, optional>: Semi-major axis of the body's orbit around its parent. Defaults to None.
      eccentricity<float, optional>: Eccentricity of the body's orbit around its parent. Defaults to None.
      soi<float, optional>: Radius of the body's sphere of influence (m). Defaults to None.
      parent_body<float, optional>: The celestial body this body orbits. Defaults to None.
      TODO:
      mean_radius,
      flattening,
      surface_area,
      volume,
      density,
      surface_gravity,
      moment_of_inertia_factor,
      escape_velocity,
      """
    self.name = name
    # Physical characteristics
    self.mass = mass
    self.radius = radius
    # Orbital characteristics
    self.sma = sma
    self.soi = soi
    self.parent_body = parent_body

    @property
    def gm(self):
      """Lazily calculate and cache the standard gravitational parameter (GM)."""
      G = 6.67430e-11 # m^3/kg/s^2
      return G * self.mass
    
    def orbital_period(self):
        """
        Calculate the orbital period of the body around its parent.
        Requires orbit_radius and parent_body to be defined.
        """
        if self.orbit_radius is None or self.parent_body is None:
            raise ValueError(f"Cannot calculate orbital period for {self.name}. Missing orbit_radius or parent_body.")
        G = 6.67430e-11  # m^3/kg/s^2
        mu = self.parent_body.calculate_gravitational_parameter()
        return 2 * 3.14159 * (self.orbit_radius**3 / mu)**0.5
    def __repr__(self):
        return f"Body(name={self.name}, mass={self.mass:.2e}, radius={self.radius:.2e}, orbit_radius={self.orbit_radius}, soi={self.soi})"