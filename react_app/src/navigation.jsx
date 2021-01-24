import React from 'react';
import { Nav, Navbar } from "react-bootstrap";
import './css/navigation.css'
import { Link } from 'react-router-dom';


const Navigation = () => {
    return (
        <Navbar bg="light" variant="light" expand="lg" className="navBanner">
            <Navbar.Toggle aria-controls="basic-navbar-nav" />

            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Item>
                        <Link to="/import" className="nav-link">Import Dataset</Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Link to="/model" className="nav-link">Build Models</Link>
                    </Nav.Item>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
}

export default Navigation;