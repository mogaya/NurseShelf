import { useState } from "react";
import {
  Navbar,
  Nav,
  Container,
  Button,
  Modal,
  Form,
  FormControl,
} from "react-bootstrap";
import { useNavigate } from "react-router-dom"; // Import useNavigate

const AppNavbar = () => {
  const [show, setShow] = useState(false);
  const [isSignup, setIsSignup] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const navigate = useNavigate(); // Initialize navigation

  const handleClose = () => setShow(false);
  const handleShow = (signup: boolean) => {
    setIsSignup(signup);
    setShow(true);
  };

  const handleLogin = (event: React.FormEvent) => {
    event.preventDefault();
    setIsLoggedIn(true); // Simulating login (replace with actual authentication)
    setShow(false);
    navigate("/"); // Redirect to Home after login
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
    navigate("/"); // Redirect to Home after logout
  };

  return (
    <>
      {/* Navbar */}
      <Navbar bg="primary" variant="dark" expand="lg">
        <Container>
          <Navbar.Brand href="/">NurseShelf</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            {isLoggedIn ? (
              <>
                <Nav className="me-auto">
                  <Nav.Link href="/">Home</Nav.Link>
                  <Nav.Link href="/categories">Categories</Nav.Link>
                  <Nav.Link href="/subscriptions">Subscriptions</Nav.Link>
                  <Nav.Link href="/support">Support</Nav.Link>
                </Nav>
                <Form className="d-flex">
                  <FormControl
                    type="search"
                    placeholder="Search notes..."
                    className="me-2"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                  />
                  <Button variant="light">Search</Button>
                </Form>
                <Button
                  variant="outline-light"
                  className="ms-3"
                  onClick={handleLogout}
                >
                  Logout
                </Button>
              </>
            ) : (
              <Nav className="ms-auto">
                <Button
                  variant="outline-light"
                  className="me-2"
                  onClick={() => handleShow(false)}
                >
                  Login
                </Button>
                <Button variant="light" onClick={() => handleShow(true)}>
                  Sign Up
                </Button>
              </Nav>
            )}
          </Navbar.Collapse>
        </Container>
      </Navbar>

      {/* Login & Sign Up Modal */}
      <Modal show={show} onHide={handleClose} centered>
        <Modal.Header closeButton>
          <Modal.Title>{isSignup ? "Sign Up" : "Login"}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form onSubmit={handleLogin}>
            {isSignup && (
              <Form.Group className="mb-3">
                <Form.Label>Full Name</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Enter your full name"
                  required
                />
              </Form.Group>
            )}
            <Form.Group className="mb-3">
              <Form.Label>Email address</Form.Label>
              <Form.Control type="email" placeholder="Enter email" required />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter password"
                required
              />
            </Form.Group>
            <Button variant="primary" type="submit" className="w-100">
              {isSignup ? "Sign Up" : "Login"}
            </Button>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <small>
            {isSignup ? "Already have an account?" : "Don't have an account?"}{" "}
            <span
              style={{ cursor: "pointer", color: "blue" }}
              onClick={() => handleShow(!isSignup)}
            >
              {isSignup ? "Login" : "Sign Up"}
            </span>
          </small>
        </Modal.Footer>
      </Modal>
    </>
  );
};

export default AppNavbar;
