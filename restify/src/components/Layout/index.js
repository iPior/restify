import {Link, Outlet} from "react-router-dom";

const Layout = () => {
    return <>
        <nav>
            <Link to="/">MainFeed</Link>
            <Link to="/search">Search</Link>
            <Link to="/myrestaurant">MyRestaurant</Link>
            <Link to="/profile">Profile</Link>
            <Link to="/login">Login</Link>
        </nav>

        <Outlet />
    </>
}

export default Layout