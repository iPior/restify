import {BrowserRouter, Route, Routes} from "react-router-dom";
import MainFeed from "../Feed/MainFeed";
import Search from "../Search";
import MyRestaurantBlog from "../MyRestaurant/Blog";
import Profile from "../Profile";
import Login from "../Login"
import Layout from "../Layout"


const Router = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Layout />}>
                    <Route index element={<MainFeed />} />
                    <Route path="search" element={<Search />} />
                    <Route path="myrestaurant" element={<MyRestaurantBlog />} />
                    <Route path="profile" element={<Profile />} />
                    <Route path="login" element={<Login />} />
                </Route>
            </Routes>
        </BrowserRouter>
    )
}

export default Router