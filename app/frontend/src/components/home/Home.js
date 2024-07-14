import { AuthContext } from '../accounts/AuthContext'
import { Link } from 'react-router-dom';
import Card from '../global/Card';
import  { useState, useEffect,  useContext } from 'react';
import Grid from '../global/Grid';
import GridButton from '../global/GridButton';
import API from '../api/API';

function Home() {

  const {user, setUser} = useContext(AuthContext)

  return (
    <>
      <Card>
        <div>
          {user ? (
            <div>
              <p>Welcome, {user.username}!</p>
              <Grid>
                  <Link to="/inventory-management">
                <GridButton>
                    Inventory Management
                </GridButton>
                  </Link>

                  <Link to="/analytics">
                <GridButton>
                    Analytics
                </GridButton>
                  </Link>

                  <Link to="/storefronts">
                <GridButton>
                    Store
                </GridButton>
                  </Link>

                  <Link to="/fulfillment">
                <GridButton>
                  Shipping Fulfillment
                </GridButton>
                  </Link>

                  <Link to="/customer-service">
                <GridButton>
                  Customer Service
                </GridButton>
                  </Link>

                  <Link to="/public-relations">
                <GridButton >
                  Public Relations
                </GridButton>
                  </Link>

                <Link to="/experimental">
                <GridButton>
                  Labs
                </GridButton>
                </Link>

                <Link to="/procurement">
                <GridButton>
                  Item Procurement
                </GridButton>
                </Link>

                <Link>
                <GridButton>
                  Dashboard Settings
                </GridButton>
                </Link>

              </Grid>
            </div>
          ) : (
            <p>Welcome to the home page!</p>
          )}
        </div>
      </Card>
    </>
  );
}

export default Home;