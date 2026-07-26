import { useEffect, useState } from "react";
import {
  ArrowRight,
  Check,
  Home,
  Building2,
  Sparkles,
  Menu,
  X,
} from "lucide-react";
import "./App.css";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

const services = [
  {
    title: "Home Cleaning",
    description:
      "Consistent, detail-focused cleaning for kitchens, bathrooms, bedrooms, and living spaces.",
    icon: Home,
  },
  {
    title: "Deep Cleaning",
    description:
      "A thorough top-to-bottom service for spaces that need extra time, care, and attention.",
    icon: Sparkles,
  },
  {
    title: "Office Cleaning",
    description:
      "Flexible cleaning services designed to keep your workplace fresh and professional.",
    icon: Building2,
  },
];

function App() {
  const [apiStatus, setApiStatus] = useState("checking");
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    async function checkApi() {
      try {
        const response = await fetch(`${API_URL}/health`);

        if (!response.ok) {
          throw new Error("API request failed");
        }

        const data = await response.json();
        setApiStatus(data.status);
      } catch (error) {
        console.error("Could not connect to the API:", error);
        setApiStatus("unavailable");
      }
    }

    checkApi();
  }, []);

  function closeMenu() {
    setMenuOpen(false);
  }

  return (
    <>
      <header className="site-header">
        <a className="brand" href="#top" onClick={closeMenu}>
          <span className="brand-mark">CT</span>
          <span className="brand-name">Clean Tangerine</span>
        </a>

        <button
          className="menu-button"
          type="button"
          aria-label="Toggle navigation"
          aria-expanded={menuOpen}
          onClick={() => setMenuOpen((current) => !current)}
        >
          {menuOpen ? <X size={26} /> : <Menu size={26} />}
        </button>

        <nav className={`navigation ${menuOpen ? "navigation-open" : ""}`}>
          <a href="#services" onClick={closeMenu}>
            Services
          </a>

          <a href="#about" onClick={closeMenu}>
            About
          </a>

          <a href="#reviews" onClick={closeMenu}>
            Reviews
          </a>

          <a className="nav-button" href="#quote" onClick={closeMenu}>
            Get a quote
          </a>
        </nav>
      </header>

      <main id="top">
        <section className="hero">
          <div className="hero-content">
            <p className="eyebrow">Residential and commercial cleaning</p>

            <h1>A brighter kind of clean.</h1>

            <p className="hero-description">
              Reliable, detail-focused cleaning services that leave your home
              or office fresh, comfortable, and ready to enjoy.
            </p>

            <div className="hero-actions">
              <a className="button button-primary" href="#quote">
                Request a free quote
                <ArrowRight size={18} />
              </a>

              <a className="button button-secondary" href="tel:+14155550199">
                Call us
              </a>
            </div>

            <div className="trust-list">
              <span>
                <Check size={18} />
                Insured
              </span>

              <span>
                <Check size={18} />
                Background checked
              </span>

              <span>
                <Check size={18} />
                Satisfaction focused
              </span>
            </div>

            <p className={`api-status api-status-${apiStatus}`}>
              API: {apiStatus}
            </p>
          </div>

          <div className="hero-image-container">
            <div className="hero-image">
              <div className="hero-card">
                <span className="hero-card-icon">✦</span>

                <div>
                  <strong>Fresh space.</strong>
                  <span>Clear mind.</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section className="services-section" id="services">
  <div className="services-heading">
    <div>
      <p className="eyebrow">Our services</p>
      <h2>Professional cleaning for every space.</h2>
    </div>

    <p className="services-intro">
      Straightforward cleaning services tailored to your home, workplace,
      schedule, and priorities.
    </p>
  </div>

  <div className="services-grid">
    {services.map((service) => {
      const Icon = service.icon;

      return (
        <article className="service-card" key={service.title}>
          <div className="service-icon">
            <Icon size={24} />
          </div>

          <h3>{service.title}</h3>
          <p>{service.description}</p>

          <a href="#quote">
            Get a quote
            <ArrowRight size={16} />
          </a>
        </article>
      );
    })}
  </div>
</section>
      </main>
    </>
  );
}

export default App;