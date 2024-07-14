import {BrowserRouter, Routes , Route, Link } from "react-router-dom" 
import {useState, useContext} from 'react'
import './static/css/App.css'

import { AuthProvider } from './components/accounts/AuthContext'

import Login from './components/accounts/Login'
import Logout from './components/accounts/Logout'
import Register from './components/accounts/Register'
import Navbar from './components/global/Navbar'
import ProductNavbar from "./components/global/ProductNavbar"
import Footer from './components/global/Footer'
import Profile from './components/accounts/Profile'
import UserSettings from './components/accounts/UserSettings'

import Catalog from "./components/catalog/Catalog"
import Product from "./components/Product/Product"

import Checkout from "./components/checkout/Checkout"
import Cart from "./components/checkout/Cart"

import Home from './components/Index/Home'


function App() {
  const [announcement, setAnnouncement] = useState(
    {"announcement":"FREE SHIPPING ON ORDERS $50+", "href":null}

  ) 
  return (
    <>
      {announcement.announcement && ( 
        <div className="items-center bg-slate-300 announcement">
          <div className="text-center">
            <a href={announcement.href}>
              <b>{announcement.announcement}</b>
            </a>
          </div>
        </div>
      )}

      <AuthProvider>
        <div className="App">
          <Navbar />
          <ProductNavbar />
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/login" element={<Login />} />
              <Route path="/logout" element={<Logout />} />
              <Route path="/register" element={<Register />} />
              <Route path="/profile" element={<Profile/>} />
              <Route path="/user-settings" element={<UserSettings />} />


              {/* For Development */}
              <Route path="/catalog" element={<Catalog />} />
              <Route path="/catalog/publishers" element={<Catalog />} />
              <Route path="/catalog/publishers/:searchCategory" element={<Catalog />} />
              <Route path="/catalog/timeera" element={<Catalog />} />
              <Route path="/catalog/timeera/:searchCategory" element={<Catalog />} />
              <Route path="/catalog/miscellaneous" element={<Catalog />} />
              <Route path="/catalog/miscellaneous/:searchCategory" element={<Catalog />} />
              <Route path="/catalog/sale" element={<Catalog />} />
              <Route path="/catalog/sale/:searchCategory" element={<Catalog />} />


              {/* <Route path="/product" element={<Product />} /> */}
              <Route path="/product/:itemID" element={<Product />} />

              <Route path="/cart" element={<Cart />} />
              <Route path="/checkout" element={<Checkout />} />
            </Routes>
          {/* <Footer /> */}
        </div>
      </AuthProvider>
    </>
  );
}

export default App;
