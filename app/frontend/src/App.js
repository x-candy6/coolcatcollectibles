import {BrowserRouter, Routes , Route, Link } from "react-router-dom" 

import logo from './static/media/images/logo.svg';
import './static/css/App.css'

import { AuthProvider } from './components/accounts/AuthContext'

import Login from './components/accounts/Login'
import Logout from './components/accounts/Logout'
import Register from './components/accounts/Register'
import Home from './components/home/Home'
import Navbar from './components/global/Navbar'
import Footer from './components/global/Footer'
import Profile from './components/accounts/Profile'
import Settings from './components/accounts/Settings'
import { useContext } from "react";

import InventoryManagement from "./components/dashboards/InventoryManagement";
import GeneralInventory from "./components/inventory/GeneralInventory";

import Analytics from "./components/dashboards/Analytics"
import CustomerService from "./components/dashboards/CustomerService"
import Experimental from "./components/dashboards/Experimental"
import Fulfillment from "./components/dashboards/Fulfillment"
import Procurement from "./components/dashboards/Procurement"
import PublicRelations from "./components/dashboards/PublicRelations"

import Storefronts from "./components/dashboards/Storefronts"
import StoreHome from "./components/store/home/StoreHome"

function App() {

  return (
    <AuthProvider>
      <div className="App">
        <Navbar />
            <Routes>
              <Route path="/" element={<Home/> } />
              <Route path="/login" element={<Login/> } />
              <Route path="/logout" element={<Logout/> } />
              <Route path="/register" element={<Register/> } />
              <Route path="/profile" element={<Profile/> } />
              <Route path="/settings" element={<Settings/> } />

              <Route path="/inventory-management" element={<InventoryManagement />} />
              <Route path="/general-inventory" element={<GeneralInventory/>} />



              <Route path="/analytics" element={<Analytics />}></Route>
              <Route path="/customer-service" element={<CustomerService />}></Route>
              <Route path="/experimental" element={<Experimental/>}></Route>
              <Route path="/fulfillment" element={<Fulfillment />}></Route>
              <Route path="/procurement" element={<Procurement/>}></Route>
              <Route path="/public-relations" element={<PublicRelations/>}></Route>

              <Route path="/storefronts" element={<Storefronts/>}></Route>
              <Route path="/coolcatcollectiblesshop" element={<StoreHome/>}></Route>

            </Routes>
        <Footer />
      </div>
    </AuthProvider>
  );
}

export default App;
