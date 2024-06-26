import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
    return (
        <header>
            <h1>NetNest E-Commerce</h1>
            <nav>
                <Link to="/">Home</Link>
                <Link to="/cart">Cart</Link>
                <Link to="/profile">Profile</Link>
            </nav>
        </header>
    );
}

export default Header;
